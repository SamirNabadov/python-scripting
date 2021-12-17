import datetime, psutil, time, os

def getUptime():
    n = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    m, s = divmod(n.seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return f"{h}:{m}:{s}, days {n.days}"

def getNowtime():
    process = psutil.Process(os.getpid())
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(process.create_time()))
    return f"{nowTime}"

def timeDetails():
    print(f"current time: {getNowtime()}")
    print(f"uptime: {getUptime()}")