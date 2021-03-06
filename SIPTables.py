#!/bin/env Python3
import argparse
import socket


def wizard():
	print("Destination IP of Package * for all")
	dIP = input()
	print("Destination Port of Package * for all")
	dport = input()
	print("IP and/or Port Package to send to")
	to = input()
	prinasdt("Chain (IN/OUT)")
	chain = input()
	print()



def IP(addr):
	try:
		socket.inet_aton(addr)
		return True
	except socket.error:
		try:
			socket.inet_pton(socket.AF_INET6, addr)
			return True
		except socket.error:
			return False
def Port(port):
	try:
		int(port)
		return True
	except :
		return False


parser = argparse.ArgumentParser(prog='IPTables-CLI', description='Commad Line Iterface for IPTables-daemon')
parser.add_argument('-unixsocket', action='store', dest='socketfile',default="/var/run/IPTables-deamon",help='Path to IPTables-deamon Unixsocket file')
parser.add_argument('-DNAT', action='store_true', dest='DNAT',help='Adding a DNAT rule')
parser.add_argument('-SNAT', action='store_true', dest='SNAT',help='Adding a SNAT rule')
parser.add_argument('-LOG', action='store_true', dest='LOG',help='Adding a LOG rule')
parser.add_argument('-DROP', action='store_true', dest='DROP',help='Adding a DROP rule')
parser.add_argument('-REJECT', action='store_true', dest='REJECT',help='Adding a REJECT rule')
parser.add_argument('-dip', action='store', dest='dip',default="NONE",help='Filter package by destination IP')
parser.add_argument('-dport', action='store', dest='dport',default="NONE",help='Filter package by destination Port')
parser.add_argument('-to', action='store', dest='to',default="NONE",help='Rewrites destination IP of filtered package')
parser.add_argument('-to-port', action='store', dest='to',default="NONE",help='Rewrites destination Port of filtered package')
parser.add_argument('-OUT', action='store_const', dest='chain',const="OUT",help='Filters outgoing traffic')
parser.add_argument('-IN', action='store_const', dest='chain',const="IN",help='Filters ingoing traffic')
parser.add_argument('--wizard', action='store_true', dest='cli',help='Setup wirad for IP rules')
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
results = parser.parse_args()
if results.cli:
	wizard()
else:
	if (results.dip != "NONE" or results.dport != "NONE"):
		if(results.dip == "NONE"):
			if (Port(results.dport)):
				if(IP(results.to)):
					print(results)
				elif(results.to == "NONE"):
					print("Missing ")
			else:
				if(results.dport == "NONE"):
					print("No dip and dport")
				else:
					print(results.dport + " is not a vaild Port")
		elif (results.dport == "NONE"):
			if (IP(results.dip)):
				print(results)
			else:
				if(results.dip == "NONE"):
					print("No dip and dport")
				elif(Port(results.dport)):
					print(results.dip + " is not a vaild IP")
				else:
					print(results.dip + ":" +results.dport + " is not vaild")
		elif (results.dip != "NONE" and results.dport != "NONE"):
			if(IP(results.dip)):
				if(Port(results.dport)):
					print(results)
					print(IP(results.to))
				else:
					print(results.dport + " is not a valid Port")
			elif(Port(results.dport)):
				print(results.dip + " is not a Valid IP")
			else:
				print(results.dip + ":" + results.dport + " is not vaild")
