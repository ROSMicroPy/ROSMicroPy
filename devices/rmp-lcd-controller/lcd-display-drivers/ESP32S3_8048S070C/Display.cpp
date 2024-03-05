#include "Display.h"

extern "C"
{
    // we use two semaphores to sync the VSYNC event and the LVGL task, to avoid
    // potential tearing effect
    SemaphoreHandle_t sem_vsync_end;
    SemaphoreHandle_t sem_gui_ready;

    static lv_disp_draw_buf_t disp_buf; // contains internal graphic buffer(s) called draw buffer(s)
    static lv_disp_drv_t disp_drv;
    static esp_lcd_touch_handle_t tp = NULL;

    const char *TAG = "ESP32-8048S070c";

    // ESP_LOGI(TAG, "Install RGB LCD panel driver");
    esp_lcd_panel_handle_t panel_handle = NULL;

    esp_lcd_rgb_panel_config_t panel_config =
        {.clk_src = LCD_CLK_SRC_DEFAULT,
         .timings =
             {
                 .pclk_hz = LCD_PIXEL_CLOCK_HZ,
                 .h_res = LCD_H_RES,
                 .v_res = LCD_V_RES,
                 .hsync_pulse_width = 30,
                 .hsync_back_porch = 16,
                 .hsync_front_porch = 210,
                 .vsync_pulse_width = 13,
                 .vsync_back_porch = 10,
                 .vsync_front_porch = 22,
                 .flags =
                     {
                         .hsync_idle_low = (uint32_t)NULL,
                         .vsync_idle_low = (uint32_t)NULL,
                         .de_idle_high = (uint32_t)NULL,
                         .pclk_active_neg = true,
                         .pclk_idle_high = (uint32_t)NULL,
                     },
             },
         .data_width = 16, // RGB565 in parallel mode, thus 16bit in width
         .bits_per_pixel = (uint8_t)NULL,
         .num_fbs = LCD_NUM_FB,

#if CONFIG_EXAMPLE_USE_BOUNCE_BUFFER
         .bounce_buffer_size_px = 10 * h_resolution,
#else
         .bounce_buffer_size_px = (size_t)NULL,
#endif

         .sram_trans_align = (size_t)NULL,
         .psram_trans_align = 64,
         .hsync_gpio_num = PIN_NUM_HSYNC,
         .vsync_gpio_num = PIN_NUM_VSYNC,
         .de_gpio_num = PIN_NUM_DE,
         .pclk_gpio_num = PIN_NUM_PCLK,
         .disp_gpio_num = PIN_NUM_DISP_EN,

         .data_gpio_nums =
             {
                 PIN_NUM_DATA0,
                 PIN_NUM_DATA1,
                 PIN_NUM_DATA2,
                 PIN_NUM_DATA3,
                 PIN_NUM_DATA4,
                 PIN_NUM_DATA5,
                 PIN_NUM_DATA6,
                 PIN_NUM_DATA7,
                 PIN_NUM_DATA8,
                 PIN_NUM_DATA9,
                 PIN_NUM_DATA10,
                 PIN_NUM_DATA11,
                 PIN_NUM_DATA12,
                 PIN_NUM_DATA13,
                 PIN_NUM_DATA14,
                 PIN_NUM_DATA15,
             },
         .flags = {
             .disp_active_low = (uint32_t)NULL,
             .refresh_on_demand = (uint32_t)NULL,
             .fb_in_psram = true,
             .double_fb = (uint32_t)NULL,
             .no_fb = (uint32_t)NULL,
             .bb_invalidate_cache = (uint32_t)NULL,
         }};

    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = TOUCH_GT911_SDA, // select GPIO specific to your
                                       //   project
        .scl_io_num = TOUCH_GT911_SCL, // select GPIO specific to your
        // project
        .sda_pullup_en = GPIO_PULLUP_ENABLE,

        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master =
            {
                .clk_speed = 100000,
            },          // select frequency specific to your
                        //   project
        .clk_flags = 0, /*!< Optional, you can use
    I2C_SCLK_SRC_FLAG_*
    flags to choose i2c source clock here. */
    };

    esp_lcd_touch_config_t tp_cfg = {
        .x_max = LCD_H_RES,
        .y_max = LCD_V_RES,
        .rst_gpio_num = TOUCH_GT911_RST,
        .int_gpio_num = TOUCH_GT911_INT,
        .levels =
            {
                .reset = NULL,
                .interrupt = NULL,
            },
        .flags =
            {
                .swap_xy = 0,
                .mirror_x = 0,
                .mirror_y = 0,
            },
        .process_coordinates = NULL,
        .interrupt_callback = NULL,
    };

    bool on_vsync_event(esp_lcd_panel_handle_t panel,
                        const esp_lcd_rgb_panel_event_data_t *event_data,
                        void *user_data)
    {

        BaseType_t high_task_awoken = pdFALSE;

#if CONFIG_EXAMPLE_AVOID_TEAR_EFFECT_WITH_SEM
        if (xSemaphoreTakeFromISR(sem_gui_ready, &high_task_awoken) == pdTRUE)
        {
            xSemaphoreGiveFromISR(sem_vsync_end, &high_task_awoken);
        }
#endif

        return high_task_awoken == pdTRUE;
    }

    void lvgl_flush_cb(lv_disp_drv_t *drv, const lv_area_t *area, lv_color_t *color_map)
    {
        esp_lcd_panel_handle_t panel_handle = (esp_lcd_panel_handle_t)drv->user_data;

        int offsetx1 = area->x1;
        int offsetx2 = area->x2;
        int offsety1 = area->y1;
        int offsety2 = area->y2;

#if CONFIG_EXAMPLE_AVOID_TEAR_EFFECT_WITH_SEM
        xSemaphoreGive(sem_gui_ready);
        xSemaphoreTake(sem_vsync_end, portMAX_DELAY);
#endif

        // pass the draw buffer to the driver
        esp_lcd_panel_draw_bitmap(panel_handle, offsetx1, offsety1, offsetx2 + 1, offsety2 + 1, color_map);
        lv_disp_flush_ready(drv);
    }

