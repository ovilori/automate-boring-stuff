import ctypes, sys
from datetime import date, datetime

stop_time = datetime(2021, 11, 22, 23, 0)

sites_to_block = ['www.twitter.com', 'twitter.com', 'www.linkedin.com', 'linkedin.com']
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    if datetime.now() < stop_time:
        print('Block sites')
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write(redirect + ' ' + site + '\n')
    else:
        print('Unblock sites')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()
else:
    #run with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__.join(sys.argv), None, 1)





