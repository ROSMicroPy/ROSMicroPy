BRIDGE_ADDRESS = "192.168.8.100"
AGENT_PORT = "8888"
NAMESPACE = ""
DOMAIN_ID = 0


def init_rclpy(rclpy, node_name, args=None):
    return rclpy.init(
        args=args,
        bridge_address=BRIDGE_ADDRESS,
        agent_port=AGENT_PORT,
        node_name=node_name,
        namespace=NAMESPACE,
        domain_id=DOMAIN_ID,
    )
