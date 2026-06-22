import logging

import rclpy
from rclpy.node import Node

from config import init_rclpy
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        self.logger = logging.getLogger("add_two_ints_server")
        self.logger.setLevel(logging.INFO)

        super().__init__("add_two_ints_server")
        self.service = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.add_two_ints_callback,
        )

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(
            "Incoming request: %d + %d = %d" % (request.a, request.b, response.sum)
        )
        return response


def main(args=None):
    init_rclpy(rclpy, "add_two_ints_server", args=args)

    node = AddTwoIntsServer()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
