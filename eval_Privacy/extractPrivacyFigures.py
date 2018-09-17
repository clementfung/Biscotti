import os

directory = "../DistSys/LogFiles"
privacyResultsFile = "results.csv"

totalUnmaskedUpdates = 0
privProb = 0

results = open(privacyResultsFile, "a+")


for filename in os.listdir(directory):
  
	if filename.startswith("test1"): 
    	
		print filename

		with open(directory+"/"+filename, 'r') as clientFile:
			thisLine = clientFile.readline()
			values = [s for s in thisLine.split()]
			print values
			if(len(values) > 0):
				totalUnmaskedUpdates = totalUnmaskedUpdates + int(values[0])			
				totalUpdates = int(values[1])
				privProb = float(values[2])

			print values
	
print totalUnmaskedUpdates

maskingProb = (totalUnmaskedUpdates*1.0)/(totalUpdates*1.0)

lineToWrite = str(privProb) + "," + str(maskingProb)+"\n"

results.write(lineToWrite)