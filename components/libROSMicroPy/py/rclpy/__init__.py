import ROSMicroPy as _rm
import time as _time


_initialized = False
_current_node = None
_ros_stack_started = False
_service_topics = {}
_registered_types = {}
_startup_config = {
    "agent_ip": "192.16.0.50",
    "agent_port": "8888",
    "node_name": "turtle2",
    "namespace": "",
    "domain_id": None,
}


def _ticks_ms():
    ticks_ms = getattr(_time, "ticks_ms", None)
    if ticks_ms:
        return ticks_ms()
    return int(_time.monotonic() * 1000)


def _ticks_add(ticks, delta):
    ticks_add = getattr(_time, "ticks_add", None)
    if ticks_add:
        return ticks_add(ticks, delta)
    return ticks + delta


def _ticks_diff(ticks1, ticks2):
    ticks_diff = getattr(_time, "ticks_diff", None)
    if ticks_diff:
        return ticks_diff(ticks1, ticks2)
    return ticks1 - ticks2


def _sleep_ms(delay):
    sleep_ms = getattr(_time, "sleep_ms", None)
    if sleep_ms:
        sleep_ms(delay)
    else:
        _time.sleep(delay / 1000)


def unimplemented(function_name=None, *args, **kwargs):
    if function_name:
        print("unimplemented: {}".format(function_name))
    else:
        print("unimplemented")
    return None


def _type_data_map(msg_type):
    if isinstance(msg_type, str):
        return None

    getter = getattr(msg_type, "get_data_map", None)
    if getter:
        return getter()

    data_map = getattr(msg_type, "dataMap", None)
    if data_map is not None:
        return data_map

    return getattr(msg_type, "_DATA_MAP", None)


def _ensure_type_registered(msg_type):
    type_name = _resolve_type_name(msg_type)
    if type_name in _registered_types:
        return type_name

    data_map = _type_data_map(msg_type)
    if data_map is not None:
        registered = _rm.registerDataType(data_map)
        if registered:
            type_name = registered
        _registered_types[type_name] = True

    return type_name


def configure(agent_ip=None, bridge_address=None, agent_port=None, node_name=None, namespace=None, domain_id=None):
    if bridge_address is not None:
        agent_ip = bridge_address
    if agent_ip is not None:
        _startup_config["agent_ip"] = agent_ip
    if agent_port is not None:
        _startup_config["agent_port"] = str(agent_port)
    if node_name is not None:
        _startup_config["node_name"] = node_name
    if namespace is not None:
        _startup_config["namespace"] = namespace
    if domain_id is not None:
        _startup_config["domain_id"] = domain_id

    return dict(_startup_config)


def get_config():
    return dict(_startup_config)


def _apply_startup_config(node_name=None, namespace=None, domain_id=None):
    if node_name is not None:
        _startup_config["node_name"] = node_name
    if namespace is not None:
        _startup_config["namespace"] = namespace
    if domain_id is not None:
        _startup_config["domain_id"] = domain_id

    _rm.setAgentIP(_startup_config["agent_ip"])
    _rm.setAgentPort(_startup_config["agent_port"])
    _rm.setNodeName(_startup_config["node_name"])

    if _startup_config["namespace"]:
        _rm.setNamespace(_startup_config["namespace"])
    if _startup_config["domain_id"] is not None:
        _rm.setDomainID(_startup_config["domain_id"])


def _resolve_type_name(msg_type):
    if isinstance(msg_type, str):
        return msg_type

    name = getattr(msg_type, "_TYPE_NAME", None)
    if name:
        return name

    name = getattr(msg_type, "__name__", None)
    if name:
        return name

    return str(msg_type)


def _to_plain_data(value):
    if isinstance(value, dict):
        plain = {}
        for key, item in value.items():
            plain[key] = _to_plain_data(item)
        return plain

    items = getattr(value, "items", None)
    if items:
        plain = {}
        for key, item in items():
            plain[key] = _to_plain_data(item)
        return plain

    if isinstance(value, list):
        return [_to_plain_data(item) for item in value]

    if isinstance(value, tuple):
        return [_to_plain_data(item) for item in value]

    return value


def _from_plain_data(msg_type, value):
    if not isinstance(value, dict):
        return value

    if msg_type is dict:
        plain = {}
        for key, item in value.items():
            plain[key] = _from_plain_data(dict, item)
        return plain

    try:
        msg = msg_type()
    except Exception:
        msg = None

    if msg is None:
        return value

    for key, item in value.items():
        setattr(msg, key, _from_plain_data(dict, item))
    return msg


def _service_topic(service_name, suffix):
    service_name = service_name.strip("/")
    return "{}/_{}".format(service_name, suffix)


def _service_request_type(srv_type):
    return getattr(srv_type, "Request")


def _service_response_type(srv_type):
    return getattr(srv_type, "Response")


class _UnsupportedMixin:
    def __getattr__(self, name):
        def _unsupported(*args, **kwargs):
            return unimplemented(name, *args, **kwargs)

        _unsupported.__name__ = name
        return _unsupported


