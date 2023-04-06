import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray
import serial

ser = serial.Serial('/dev/ttyUSB0',115200)# Need to set the specific udev rule for it


def get_single_serial_output():
        xs = ser.read_until(b'\r\n').replace(b'\r\n', b'').decode('utf8').split(',')
        try:
            data = [int(x) for x in xs]
            print(data)
            return data
        except:
            print("An exception occurred") 
            return []

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'topic', 100)
        timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        while True:
            msg = Int32MultiArray()
            msg.data =get_single_serial_output()
            if (msg.data != []):
                self.publisher_.publish(msg)
            #print(data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    #rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
