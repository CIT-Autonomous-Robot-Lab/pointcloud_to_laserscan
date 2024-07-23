from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    pc2_to_scan = Node(
        package='pointcloud_to_laserscan',
        executable='pointcloud_to_laserscan_node',
        name='pointcloud_to_laserscan',
        remappings=[('cloud_in', '/livox/lidar'),
                    ('scan', '/scan')],
        parameters=[{
            'target_frame': 'livox_frame',
            'transform_tolerance': 0.01,
            'min_height': 0.0,
            'max_height': 0.2,
            'angle_min': -3.1415,
            'angle_max': 3.1415,
            'angle_increment': 0.0087,  # M_PI/360.0
            'scan_time': 0.3333,
            'range_min': 0.45,
            'range_max': 10.0,
            'use_inf': True,
            'inf_epsilon': 1.0
        }],
        output='screen',
    )

    ld = LaunchDescription()
    ld.add_action(pc2_to_scan)

    return ld
