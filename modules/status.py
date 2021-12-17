import os, requests, time

def getSiteStatus(url):
    request_response = requests.head(url)
    status_code = request_response.status_code
    status_code == 200

    if status_code == 200:
        return True
    else:
        return False

def isSiteReachable():
    print("Example: https://www.google.com")
    url = input("Enter URL: ")
    if getSiteStatus(url) == True:
        print("Site is reachable!")
    else:
        print("Site is not reachable!")

def fileStatus():
    file = input("Enter file path: ")
    if os.path.exists(file):
        modified = os.path.getmtime(file)
        created = os.path.getctime(file)
        accessed = os.path.getatime(file)

        print("Date modified:  " + time.ctime(modified))
        print("Date created:   " + time.ctime(created))
        print("Date accessed:   " + time.ctime(accessed))
    else:
        print("File path incorrect!")
