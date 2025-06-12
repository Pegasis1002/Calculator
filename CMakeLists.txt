cmake_minimum_required(VERSION 3.10)

# Set the project name
project(MyProject)

# Add executable
add_executable(my_app src/main.cpp)

# Include directories
target_include_directories(my_app PRIVATE include)
