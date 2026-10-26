
import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    bringup_dir = get_package_share_directory('pcd_to_occupancy_map')
    params_file = os.path.join(bringup_dir, 'config', 'pcd_to_occupancy_map.yaml')

    pcd_file = LaunchConfiguration('pcd_file')

    return LaunchDescription([
        DeclareLaunchArgument('pcd_file', description = '先验 PCD 地图绝对路径'),
        Node(
            package = 'pcd_to_occupancy_map',
            executable = 'pcd_to_occupancy_map',
            name = 'pcd_to_occupancy_map',
            output = 'screen',
            parameters = [params_file, {'pcd_file': pcd_file}],
        ),
    ])