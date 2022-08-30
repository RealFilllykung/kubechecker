import os
import subprocess

os.system('clear')
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

answer = input("Choosen option: ")
chosenAnswer = int(answer) - 1

osArgs = "kubectl logs -f " + options[chosenAnswer] + " -n xom-logistics-dev"
os.system(osArgs)
