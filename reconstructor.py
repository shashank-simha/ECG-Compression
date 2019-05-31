import pylab
import scipy.signal as signal
import numpy 
import csv

ecg = []
with open('ecg_values.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        ecg.append(float(row[0]))

csvFile.close()

ecg_final = numpy.array(ecg, dtype=numpy.float32)

pylab.plot(ecg_final)
pylab.xlabel('Sample number')
pylab.ylabel('bit value')
pylab.title('Reconstructed ECG')
pylab.show()

