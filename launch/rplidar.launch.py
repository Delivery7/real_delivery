import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB1',
                'serial_baudrate': 256000, 
                'frame_id': 'map',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])
