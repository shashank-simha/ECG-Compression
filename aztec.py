import csv
import pylab
import scipy.signal as signal
import numpy 

filename = "ecg_values.csv"

with open(filename, 'r') as csvfile:
    ecg_vals = csvfile.readlines()

csvfile.close()

# Initializations

ecg_vals = [float(x) for x in ecg_vals]
Vth = sum(ecg_vals)/len(ecg_vals)
Ln = 0
V = list()
t = 0
ecg_vals_len = len(ecg_vals)
Vmax = Vmin = Vmax1 = Vmin1 = 0
Length = list()
flag = False


def store(v_max, v_min):
    V.append((v_max+v_min)/2)
    Length.append(Ln - 1)


while t < ecg_vals_len - 1:
    Vmax = Vmin = Vmax1 = Vmin1 = ecg_vals[t]
    while t < ecg_vals_len - 1:
        if Ln >= 50:
            store(Vmax, Vmin)
            Ln = 0
            break
        else:
            Ln += 1
            t += 1

            if ecg_vals[t] > Vmax:
                Vmax1 = ecg_vals[t]
            elif ecg_vals[t] < Vmin:
                Vmin1 = ecg_vals[t]

            if Vmax1 - Vmin1 > Vth:
                store(Vmax, Vmin)
                Ln = 0
                break
            else:
                Vmax = Vmax1
                Vmin = Vmin1

# print(V)

aztecCSV = 'aztec_vals.csv'
file = open(aztecCSV, 'w', newline='')
writer = csv.writer(file)
writer.writerows(map(lambda x: [x], V))
file.close()

ecg = []
with open('aztec_vals.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        ecg.append(float(row[0]))
csvFile.close()

ecg_final = numpy.array(ecg, dtype=numpy.float32)

pylab.plot(ecg_final)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('Aztec Compression ECG')
pylab.show()