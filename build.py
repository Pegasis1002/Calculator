#!/usr/bin/env python3
import os
import platform
import subprocess
import sys
from pathlib import Path

def main():
    # Project configuration
    project_name = "MyCppProject"
    build_dir = "build"
    source_dir = "."
    generator = None  # Let CMake decide by default
    
    # Platform-specific configurations
    system = platform.system()
    is_windows = system == "Windows"
    is_linux = system == "Linux"
    
    if not (is_windows or is_linux):
        print(f"Unsupported operating system: {system}")
        return 1
    
    print(f"Configuring {project_name} for {system}...")
    
    # Create build directory if it doesn't exist
    Path(build_dir).mkdir(parents=True, exist_ok=True)
    
    # Platform-specific generator settings
    if is_windows:
        generator = "Visual Studio 17 2022"  # Modify if you need a different VS version
    # On Linux, we'll let CMake use the default generator (Unix Makefiles)
    
    # CMake configure command
    cmake_cmd = [
        "cmake",
        f"-S{source_dir}",
        f"-B{build_dir}",
    ]
    
    if generator:
        cmake_cmd.extend(["-G", generator])
    
    # Add any additional CMake options here
    # cmake_cmd.extend(["-DOPTION=Value"])
    
    # Run CMake configure
    print("Running CMake configure...")
    print(" ".join(cmake_cmd))
    try:
        subprocess.run(cmake_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"CMake configure failed: {e}")
        return 1
    
    # Build command
    build_cmd = [
        "cmake",
        "--build",
        build_dir,
        "--config",
        "Release" if is_windows else "",  # Config is relevant for multi-config generators
    ]
    
    # On Linux/macOS, you might want to specify parallel build
    if is_linux:
        import multiprocessing
        build_cmd.extend(["--", f"-j{multiprocessing.cpu_count()}"])
    
    # Run CMake build
    print("\nRunning build...")
    print(" ".join(build_cmd))
    try:
        subprocess.run(build_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        return 1
    
    print("\nBuild completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
