import os
import platform
import subprocess

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Machine": platform.machine(),
        "Node": platform.node(),
        "Processor": platform.processor(),
        "Release": platform.release(),
        "Python Version": platform.python_version()
    }
    return system_info

def get_installed_software():
    try:
        # Using wmic to list installed software
        installed_software = subprocess.check_output(
            ["wmic", "product", "get", "name,version"], 
            text=True
        )
        return installed_software.strip().splitlines()[1:]  # Skip the header
    except Exception as e:
        return str(e)

def get_hardware_info():
    hardware_info = {}
    # Get CPU info
    try:
        cpu_info = subprocess.check_output(["wmic", "cpu", "get", "name"], text=True)
        hardware_info["CPU"] = cpu_info.strip().splitlines()[1]
    except Exception as e:
        hardware_info["CPU"] = str(e)

    # Get RAM info
    try:
        ram_info = subprocess.check_output(["wmic", "memorychip", "get", "capacity"], text=True)
        ram_sizes = ram_info.strip().splitlines()[1:]  # Skip the header
        total_ram = sum(int(size) for size in ram_sizes)
        hardware_info["Total RAM (GB)"] = total_ram / (1024 ** 3)  # Convert bytes to GB
    except Exception as e:
        hardware_info["Total RAM"] = str(e)

    return hardware_info

def main():
    print("=== System Inventory ===")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\n=== Installed Software ===")
    installed_software = get_installed_software()
    for software in installed_software:
        print(software)

    print("\n=== Hardware Information ===")
    hardware_info = get_hardware_info()
    for key, value in hardware_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
