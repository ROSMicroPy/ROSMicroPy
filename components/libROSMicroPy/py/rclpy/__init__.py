import ROSMicroPy as _rm


_initialized = False
_current_node = None
_registered_types = {}
_startup_config = {
    "agent_ip": "192.16.0.50",
    "agent_port": "8888",
    "node_name": "turtle2",
    "namespace": "",
    "domain_id": None,
}


def unimplemented(*args, **kwargs):
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


class _UnsupportedMixin:
    def __getattr__(self, name):
        return unimplemented


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
        self.callback = callback
        self.is_canceled = False

    def cancel(self):
        self.is_canceled = True

    def reset(self):
        self.is_canceled = False


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
        return _rm.publishMsg(self.topic, msg)


class Subscription(_UnsupportedMixin):
    def __init__(self, topic, msg_type, callback):
        self.topic = topic
        self.msg_type = msg_type
        self.callback = callback


class Node(_UnsupportedMixin):
    def __init__(self, node_name, namespace=""):
        self._node_name = node_name
        self._namespace = namespace
        self._publishers = []
        self._subscriptions = []
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
        _rm.registerEventSubscription(topic, type_name, callback)
        subscription = Subscription(topic, msg_type, callback)
        self._subscriptions.append(subscription)
        return subscription

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
        self._timers = []
        return True


def init(args=None, context=None, domain_id=None, *extra_args, **extra_kwargs):
    global _initialized

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
    return None


def shutdown(*args, **kwargs):
    global _initialized, _current_node
    _initialized = False
    _current_node = None
    return unimplemented(*args, **kwargs)


def try_shutdown(*args, **kwargs):
    return shutdown(*args, **kwargs)


def ok(*args, **kwargs):
    return _initialized


def spin(node, executor=None):
    return _rm.run_ROS_Stack()


def spin_once(*args, **kwargs):
    return unimplemented(*args, **kwargs)


def spin_until_future_complete(*args, **kwargs):
    return unimplemented(*args, **kwargs)


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
    return unimplemented(*args, **kwargs)


def Parameter(*args, **kwargs):
    return unimplemented(*args, **kwargs)


def Future(*args, **kwargs):
    return unimplemented(*args, **kwargs)
