import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hirose/fresh_ros2_ws/src/fresh_package/install/fresh_package'
