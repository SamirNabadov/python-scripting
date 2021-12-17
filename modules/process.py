import subprocess, psutil, os, re

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           listOfProcObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

def getProcessHighestMemoryUsage():
    count = int(input("Enter process count for get result process with highest memory usage: "))
    listOfRunningProcess = getListOfProcessSortedByMemory()
    for elem in listOfRunningProcess[:count] :
        print('--------------------------------------------------------------')
        print(f"pid: {elem.get('pid')}, name: {elem.get('name')}, username: {elem.get('username')}, vms: {elem.get('vms')}MB")

    print('--------------------------------------------------------------')

#---------------------------------------------------------------------------------------------

def processCheck(proc_name):
    ps = subprocess.Popen("ps ax -o pid= -o args= ", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    ps_pid = ps.pid
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()

    for line in output.split("\n"):
        res = re.findall("(\d+) (.*)", line)
        if res:
            pid = int(res[0][0])
            if proc_name in res[0][1] and pid != os.getpid() and pid != ps_pid:
                return True
    return False

def processExists():
    process = input("Enter process name: ")
    if processCheck(process) is True:
        print(f"Process active!")
    else:
        print(f"Process dead!")