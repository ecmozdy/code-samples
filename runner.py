import subprocess, os
import sys

directory = 'runnerfiles'
for filename in os.listdir(directory):
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'tcp','-w','runnertcp/'+filename])
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'udp','-w','runnerudp/'+filename])


#sys.stdout = open('netflowoutput', 'w')
second_directory = 'runnertcp'
for filename in os.listdir(second_directory):
	subprocess.call(['softflowd','-n','localhost:9995','-r',directory + '/' + filename])
	subprocess.call(['nfcapd','-l','/var/cache/nfdump','-p','9995']) #-D maybe? Daemon mode
	subprocess.call(['nfdump','-r','/var/cache/nfdump','-o','extended','-o','csv']) #'-r','/var/cache/nfdump']) --> reading from file
									#-q removes headers and summary