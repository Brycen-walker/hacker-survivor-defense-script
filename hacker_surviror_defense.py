import time
import os


while True:
	time.sleep(0.1)
	os.system("who -u | tr -s \" \" | grep -v \"tty7\" | awk \'{print $6}\' > pids.txt")
	os.system("who -u | tr -s \" \" | grep -v \"tty7\" | awk \'{print $7}\' | sed \"s/(//g\" | sed \"s/)//g\" > ips.txt")

	with open("pids.txt", "r") as file:
		pids = file.read().split("\n")
	with open("ips.txt", "r") as file:
		ips = file.read().split("\n")
	pids = pids[:-1]
	ips = ips[:-1]
	for i in pids:
		num = 0
		os.system(f"kill {pids[num]}")
		print(f"killed {ips[num]}")
		os.system(f"sshpass -p student ssh -t -o 'StrictHostKeyChecking=no' student@{ips[num]} 'echo student | sudo -S poweroff'")
		num += 1

	os.system("rm pids.txt; rm ips.txt")
