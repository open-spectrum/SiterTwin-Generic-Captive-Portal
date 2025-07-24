from subprocess import run
from time import sleep
while True:
	run(['clear'])
	run(['arp' ,'-a'])
	sleep(1)
