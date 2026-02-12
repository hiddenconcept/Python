import platform as pl
import psutil
import socket
from datetime import datetime


def get_size(bytes):
    """Convert bytes to human readable format"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


def display_system_info():
    print("=" * 60)
    print("SYSTEM INFORMATION".center(60))
    print("=" * 60)

    # ===== OS Information =====
    print("\n[OS Information]")
    uname = pl.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor or pl.processor()}")
    print(f"Architecture: {pl.architecture()[0]}")

    # ===== CPU Information =====
    print("\n[CPU Information]")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores (with hyperthreading): {psutil.cpu_count(logical=True)}")

    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    if cpufreq:
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

    # CPU usage per core
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent(interval=1)}%")

    # ===== Memory Information =====
    print("\n[Memory Information]")
    svmem = psutil.virtual_memory()
    print(f"Total RAM: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)} ({svmem.percent}%)")

    # Swap memory
    swap = psutil.swap_memory()
    print(f"\nSwap Total: {get_size(swap.total)}")
    print(f"Swap Used: {get_size(swap.used)} ({swap.percent}%)")
    print(f"Swap Free: {get_size(swap.free)}")

    # ===== Disk Information =====
    print("\n[Disk Information]")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"\nDevice: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)} ({partition_usage.percent}%)")
            print(f"  Free: {get_size(partition_usage.free)}")
        except PermissionError:
            print("  (Permission denied)")

    # ===== Network Information =====
    print("\n[Network Information]")
    print(f"Hostname: {socket.gethostname()}")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")

    # Network interfaces
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        print(f"\nInterface: {interface_name}")
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")

    # ===== Python Information =====
    print("\n[Python Information]")
    print(f"Python Version: {pl.python_version()}")
    print(f"Python Build: {pl.python_build()}")
    print(f"Python Compiler: {pl.python_compiler()}")

    # ===== Boot Time =====
    print("\n[System Boot Time]")
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    print(f"Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    display_system_info()