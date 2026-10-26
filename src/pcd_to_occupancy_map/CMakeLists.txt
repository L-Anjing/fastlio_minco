cmake_minimum_required(VERSION 3.16)
project(pcd_to_occupancy_map)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(PCL REQUIRED COMPONENTS common io)

add_executable(pcd_to_occupancy_map src/pcd_to_occupancy_map.cpp)
target_include_directories(pcd_to_occupancy_map PRIVATE
        ${PCL_INCLUDE_DIRS}
)
ament_target_dependencies(pcd_to_occupancy_map
        rclcpp
        nav_msgs
        sensor_msgs
)
target_link_libraries(pcd_to_occupancy_map
        ${PCL_LIBRARIES}
)

install(TARGETS pcd_to_occupancy_map
        DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY config launch
        DESTINATION share/${PROJECT_NAME})

ament_package()