import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HotpotTalker(Node):
    def __init__(self):
        super().__init__('hotpot_talker') 

        self.publisher = self.create_publisher(String, '/hotpot_chat', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 1 

    def timer_callback(self):
        msg = String()
        msg.data = f'Hotpot is the best! {self.count}'

        self.publisher.publish(msg)
        self.get_logger().info(f'发布: "{msg.data}"')

        self.count += 1

def main(args=None):
    rclpy.init(args=args)

    hotpot_talker = HotpotTalker()

    try:
        rclpy.spin(hotpot_talker)
    except KeyboardInterrupt:
        pass
    finally:
        hotpot_talker.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    
    