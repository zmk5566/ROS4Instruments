import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray

from pythonosc.dispatcher import Dispatcher
from typing import List, Any

from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient



class OSCPublisher(Node):

    def set_filter(self,address: str, *args: List[Any]) -> None:
        data = [float(x) for x in args]
        msg = Float32MultiArray()
        msg.data = data
        self.publisher_.publish(msg)
        print(f"Received message: {address} {data}")

    def __init__(self):
        super().__init__('osc_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'topic', 100)
        self.dispatcher = Dispatcher()
        self.dispatcher.map("/gyro*", self.set_filter)
        
        self.oscserver = BlockingOSCUDPServer(("0.0.0.0", 9500), self.dispatcher)
        self.oscserver.serve_forever()
        #self.timer = self.create_timer(timer_period, self.timer_callback)

def main(args=None):
    rclpy.init(args=args)

    osc_publisher = OSCPublisher()

    #rclpy.spin(osc_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #osc_publisher.destroy_node()
    #rclpy.shutdown()


if __name__ == '__main__':
    main()
