import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 8080


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.client = SimpleUDPClient(ip, port)
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.client.send_message("/arduino/sensors", msg.data) 
        #self.get_logger().info('I heard: "%s"' % msg.data[0])


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

