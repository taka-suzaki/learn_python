import csv
import numpy as np
import pandas as pd

a = np.array([[1, 4, 2], [7, 9, 4], [0, 6, 2]])
b = np.array([1, 2, 3, 4, 5])


def writeCSV(data, path):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


# writer

writeCSV(a, 'data/csv/sample1.csv')
writeCSV(b, 'data/csv/sampleb1.csv')

# numpy
np.savetxt('data/csv/sample2.csv', a)

# pandas
df = pd.DataFrame(a)
df.to_csv('data/csv/sample3.csv')
