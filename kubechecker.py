import os
import subprocess
import platform
import time

def clearScreen():
	mySystem = platform.system()
	if mySystem == "Windows":
		os.system('cls')
	else:
		os.system('clear')

clearScreen()

print("Loop checking mode: ")
print("1. Loop check")
print("2. Other mode")
loopCheckMode = input("Chosen option: ")
SLEEP_TIME = 5

if loopCheckMode == "1":
	while True:
		print("Refreshing kube list")
		result = subprocess.run(["kubectl","get","pods","-n","xom-logistics-dev"],stdout=subprocess.PIPE)
		lines = result.stdout.splitlines()
		index = 0
		options = []
		for byteLine in lines:
			if index == 0:
				index = index + 1
				continue
			line = byteLine.decode("utf-8")
			options.append(line)
		index = 1
		for option in options:
			print(str(index) + ") "  + option)
			index = index + 1
		time.sleep(SLEEP_TIME)
		clearScreen()


print("Gathering pods list...")
result = subprocess.run(["kubectl","get","pods","-n","xom-logistics-dev"],stdout=subprocess.PIPE)
lines = result.stdout.splitlines()
index = 0
options = []
for byteLine in lines:
	if index == 0:
		index = index + 1
		continue
	line = byteLine.decode("utf-8")
	lineSplit = line.split(" ")
	options.append(lineSplit[0])

print("Choose the pod you want to observe:")
index = 1
for option in options:
	print(str(index) + ") "  + option)
	index = index + 1

answer = input("Chosen option: ")
chosenAnswer = int(answer) - 1

print("Available mode: ")
print("1. Logs")
print("2. Describe")
mode = input("Chosen mode: ")
chosenMode = int(mode)

if chosenMode == 1:
	print("Gathering log of the pod " + options[chosenAnswer])
	osArgs = "kubectl logs -f " + options[chosenAnswer] + " -n xom-logistics-dev"
	os.system(osArgs)
elif chosenMode == 2:
	print("Gathering describe of the pod " + options[chosenAnswer])
	osArgs = "kubectl describe pod " + options[chosenAnswer] + " -n xom-logistics-dev"
	os.system(osArgs)