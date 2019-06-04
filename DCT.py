import csv
import pylab
import numpy as np
import math


# DCT Algorithm

# Read ECG Values from csv file

filename = "ecg_values.csv"

with open(filename, 'r') as csvfile:
    ecg_vals = csvfile.readlines()

csvfile.close()

# Initializations | DCT

ecg_vals = [float(x) for x in ecg_vals]
V = list()
V2 = list()
# DCT algo
for i in range(len(ecg_vals)-1):
    sum = 0
    s = 1
    if (i == 0):
        s = math.sqrt(0.5) 
    for j in range(len(ecg_vals)-1):
        sum += s * ecg_vals[i] * math.cos((math.pi/len(ecg_vals)) * (j + 5) * i)
    V.append(sum * math.sqrt(2/len(ecg_vals)))
    V2.append((2/(len(ecg_vals)-1)) * (sum * math.sqrt(2/len(ecg_vals))))


# Plot ECG waveforms
ecg = []
with open('ecg_values.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        ecg.append(float(row[0]))

csvFile.close()

ecg_final = np.array(ecg, dtype=np.float32)

DCTCSV = 'DCT_vals.csv'
file = open(DCTCSV, 'w', newline='')
writer = csv.writer(file)
writer.writerows(map(lambda x: [x], V))
file.close()

DCTEcg = []
with open('DCT_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        DCTEcg.append(float(row[0]))
csvFile.close()

ecg_DCT = np.array(DCTEcg, dtype=np.float32)

hspace = .5
pylab.subplots_adjust(hspace=hspace)
pylab.subplot(2, 1, 1)
pylab.plot(ecg_final)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('Original ECG signal')

pylab.subplot(2, 1, 2)
pylab.plot(ecg_DCT)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('ECG After DCT Compression')

pylab.show()