#if CONFIG_EXAMPLE_LCD_TOUCH_ENABLED
    void lvgl_touch_cb(lv_indev_drv_t *drv, lv_indev_data_t *data)
    {
        const char *TAG = "ESP32-8048S070c";

        uint16_t touchpad_x[1] = {0};
        uint16_t touchpad_y[1] = {0};
        uint8_t touchpad_cnt = 0;

        /* Read touch controller data */
        esp_lcd_touch_read_data((esp_lcd_touch_handle_t)(drv->user_data));

        /* Get coordinates */
        bool touchpad_pressed = esp_lcd_touch_get_coordinates(
            (esp_lcd_touch_handle_t)(drv->user_data), touchpad_x, touchpad_y, NULL, &touchpad_cnt, 1);

        if (touchpad_pressed && touchpad_cnt > 0)
        {
            data->point.x = touchpad_x[0];
            data->point.y = touchpad_y[0];
            data->state = LV_INDEV_STATE_PRESSED;
        }
        else
        {
            data->state = LV_INDEV_STATE_RELEASED;
        }
    }
#endif

    void increase_lvgl_tick(void *arg)
    {
        /* Tell LVGL how many milliseconds has elapsed */
        lv_tick_inc(LVGL_TICK_PERIOD_MS);
    }

    /**
     *
     *
     */
    lv_disp_t *initDisplay()
    {
        lv_disp_t *disp = NULL;

        // #if CONFIG_EXAMPLE_AVOID_TEAR_EFFECT_WITH_SEM
        ESP_LOGI(TAG, "Create semaphores");
        sem_vsync_end = xSemaphoreCreateBinary();
        assert(sem_vsync_end);
        sem_gui_ready = xSemaphoreCreateBinary();
        assert(sem_gui_ready);

#if PIN_NUM_BK_LIGHT >= 0
        ESP_LOGI(TAG, "Turn off LCD backlight");
        gpio_config_t bk_gpio_config = {
            .pin_bit_mask = 1ULL << PIN_NUM_BK_LIGHT,
            .mode = GPIO_MODE_OUTPUT,
        };
        ESP_ERROR_CHECK(gpio_config(&bk_gpio_config));
#endif

        ESP_ERROR_CHECK(esp_lcd_new_rgb_panel(&panel_config, &panel_handle));

        ESP_LOGI(TAG, "Register event callbacks");
        esp_lcd_rgb_panel_event_callbacks_t cbs = {
            .on_vsync = on_vsync_event,
        };
        ESP_ERROR_CHECK(esp_lcd_rgb_panel_register_event_callbacks(panel_handle, &cbs,
                                                                   &disp_drv));

        ESP_LOGI(TAG, "Initialize RGB LCD panel");
        ESP_ERROR_CHECK(esp_lcd_panel_reset(panel_handle));
        ESP_ERROR_CHECK(esp_lcd_panel_init(panel_handle));

#if EXAMPLE_PIN_NUM_BK_LIGHT >= 0
        ESP_LOGI(TAG, "Turn on LCD backlight");
        gpio_set_level(PIN_NUM_BK_LIGHT, LCD_BK_LIGHT_ON_LEVEL);
#endif

        ESP_ERROR_CHECK(i2c_param_config(I2C_NUM_0, &conf));
        ESP_ERROR_CHECK(i2c_driver_install(I2C_NUM_0, I2C_MODE_MASTER, 0, 0, 0));

        esp_lcd_panel_io_handle_t tp_io_handle = NULL;
        esp_lcd_panel_io_i2c_config_t tp_io_config =
            ESP_LCD_TOUCH_IO_I2C_GT911_CONFIG();

        // Attach the TOUCH to the I2C bus
        ESP_ERROR_CHECK(esp_lcd_new_panel_io_i2c((esp_lcd_i2c_bus_handle_t)I2C_NUM_0,
                                                 &tp_io_config, &tp_io_handle));

        ESP_LOGI(TAG, "Initialize touch controller GT911");
        ESP_ERROR_CHECK(esp_lcd_touch_new_i2c_gt911(tp_io_handle, &tp_cfg, &tp));

        ESP_LOGI(TAG, "Initialize LVGL library");
        lv_init();

        // #endif

        void *buf1 = NULL;
        void *buf2 = NULL;

#if CONFIG_EXAMPLE_DOUBLE_FB
        ESP_LOGI(TAG, "Use frame buffers as LVGL draw buffers");
        ESP_ERROR_CHECK(
            esp_lcd_rgb_panel_get_frame_buffer(panel_handle, 2, &buf1, &buf2));
        // initialize LVGL draw buffers
        lv_disp_draw_buf_init(&disp_buf, buf1, buf2, LCD_H_RES * LCD_V_RES);
#else
        ESP_LOGI(TAG, "Allocate separate LVGL draw buffers from PSRAM");
        buf1 =
            heap_caps_malloc(LCD_H_RES * 100 * sizeof(lv_color_t), MALLOC_CAP_SPIRAM);
        assert(buf1);
        buf2 =
            heap_caps_malloc(LCD_H_RES * 100 * sizeof(lv_color_t), MALLOC_CAP_SPIRAM);
        assert(buf2);
        // initialize LVGL draw buffers
        lv_disp_draw_buf_init(&disp_buf, buf1, buf2, LCD_H_RES * 100);
#endif // CONFIG_EXAMPLE_DOUBLE_FB

        ESP_LOGI(TAG, "Register display driver to LVGL");
        lv_disp_drv_init(&disp_drv);
        disp_drv.hor_res = LCD_H_RES;
        disp_drv.ver_res = LCD_V_RES;
        disp_drv.flush_cb = lvgl_flush_cb;
        disp_drv.draw_buf = &disp_buf;
        disp_drv.user_data = panel_handle;

#if CONFIG_EXAMPLE_DOUBLE_FB
        disp_drv.full_refresh = true; // the full_refresh mode can maintain the
                                      // synchronization between the two frame buffers
#endif
        disp = lv_disp_drv_register(&disp_drv);

        ESP_LOGI(TAG, "Install LVGL tick timer");
        // Tick interface for LVGL (using esp_timer to generate 2ms periodic event)
        const esp_timer_create_args_t lvgl_tick_timer_args = {
            .callback = &increase_lvgl_tick, .name = "lvgl_tick"};
        esp_timer_handle_t lvgl_tick_timer = NULL;
        ESP_ERROR_CHECK(esp_timer_create(&lvgl_tick_timer_args, &lvgl_tick_timer));
        ESP_ERROR_CHECK(
            esp_timer_start_periodic(lvgl_tick_timer, LVGL_TICK_PERIOD_MS * 1000));

#if CONFIG_EXAMPLE_LCD_TOUCH_ENABLED
        static lv_indev_drv_t indev_drv; // Input device driver (Touch)
        lv_indev_drv_init(&indev_drv);
        indev_drv.type = LV_INDEV_TYPE_POINTER;
        indev_drv.disp = disp;
        indev_drv.read_cb = lvgl_touch_cb;
        indev_drv.user_data = tp;

        lv_indev_drv_register(&indev_drv);
#endif

        ESP_LOGI(TAG, "Display simple buttons example");

        return disp;
    }
}