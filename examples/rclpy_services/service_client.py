import logging

import rclpy
from rclpy.node import Node

from config import init_rclpy
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        self.logger = logging.getLogger("add_two_ints_client")
        self.logger.setLevel(logging.INFO)

        super().__init__("add_two_ints_client")
        self.client = self.create_client(AddTwoInts, "add_two_ints")
        self.a = 1
        self.b = 2
        self.future = None
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        if self.future is not None and not self.future.done():
            return

        request = AddTwoInts.Request()
        request.a = self.a
        request.b = self.b

        self.get_logger().info("Sending request: %d + %d" % (request.a, request.b))
        self.future = self.client.call_async(request)
        self.future.add_done_callback(self.response_callback)

        self.a += 1
        self.b += 1

    def response_callback(self, future):
        response = future.result()
        self.get_logger().info("Service response: sum=%d" % response.sum)


def main(args=None):
    init_rclpy(rclpy, "add_two_ints_client", args=args)

    node = AddTwoIntsClient()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
