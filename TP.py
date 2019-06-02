import csv
import pylab
import numpy as np


# Turning Point Algorithm

# Read ECG Values from csv file

filename = "ecg_values.csv"

with open(filename, 'r') as csvfile:
    ecg_vals = csvfile.readlines()

csvfile.close()

# Initializations 

ecg_vals = [float(x) for x in ecg_vals]

i = 0
V = list()
V2 = list()

ecg_vals_len = len(ecg_vals)

def store(x):
    """Store the passed value"""
    V.append(x)
    V2.append(x)
    
while i < ecg_vals_len - 2:
    X0 = ecg_vals[i]
    X1 = ecg_vals[i+1]
    X2 = ecg_vals[i+2]
    s1 = X1 - X0
    s2 = X2 - X1
    if ((s1 * s2) < 0):
        store(X1)
        i += 1
    else:
        store(X2)
        V2.append(X1)
        i += 2

# Plot ECG waveforms

ecg = []
with open('ecg_values.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        ecg.append(float(row[0]))

csvFile.close()

ecg_final = np.array(ecg, dtype=np.float32)

TPCSV = 'TP_vals.csv'
file = open(TPCSV, 'w', newline='')
writer = csv.writer(file)
writer.writerows(map(lambda x: [x], V))
file.close()

TPEcg = []
with open('TP_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        TPEcg.append(float(row[0]))
csvFile.close()

ecg_TP = np.array(TPEcg, dtype=np.float32)

# extra csv file with appended zeroes

# append last two values
V2.append(ecg_final[-1])
V2.append(ecg_final[-2])

TPCSV = 'TP_vals1.csv'
file = open(TPCSV, 'w', newline='')
writer = csv.writer(file)
writer.writerows(map(lambda x: [x], V2))
file.close()

TPEcg1 = []
with open('TP_vals1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        TPEcg1.append(float(row[0]))
csvFile.close()

ecg_TP1 = np.array(TPEcg1, dtype=np.float32)


hspace = .5
pylab.subplots_adjust(hspace=hspace)
pylab.subplot(2, 1, 1)
pylab.plot(ecg_final)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('Original ECG signal')

pylab.subplot(2, 1, 2)
pylab.plot(ecg_TP)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('ECG After TP Compression')

pylab.show()