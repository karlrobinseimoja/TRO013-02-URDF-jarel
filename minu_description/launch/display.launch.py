"""RViz2 visualiseerimine - roboti mudeli kuvamine."""
import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg = get_package_share_directory('minu_description')

    use_sim_time = LaunchConfiguration('use_sim_time')
    model_arg = DeclareLaunchArgument(
        'model',
        default_value=os.path.join(pkg, 'urdf', 'yahboom_robot.urdf.xacro'),
    )
    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
    )

    robot_description = ParameterValue(
    Command([
        'xacro ',
        LaunchConfiguration('model')
    ]),
    value_type=str
)

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': use_sim_time,
        }],
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=launch.conditions.UnlessCondition(use_sim_time),
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg, 'rviz', 'robot.rviz')],
        parameters=[{'use_sim_time': use_sim_time}],
    )

    return LaunchDescription([
        model_arg,
        sim_time_arg,
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz,
    ])
