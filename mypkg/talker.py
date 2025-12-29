import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Person, "person", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0

    def cb(self):
        msg = Person()
        msg.name = "上田隆一"
        msg.age = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
