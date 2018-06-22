import subprocess, os
import sys

directory = 'runnerfiles'
for filename in os.listdir(directory):
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'tcp','-w','runnertcp/'+filename])
	subprocess.call(['tcpdump','-r',directory + '/' + filename,'udp','-w','runnerudp/'+filename])