class Logger:
    def __init__(self, name):
        self.name = name

    def info(self, msg, *args):
        if args:
            msg = msg % args
        print(msg)

    def warning(self, msg, *args):
        if args:
            msg = msg % args
        print(msg)

    warn = warning

    def error(self, msg, *args):
        if args:
            msg = msg % args
        print(msg)


class Timer(_UnsupportedMixin):
    def __init__(self, period, callback):
        self.timer_period_ns = int(period * 1000000000)
        self._timer_period_ms = max(1, int(period * 1000))
        self._next_call_ms = _ticks_add(_ticks_ms(), self._timer_period_ms)
        self.callback = callback
        self.is_canceled = False

    def cancel(self):
        self.is_canceled = True

    def reset(self):
        self.is_canceled = False
        self._next_call_ms = _ticks_add(_ticks_ms(), self._timer_period_ms)

    def _call_if_ready(self):
        if self.is_canceled:
            return

        now = _ticks_ms()
        if _ticks_diff(now, self._next_call_ms) < 0:
            return

        self._next_call_ms = _ticks_add(now, self._timer_period_ms)
        self.callback()


class QoSProfile:
    def __init__(self, depth=10, reliability=None, durability=None, history=None):
        self.depth = depth
        self.reliability = reliability
        self.durability = durability
        self.history = history


qos_profile_default = QoSProfile()
qos_profile_sensor_data = QoSProfile(depth=5)


class Publisher(_UnsupportedMixin):
    def __init__(self, topic, msg_type):
        self.topic = topic
        self.msg_type = msg_type

    def publish(self, msg):
        return _rm.publishMsg(self.topic, _to_plain_data(msg))


class Subscription(_UnsupportedMixin):
    def __init__(self, topic, msg_type, callback, raw_callback=None):
        self.topic = topic
        self.msg_type = msg_type
        self.callback = callback
        self.raw_callback = raw_callback


class Future(_UnsupportedMixin):
    def __init__(self):
        self._done = False
        self._result = None
        self._exception = None
        self._callbacks = []

    def done(self):
        return self._done

    def result(self):
        if self._exception is not None:
            raise self._exception
        return self._result

    def exception(self):
        return self._exception

    def set_result(self, result):
        if self._done:
            return
        self._result = result
        self._done = True
        self._invoke_callbacks()

    def set_exception(self, exception):
        if self._done:
            return
        self._exception = exception
        self._done = True
        self._invoke_callbacks()

    def add_done_callback(self, callback):
        if self._done:
            callback(self)
        else:
            self._callbacks.append(callback)

    def _invoke_callbacks(self):
        callbacks = self._callbacks
        self._callbacks = []
        for callback in callbacks:
            callback(self)


class Service(_UnsupportedMixin):
    def __init__(self, node, srv_type, srv_name, callback):
        self.node = node
        self.srv_type = srv_type
        self.srv_name = srv_name
        self.callback = callback
        self.request_type = _service_request_type(srv_type)
        self.response_type = _service_response_type(srv_type)
        self.request_topic = _service_topic(srv_name, "request")
        self.response_topic = _service_topic(srv_name, "response")
        print("Init Service Server Response Publisher Name={}".format(self.response_topic))
        self.publisher = node.create_publisher(self.response_type, self.response_topic, 10)
        print("Init Service Server Request Subscription Name={}".format(self.request_topic))
        self.subscription = node.create_subscription(
            self.request_type,
            self.request_topic,
            self._handle_request,
            10,
        )

    def _handle_request(self, request):
        response = self.response_type()
        result = self.callback(request, response)
        if result is not None:
            response = result
        self.publisher.publish(response)


class Client(_UnsupportedMixin):
    def __init__(self, node, srv_type, srv_name):
        self.node = node
        self.srv_type = srv_type
        self.srv_name = srv_name
        self.request_type = _service_request_type(srv_type)
        self.response_type = _service_response_type(srv_type)
        self.request_topic = _service_topic(srv_name, "request")
        self.response_topic = _service_topic(srv_name, "response")
        self._pending = []
        self._response_subscription = None
        print("Init Service Client Request Publisher Name={}".format(self.request_topic))
        self.publisher = node.create_publisher(self.request_type, self.request_topic, 10)
        self.subscription = None

    def wait_for_service(self, timeout_sec=None):
        return True

    def service_is_ready(self):
        return True

    def call_async(self, request):
        self._ensure_response_subscription()
        future = Future()
        self._pending.append(future)
        self.publisher.publish(request)
        return future

    def call(self, request):
        future = self.call_async(request)
        spin_until_future_complete(self.node, future)
        return future.result()

    def _handle_response(self, response):
        if not self._pending:
            return
        future = self._pending.pop(0)
        future.set_result(response)

    def _ensure_response_subscription(self):
        if self._response_subscription is not None:
            return

        print("Init Service Client Response Subscription Name={}".format(self.response_topic))
        self._response_subscription = self.node.create_subscription(
            self.response_type,
            self.response_topic,
            self._handle_response,
            10,
        )
        self.subscription = self._response_subscription


