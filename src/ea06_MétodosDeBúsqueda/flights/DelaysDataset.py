

import csv
from DelayRecord import DelayRecord


def readCSV(filename):
    """Reads a CSV of flight delays and returns a list of DelayRecord"""
    with open(filename, 'r') as fh:
        reader = csv.reader(fh, delimiter=',', quotechar='"')
        # Discard first line
        next(reader)
        # Read the rest of the lines
        return [DelayRecord(*rec) for rec in reader]
    

if __name__=="__main__":
    records = readCSV('/home/jmlon/tmp/Datasets/548634059_T_ONTIME_REPORTING.csv')

    print(len(records))
    
