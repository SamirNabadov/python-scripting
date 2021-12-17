import subprocess
from datetime import datetime

def readAndParsePasswd(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            if int(line.split(":")[2]) == 0 or int(line.split(":")[2]) >= 1000:
                data.append(line.split(":")[0])
        data.sort()
    return data

def getPasswordExpiryFromChage(account):
    try:
        chage = subprocess.Popen(('chage', '-l', account), shell=False, stdout=subprocess.PIPE, universal_newlines=True)
        grep = subprocess.Popen(('grep', 'Account expires'), shell=False, stdin=chage.stdout, stdout=subprocess.PIPE, universal_newlines=True)
        cut = subprocess.Popen('cut -d : -f2'.split(), shell=False,  stdin=grep.stdout, stdout=subprocess.PIPE, universal_newlines=True)
        output = cut.communicate()[0].strip()
        return output if output != 'never' else None
    except subprocess.CalledProcessError as e:
        return None

def isGoingToExpire(chage_date):
    BUFFER_DURATION = 60 # in days
    expiry_date = datetime.strptime(chage_date, '%b %d, %Y')
    today = datetime.now()
    return abs((expiry_date - today).days) <= BUFFER_DURATION

def checkExpire():
    accounts = readAndParsePasswd("/etc/passwd")
    for account in accounts:
        chage_date = getPasswordExpiryFromChage(account)

        if chage_date != None and isGoingToExpire(chage_date):
            print(f"{account} is going to expire on {chage_date}")
        else:
            print(f"{account} have not expire time")
