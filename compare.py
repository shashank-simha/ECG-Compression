import csv

original = []
aztec = []
TP = []
TP_with_zeros = []
cortes = []
cortes_with_zeros = []
DCT = []

with open('ecg_values.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        original.append(float(row[0]))
csvFile.close()

with open('aztec_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        aztec.append(float(row[0]))
csvFile.close()

with open('TP_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        TP.append(float(row[0]))
csvFile.close()

with open('TP_vals1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        TP_with_zeros.append(float(row[0]))
csvFile.close()


with open('DCT_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        DCT.append(float(row[0]))
csvFile.close()

TotalData = 0

for i in range(len(original)-1):
    TotalData += abs(original[i])



DataLoss_AZTEC = 0
CR_AZTEC = 0

for i in range(len(original)-1):
    """ Let 40% be the threshold, anything within + or - threshold shall be 
    considered as noise and removing than info will not account for data loss"""
    if(aztec[i]>(0.4*max(aztec)) or aztec[i]<(0.4*min(aztec))): 
        DataLoss_AZTEC += abs(original[i] - TP_with_zeros[i])

DataLoss_AZTEC = DataLoss_AZTEC/TotalData

CR_AZTEC = len(original)/len(aztec)


DataLoss_TP = 0
CR_TP = 0

for i in range(len(original)-1):
    """Let 40% be the threshold, anything within + or - threshold shall be 
    considered as noise and removing than info will not account for data loss"""
    if(TP_with_zeros[i]>(0.4*max(TP_with_zeros)) or TP_with_zeros[i]<(0.4*min(TP_with_zeros))): 
        DataLoss_TP += abs(original[i] - TP_with_zeros[i])

CR_TP = len(original)/len(TP)


DataLoss_DCT = 0
CR_DCT = 0

for i in range(len(original)-1):
    """Let 40% be the threshold, anything within + or - threshold shall be 
    considered as noise and removing than info will not account for data loss"""
    if(DCT[i]>(0.4*max(DCT)) or DCT[i]<(0.4*min(DCT))): 
        DataLoss_DCT += abs(original[i] - DCT[i])

CR_DCT = len(original)/len(DCT)

print("Comparision between AZTEC, TP and Cortes Algorithms")

print("\n\nAlgo \t\tAvg Data loss \t\tCompression ratio \tData Encryption \tRelevence to original data")

print("\n\nAztec \t\t"+str(DataLoss_AZTEC)+"\t"+str(CR_AZTEC)+"\tNot present"+"\t\tHigh")

print("\n\nTP \t\t"+str(DataLoss_TP)+"\t"+str(CR_TP)+"\tNot present"+"\t\tModerate")

print("\n\nDCT \t\t"+str(DataLoss_DCT)+"\t"+str(CR_DCT)+"\tPresent"+"\t\t\tLow")

