from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys
from time import sleep 
import os

PHASE2_LOG = '../results/phase_2_report'

class Testing(object):

	def __init__(self, net):
		self.net = net
		self.h1 = self.net.get('h1')
		self.h2 = self.net.get('h2')
		self.h3 = self.net.get('h3')
		self.h4 = self.net.get('h4')
		self.ds1 = self.net.get('h5')
		self.ds2 = self.net.get('h6')
		self.ds3 = self.net.get('h7')
		self.ws1 = self.net.get('h8')
		self.ws2 = self.net.get('h9')
		self.ws3 = self.net.get('h10')
		self.file = open('phase_2_report', 'w')



	def parsePing(self, test_message):
		"Parse"
		if 'Destination Host Unreachable' in test_message:
			return False
		if 'Network is unreachable' in test_message:
			return False
		if '100% packet loss' in test_message:		
			return False
		if '0% packet loss' in test_message:
			return True
		else:
			return True 

	def parseDNS(self, test_message):
		if "connection timed out" in test_message:
			return False
        else:
			return True

	def parseTCP(self, test_message):
		if "<html>" in test_message:
			return True
		if "Connection timed out" in test_message:
			return False
		else:
			return False

	def pingTest(self):
		ping_success = 0
		ping_total = 0
	
        self.file.write("======================Ping Test=====================\n")

		# H1 Ping H2
		result1 = self.h1.cmdPrint('ping -c 1 100.0.0.11')
		self.file.write('H1 -> H2 :'+result1)
		if self.parsePing(result1):
			self.file.write('H1 -> H2 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H1 -> H2 : Failed\n\n')
			ping_total = ping_total+1

		# H1 Ping H3
        result2 = self.h1.cmdPrint('ping -c 1 100.0.0.50')
       	self.file.write('H1 -> H3 :'+result2+)
		if self.parsePing(result2):
			self.file.write('H1 -> H3 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
        	else:
           		self.file.write('H1 -> H3 : Failed\n\n')
			ping_total = ping_total+1

		# H1 Ping H4
        result3 = self.h1.cmdPrint('ping -c 1 100.0.0.51')
       	self.file.write('H1 -> H4 :'+result3+)
		if self.parsePing(result3):
			self.file.write('H1 -> H4 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
        	else:
           		self.file.write('H1 -> H4 : Failed\n\n')
			ping_total = ping_total+1

		# H1 Ping Load Balancer 1
		result4 = self.h1.cmdPrint('ping -c 1 100.0.0.25')
		self.file.write('H1 -> Load Balancer 1 :'+result4)
		if self.parsePing(result4):
			self.file.write('H1 -> Load Balancer 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H1 -> Load Balancer 1 : Failed\n\n')
			ping_total = ping_total+1

		# H1 Ping Load Balancer 2
		result5 = self.h1.cmdPrint('ping -c 1 100.0.0.45')
		self.file.write('H1 -> Load Balancer 2 :'+result5)
		if self.parsePing(result5):
			self.file.write('H1 -> Load Balancer 2 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H1 -> Load Balancer 2 : Failed\n\n')
			ping_total = ping_total+1
		
		# H1 Ping Web Server 1
		result6 = self.h1.cmdPrint('ping -c 1 100.0.0.40')
		self.file.write('H1 -> Web Server 1 :'+result6)
		if self.parsePing(result6):
			self.file.write('H1 -> Web Server 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H1 -> Web Server 1 : Failed\n\n')
			ping_total = ping_total+1
        
        # H1 Ping DNS Server 1
		result7 = self.h1.cmdPrint('ping -c 1 100.0.0.20')
		self.file.write('H1 -> DNS Server 1 :'+result7)
		if self.parsePing(result7):
			self.file.write('H1 -> DNS Server 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H1 -> DNS Server 1 : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping H4
		result8 = self.h3.cmdPrint('ping -c 1 100.0.0.52')
		self.file.write('H3 -> H4 :'+result8)
		if self.parsePing(result8):
			self.file.write('H3 -> H4 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H3 -> H4 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping H3
		result9 = self.h2.cmdPrint('ping -c 1 100.0.0.50')
		self.file.write('H2 -> H3 :'+result9)
		if self.parsePing(result9):
			self.file.write('H2 -> H3 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> H3 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping H4
		result10 = self.h2.cmdPrint('ping -c 1 100.0.0.51')
		self.file.write('H2 -> H4 :'+result9)
		if self.parsePing(result9):
			self.file.write('H2 -> H4 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> H4 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping Load Balancer 1
		result10 = self.h2.cmdPrint('ping -c 1 100.0.0.25')
		self.file.write('H2 -> Load Balancer 1 :'+result10)
		if self.parsePing(result10):
			self.file.write('H2 -> Load Balancer 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> Load Balancer 1 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping Load Balancer 2
		result11 = self.h2.cmdPrint('ping -c 1 100.0.0.45')
		self.file.write('H2 -> Load Balancer 2 :'+result11)
		if self.parsePing(result11):
			self.file.write('H2 -> Load Balancer 2 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> Load Balancer 2 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping DNS Server 1
		result12 = self.h2.cmdPrint('ping -c 1 100.0.0.20')
		self.file.write('H2 -> DNS Server 1 :'+result12)
		if self.parsePing(result12):
			self.file.write('H2 -> DNS Server 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> H3 : Failed\n\n')
			ping_total = ping_total+1

		# H2 Ping Web Server 1
		result13 = self.h2.cmdPrint('ping -c 1 100.0.0.40')
		self.file.write('H2 -> Web Server 1 :'+result13)
		if self.parsePing(result13):
			self.file.write('H2 -> Web Server 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H2 -> Web Server 1 : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping H1
		result14 = self.h3.cmdPrint('ping -c 1 100.0.0.10')
		self.file.write('H3 -> H1 :'+result14)
		if self.parsePing(result14):
			self.file.write('H3 -> H1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H3 -> H1 : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping H2
		result15 = self.h3.cmdPrint('ping -c 1 100.0.0.11')
		self.file.write('H3 -> H2 :'+result15)
		if self.parsePing(result15):
			self.file.write('H3 -> H2 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H3 -> H2 : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping Load Balancer 1
		result16 = self.h3.cmdPrint('ping -c 1 100.0.0.25')
		self.file.write('H3 -> Load Balancer 1 :'+result16)
		if self.parsePing(result16):
			self.file.write('H3 -> Load Balancer 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H3 -> Load Balancer 1 : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping Load Balancer 2
		result17 = self.h3.cmdPrint('ping -c 1 100.0.0.45')
		self.file.write('H3 -> Load Balancer :'+result17)
		if self.parsePing(result17):
			self.file.write('H3 -> Load Balancer : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
		else:
			self.file.write('H3 -> Load Balancer : Failed\n\n')
			ping_total = ping_total+1

		# H3 Ping DNS Server 1
		result18 = self.h3.cmdPrint('ping -c 1 100.0.0.20')
		self.file.write('H3 -> DNS Server 1 :'+result18)
		if self.parsePing(result18):
            self.file.write('H3 -> DNS Server 1 : Success\n\n')
			ping_success = ping_success+1
			ping_total = ping_total+1
        else:
        	self.file.write('H3 -> DNS Server 1 : Failed\n\n')
			ping_total = ping_total+1
		
		# H3 Ping Web Server 1
        result19 = self.h3.cmdPrint('ping -c 1 100.0.0.40')
       	self.file.write('H3 -> Web Server 1 :'+result19)
       	if self.parsePing(result19):
       		self.file.write('H3 -> Web Server 1 : Success\n\n')
       		ping_success = ping_success+1
			ping_total = ping_total+1       		
		else:
			self.file.write('H3 -> Web Server 1 : Failed\n\n')
			ping_total = ping_total+1

		ping_rate = ping_success/ping_total*100
		print("\nICMP Ping tests finished!\n Conclusion: "+str(ping_total)+"ICMP packets sent in total, "+str(ping_success)+" was success.\n")
		self.file.write("\nICMP Ping tests finished!\n Conclusion: "+str(ping_total)+"ICMP packets sent in total, "+str(ping_success)+" was success.\n")
		self.file.write("The success rate is "+str(ping_rate)+"%.\n")


	def dnsTest(self):

		dns_success = 0
		dns_total = 0
		self.ds1.cmdPrint('python ds1.py &')
		self.ds2.cmdPrint('python ds2.py &')
		self.ds3.cmdPrint('python ds3.py &')
		
		sleep(2)

		self.file.write('=======================DNS Test=======================\n')

		# H1 Dig ws1.com to Load Balancer 1 port 53
		result1 = self.h1.cmdPrint('dig -p 53 @100.0.0.25 ws1.com')
		self.file.write('H1 dig Load Balancer 1 to port 53:\n'+result1)
		if self.parseDNS(result1):
			self.file.write("H1 dig Load Balancer 1 to port 53: Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("H1 dig Load Balancer 1 to port 53: Failed\n\n")
			dns_total = dns_total+1
		
		# H1 Dig ws1.com to Load Balancer 1 port 60
		result2 = self.h1.cmdPrint('dig -p 60 @100.0.0.25 ws1.com')
		self.file.write('H1 dig Load Balancer 1 to port 60:\n'+result2)
		if self.parseDNS(result2):
			self.file.write("H1 dig Load Balancer 1 to port 60: Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("H1 dig Load Balancer 1 to port 60: Failed\n\n")
			dns_total = dns_total+1
                
		# H1 Dig ws1.com to Load Balancer 1 port 100
		result3 = self.h1.cmdPrint('dig -p 100 @100.0.0.25 ws1.com')
		self.file.write('H1 dig Load Balancer 1 to port 100:\n'+result3)
		if self.parseDNS(result3):
			self.file.write("H1 dig Load Balancer 1 to port 100: Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("H1 dig Load Balancer 1 to port 100: Failed\n\n")
			dns_total = dns_total+1
                
		# H3 Dig ws1.com to Load Balancer 1 port 53
		result4 = self.h3.cmdPrint('dig -p 53 @100.0.0.25 ws1.com')
		self.file.write('h3 dig ds2 to port 53:\n'+result4)
		if self.parseDNS(result4):
			self.file.write("Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("Failed\n\n")
			dns_total = dns_total+1
                
		# H3 Dig ws1.com to Load Balancer 1 port 60
		result5 = self.h3.cmdPrint('dig -p 60 @100.0.0.25 ws1.com')
		self.file.write('h3 dig ds2 to port 60:\n'+result5)
		if self.parseDNS(result5):
			self.file.write("Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("Failed\n\n")
			dns_total = dns_total+1
                
		# H3 Dig ws1.com to Load Balancer 1 port 100
		result6 = self.h3.cmdPrint('dig -p 100 @100.0.0.25 ws1.com')
		self.file.write('h3 dig ds2 to port 100:\n'+result6)
		if self.parseDNS(result6):
			self.file.write("Success\n\n")
			dns_success = dns_success+1
			dns_total = dns_total+1
		else:
			self.file.write("Failed\n\n")
			dns_total = dns_total+1

		dns_rate = dns_success/dns_total*100
		print("\nDNS Tests finished!\n Conclusion: "+str(dns_total)+" DNS requests sent. "+ str(dns_success)+" was success\n")
		self.file.write("\nDNS Tests finished!\n Conclusion: "+str(dns_total)+" DNS requests sent. "+ str(dns_success)+" was success\n")
		self.file.write("The success rate is "+dns_rate+"%.\n")
		self.ds1.cmdPrint('kill %python')
		self.ds2.cmdPrint('kill %python')
		self.ds3.cmdPrint('kill %python')

	def tcpTest(self):
		
		tcp_success = 0
		tcp_total = 0

		self.file.write('====================TCP Test====================\n')
    
		self.ws1.cmdPrint('python -m SimpleHTTPServer 80 &')
		self.ws2.cmdPrint('python -m SimpleHTTPServer 80 &')
		self.ws3.cmdPrint('python -m SimpleHTTPServer 80 &')
		self.insp.cmdPrint('tcpdump -w insp.pcap &')

		sleep(2)

		# H1 curl Web port 80 method POST
		result1 = self.h1.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n\n'+result1+'\n')
		if self.parseTCP(result1):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1
	
		# H1 curl Web port 90 method POST
		result2 = self.h1.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:90')
		self.file.write('H1 -> Web Port 90:\n'+result2+'\n\n')
		if self.parseTCP(result2):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1
                
		# H1 curl Web port 100 method POST
		result3 = self.h1.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:100')
		self.file.write('H1 -> Web Port 100:\n'+result3+'\n\n')
		if self.parseTCP(result3):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web port 80 method GET
		result4 = self.h1.cmdPrint('curl --max-time 20 http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result4+'\n\n')
		if self.parseTCP(result4):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web port 80 method HEAD
		result5 = self.h1.cmdPrint('curl --max-time 20 -I http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result4+'\n\n')
		if self.parseTCP(result4):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method OPTIONS
		result6 = self.h1.cmdPrint('curl --max-time 20 -X OPTIONS http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result6+'\n\n')
		if self.parseTCP(result6):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method TRACE
		result7 = self.h1.cmdPrint('curl --max-time 20 -v http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result7+'\n\n')
		if self.parseTCP(result7):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT
		result8 = self.h1.cmdPrint('curl --max-time 20 -X PUT http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result8+'\n\n')
		if self.parseTCP(result8):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method DELETE
		result9 = self.h1.cmdPrint('curl --max-time 20 -X DELETE http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result9+'\n\n')
		if self.parseTCP(result9):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method CONNECT
		result10 = self.h1.cmdPrint('curl --max-time 20 -X CONNECT http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result10+'\n\n')
		if self.parseTCP(result10):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT SQL cat /var/log/
		result11 = self.h1.cmdPrint('curl --max-time 20 -X PUT -d "cat /var/log/" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result11+'\n\n')
		if self.parseTCP(result11):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT SQL cat /etc/passwd/
		result12 = self.h1.cmdPrint('curl --max-time 20 -X PUT -d "cat /etc/passwd" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result12+'\n\n')
		if self.parseTCP(result12):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT SQL INSERT
		result13 = self.h1.cmdPrint('curl --max-time 20 -X PUT -d "INSERT" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result13+'\n\n')
		if self.parseTCP(result13):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT SQL UPDATE
		result14 = self.h1.cmdPrint('curl --max-time 20 -X PUT -d "UPDATE" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result14+'\n\n')
		if self.parseTCP(result14):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H1 curl Web Port 80 method PUT SQL DELETE
		result15 = self.h1.cmdPrint('curl --max-time 20 -X PUT -d "DELETE" http://100.0.0.45:80')
		self.file.write('H1 -> Web Port 80:\n'+result15+'\n\n')
		if self.parseTCP(result15):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method POST
		result16 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result16+'\n')
		if self.parseTCP(result16):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1
                
		# H3 curl Web port 90 method POST
		result17 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:90')
		self.file.write('H3 -> Web Port 80:\n\n'+result17+'\n')
		if self.parseTCP(result17):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1
                
		# H3 curl Web port 100 method POST
		result18 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:100')
		self.file.write('H1 -> Web Port 100:\n\n'+result18+'\n')
		if self.parseTCP(result18):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method GET
		result19 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result19+'\n')
		if self.parseTCP(result19):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method HEAD
		result20 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result20+'\n')
		if self.parseTCP(result20):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method OPTIONS
		result21 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result21+'\n')
		if self.parseTCP(result21):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method TRACE
		result22 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result22+'\n')
		if self.parseTCP(result22):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT
		result23 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result23+'\n')
		if self.parseTCP(result23):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method DELETE
		result24 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result24+'\n')
		if self.parseTCP(result24):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method CONNECT
		result25 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result25+'\n')
		if self.parseTCP(result25):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT SQL cat /var/log
		result26 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result26+'\n')
		if self.parseTCP(result26):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT SQL cat /etc/passwd/
		result27 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result27+'\n')
		if self.parseTCP(result27):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT SQL INSERT
		result28 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result28+'\n')
		if self.parseTCP(result28):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT SQL UPDATE
		result29 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result29+'\n')
		if self.parseTCP(result29):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		# H3 curl Web port 80 method PUT SQL DELETE
		result30 = self.h3.cmdPrint('curl --max-time 20 -d "user=admin&passwd=12345678" http://100.0.0.45:80')
		self.file.write('H3 -> Web Port 80:\n\n'+result30+'\n')
		if self.parseTCP(result30):
			self.file.write("Success\n\n")
			tcp_success = tcp_success+1
			tcp_total = tcp_total+1
		else:
			self.file.write("Failed\n\n")
			tcp_total = tcp_total+1

		self.file.write("\n HTTP tests finished! Conclusion: "+str(tcp_total)+" TCP packets sent. "+str(tcp_success)+" was success\n")

	def run_tests(self):
		log = open(PHASE2_LOG, 'w+')
		self.pingTest()
		self.file.write("\n\n")
		self.dnsTest()
		self.file.write("\n\n")
		self.tcpTest()
		self.file.write("================Auto tests finished=================")
		self.file.close()