class Node(_UnsupportedMixin):
    def __init__(self, node_name, namespace=""):
        self._node_name = node_name
        self._namespace = namespace
        self._publishers = []
        self._subscriptions = []
        self._services = []
        self._clients = []
        self._timers = []
        self._logger = Logger(node_name)

        _rm.setNodeName(node_name)
        if namespace:
            _rm.setNamespace(namespace)

    def create_publisher(self, msg_type, topic, qos_profile=None, *args, **kwargs):
        type_name = _ensure_type_registered(msg_type)
        _rm.registerROSPublisher(topic, type_name)
        publisher = Publisher(topic, msg_type)
        self._publishers.append(publisher)
        return publisher

    def create_subscription(self, msg_type, topic, callback, qos_profile=None, *args, **kwargs):
        type_name = _ensure_type_registered(msg_type)

        def _callback(msg):
            return callback(_from_plain_data(msg_type, msg))

        _rm.registerEventSubscription(topic, type_name, _callback)
        subscription = Subscription(topic, msg_type, callback, raw_callback=_callback)
        self._subscriptions.append(subscription)
        return subscription

    def create_service(self, srv_type, srv_name, callback, qos_profile=None, callback_group=None):
        service = Service(self, srv_type, srv_name, callback)
        self._services.append(service)
        _service_topics[srv_name] = True
        return service

    def create_client(self, srv_type, srv_name, qos_profile=None, callback_group=None):
        client = Client(self, srv_type, srv_name)
        self._clients.append(client)
        return client

    def create_timer(self, timer_period_sec, callback, callback_group=None, clock=None):
        timer = Timer(timer_period_sec, callback)
        self._timers.append(timer)
        return timer

    def get_logger(self):
        return self._logger

    def get_name(self):
        return self._node_name

    def get_namespace(self):
        return self._namespace

    def destroy_node(self):
        self._publishers = []
        self._subscriptions = []
        self._services = []
        self._clients = []
        self._timers = []
        return True


def init(args=None, context=None, domain_id=None, *extra_args, **extra_kwargs):
    global _initialized, _ros_stack_started

    bridge_address = extra_kwargs.pop("bridge_address", None)
    agent_ip = extra_kwargs.pop("agent_ip", None)
    agent_port = extra_kwargs.pop("agent_port", None)
    node_name = extra_kwargs.pop("node_name", None)
    namespace = extra_kwargs.pop("namespace", None)

    configure(
        agent_ip=agent_ip,
        bridge_address=bridge_address,
        agent_port=agent_port,
        node_name=node_name,
        namespace=namespace,
        domain_id=domain_id,
    )

    _apply_startup_config()
    _rm.init_ROS_Stack()
    _initialized = True
    _ros_stack_started = False
    return None


def shutdown(*args, **kwargs):
    global _initialized, _current_node, _ros_stack_started
    _initialized = False
    _current_node = None
    _ros_stack_started = False
    return None


def try_shutdown(*args, **kwargs):
    global _initialized, _current_node, _ros_stack_started
    _initialized = False
    _current_node = None
    _ros_stack_started = False
    return None


def ok(*args, **kwargs):
    return _initialized


def spin(node, executor=None):
    global _ros_stack_started

    if not _ros_stack_started:
        _rm.run_ROS_Stack()
        _ros_stack_started = True

    try:
        while ok():
            for timer in tuple(getattr(node, "_timers", ())):
                timer._call_if_ready()
            _sleep_ms(10)
    except KeyboardInterrupt:
        pass

    return None


def spin_once(*args, **kwargs):
    node = args[0] if args else kwargs.get("node", None)
    if node is not None:
        for timer in tuple(getattr(node, "_timers", ())):
            timer._call_if_ready()
    _sleep_ms(10)
    return None


def spin_until_future_complete(node, future, executor=None, timeout_sec=None):
    start = _ticks_ms()
    timeout_ms = None if timeout_sec is None else int(timeout_sec * 1000)

    while ok() and not future.done():
        spin_once(node)
        if timeout_ms is not None and _ticks_diff(_ticks_ms(), start) >= timeout_ms:
            break

    return future


def create_node(node_name, namespace="", context=None, cli_args=None, use_global_arguments=True, enable_rosout=True, start_parameter_services=True, parameter_overrides=None, allow_undeclared_parameters=False, automatically_declare_parameters_from_overrides=False):
    global _current_node

    node = Node(node_name, namespace=namespace)
    _current_node = node
    return node


def get_default_context(*args, **kwargs):
    return None


def get_global_executor(*args, **kwargs):
    return None


def create_rate(*args, **kwargs):
    return unimplemented("create_rate", *args, **kwargs)


def Parameter(*args, **kwargs):
    return unimplemented("Parameter", *args, **kwargs)
