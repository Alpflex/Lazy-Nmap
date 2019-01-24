

import nmap
import sys
import os

scanner = nmap.PortScanner()

print("""                                           
                                           
 __          ___      ________  ____    ____    .__   __. .___  ___.      ___      .______   
|  |        /   \    |       /  \   \  /   /    |  \ |  | |   \/   |     /   \     |   _  \  
|  |       /  ^  \   `---/  /    \   \/   /     |   \|  | |  \  /  |    /  ^  \    |  |_)  | 
|  |      /  /_\  \     /  /      \_    _/      |  . `  | |  |\/|  |   /  /_\  \   |   ___/  
|  `----./  _____  \   /  /----.    |  |        |  |\   | |  |  |  |  /  _____  \  |  |      
|_______/__/     \__\ /________|    |__|        |__| \__| |__|  |__| /__/     \__\ | _|      
 
Mayde By ISAK   //https://github.com/Alpflex                                                                                           


 """)


#class Nmap:



#    def __init__(self):
#        self.nmap.version_number = 0    # Version for Nmap



# 192.168.10.1


val = input("""\nPlease enter the type of scan you want to run
                1)Simple Scan
                2)Medium Scan 
                3)Intensive Scan \n""")
print("You have selected option: ", val)







if val == "1":
    enkelVal = input("""\nPlease enter the type of scan you want to run
                    1)Version check
                    2)Check if a device is live
                    3)Check all devices of all internet \n""")
    print("You have selected option: ", val)




if val == "1":
    def version_nmap(version):
        command = "nmap " + version + "  "
        process = os.popen(command)
        results = str(process.read())
        return results

    print(version_nmap('-V'))


elif val == "2":
    def ping_scan(ip):
        command = "nmap " "-sn " + ip
        process = os.popen(command)
        results = str(process.read())
        #ip = input("Whats the IP-Adress?")
        return results


    ip = input("Whats the IP-Adress?")
    print(ping_scan(ip))
######################################################################
