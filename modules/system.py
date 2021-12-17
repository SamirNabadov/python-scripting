import psutil, shutil, subprocess, platform

def osDetail():
    ip_address = subprocess.check_output("hostname --all-ip-addresses", shell=True, universal_newlines=True).split('\n')

    memory = psutil.virtual_memory()
    total_in_human_format = psutil._common.bytes2human(memory[0])

    disk_total, disk_used, disk_free = shutil.disk_usage("/")

    print(f"Architecture:                   {platform.architecture()[0]}")
    print(f"Machine type:                   {platform.machine()}")
    print(f"Hostname:                       {platform.node()}")
    print(f"Platform:                       {platform.platform()}")
    print(f"System’s release:               {platform.release()}")
    print(f"OS name:                        {platform.system()}")
    print(f"CPU Count:                      {psutil.cpu_count()}")
    print(f"Python version:                 {platform.python_version()}")
    print(f"RAM size:                       {total_in_human_format}")
    print(f"Hard Disk size:                 {disk_total // (2**30)}G")
    print(f"IP Addresses:                   {ip_address[0]}")

def disksinfo():
        values = []
        disk_partitions = psutil.disk_partitions(all=False)
        for partition in disk_partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            device = {'device': partition.device,
                      'mountpoint': partition.mountpoint,
                      'fstype': partition.fstype,
                      'opts': partition.opts,
                      'total': usage.total,
                      'used': usage.used,
                      'free': usage.free,
                      'percent': usage.percent
                      }
            values.append(device)
        values = sorted(values, key=lambda device: device['device'])
        return values

def diskDetail():
    for disk in disksinfo():
        print(f"Device:                     {disk['device']}")
        print(f"Mountpoint:                 {disk['mountpoint']}")
        print(f"Filesystem type:            {disk['fstype']}")
        print(f"Total:                      {disk['total'] // (2**30)}G")
        print(f"Used:                       {disk['used'] // (2**30)}G")
        print(f"Free:                       {disk['free'] // (2**30)}G")
        print(f"Persent:                    {disk['percent']}%")
        print("-------------------------------------")
