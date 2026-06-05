# ROSMicroPy Web Loader

This directory is a GitHub Pages-ready firmware loader for ROSMicroPy Core boards.

Open `index.html` from GitHub Pages in a browser with Web Serial support, connect the board over USB, and select **Install ROSMicroPy Core**. ESP Web Tools detects the chip family and flashes the matching build from `manifest.json`.

Supported builds:

- `rmp_core_generic` for generic ESP32 boards
- `rmp_core_s3` for ESP32-S3 boards

The firmware files in `firmware/` are copied from the top-level `release/` directory.
