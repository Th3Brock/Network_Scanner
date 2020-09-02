from scapy.all import ARP, Ether, srp

def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

       _   __     __                      __      _____                                 
      / | / /__  / /__      ______  _____/ /__   / ___/_________ _____  ____  ___  _____
     /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
    / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<     ___/ / /__/ /_/ / / / / / / /  __/ /    
   /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                                                     
         Nota! : Scanning Port es un escaner 100% funcional, verifique con nmap.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()
target_ip = "192.168.1.1/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))