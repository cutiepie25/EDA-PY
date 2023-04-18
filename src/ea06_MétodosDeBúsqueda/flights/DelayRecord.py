
# class describing a DelayRecord with the following fields:
# YEAR	FL_DATE	OP_UNIQUE_CARRIER	OP_CARRIER_AIRLINE_ID	OP_CARRIER_FL_NUM	ORIGIN_AIRPORT_ID	ORIGIN	ORIGIN_CITY_NAME	ORIGIN_STATE_ABR	DEST_AIRPORT_ID	DEST	DEST_CITY_NAME	DEST_STATE_ABR	DEP_DELAY_NEW	ARR_DELAY	ARR_DELAY_NEW	CARRIER_DELAY	WEATHER_DELAY	NAS_DELAY	SECURITY_DELAY	LATE_AIRCRAFT_DELAY

import csv
from datetime import datetime


class DelayRecord:
    """Class describing a DelayRecord with the following fields:
    YEAR	FL_DATE	OP_UNIQUE_CARRIER	OP_CARRIER_AIRLINE_ID	OP_CARRIER_FL_NUM	ORIGIN_AIRPORT_ID	ORIGIN	ORIGIN_CITY_NAME	ORIGIN_STATE_ABR	DEST_AIRPORT_ID	DEST	DEST_CITY_NAME	DEST_STATE_ABR	DEP_DELAY_NEW	ARR_DELAY	ARR_DELAY_NEW	CARRIER_DELAY	WEATHER_DELAY	NAS_DELAY	SECURITY_DELAY	LATE_AIRCRAFT_DELAY
    """

    def __init__(self, year, fl_date, op_unique_carrier, op_carrier_airline_id, op_carrier_fl_num, origin_airport_id, origin, origin_city_name, origin_state_abr, dest_airport_id, dest, dest_city_name, dest_state_abr, dep_delay_new, arr_delay, arr_delay_new, carrier_delay, weather_delay, nas_delay, security_delay, late_aircraft_delay):
        self.year = int(year)
        self.fl_date = datetime.strptime(fl_date, '%Y-%m-%d').date() 
        self.op_unique_carrier = op_unique_carrier
        self.op_carrier_airline_id = int(op_carrier_airline_id)
        self.op_carrier_fl_num = int(op_carrier_fl_num)
        self.origin_airport_id = int(origin_airport_id)
        self.origin = origin
        self.origin_city_name = origin_city_name
        self.origin_state_abr = origin_state_abr
        self.dest_airport_id = int(dest_airport_id)
        self.dest = dest
        self.dest_city_name = dest_city_name
        self.dest_state_abr = dest_state_abr
        self.dep_delay_new = dep_delay_new
        self.arr_delay = arr_delay
        self.arr_delay_new = arr_delay_new
        self.carrier_delay = carrier_delay
        self.weather_delay = weather_delay
        self.nas_delay = nas_delay
        self.security_delay = security_delay
        self.late_aircraft_delay = late_aircraft_delay
    
    def __str__(self):
        return f"{self.year}, {self.fl_date}, {self.op_unique_carrier}, {self.op_carrier_airline_id}, {self.op_carrier_fl_num}, {self.origin_airport_id}, {self.origin}, {self.origin_city_name}, {self.origin_state_abr}, {self.dest_airport_id}, {self.dest}, {self.dest_city_name}, {self.dest_state_abr}, {self.dep_delay_new}, {self.arr_delay}, {self.arr_delay_new}, {self.carrier_delay}, {self.weather_delay}, {self.nas_delay}, {self.security_delay}, {self.late_aircraft_delay}"



def readCSV(filename: str) -> list:
    """Reads a CSV of flight delays and returns a list of DelayRecord"""
    with open(filename, 'r') as fh:
        reader = csv.reader(fh, delimiter=',', quotechar='"')
        # Discard first line
        next(reader)
        # Read the rest of the lines
        return [DelayRecord(*rec) for rec in reader]
    

# Example main function:
# Reads the dataset, prints the number of records and the first record
if __name__=="__main__":
    records = readCSV('/home/jmlon/tmp/Datasets/548634059_T_ONTIME_REPORTING.csv')
    print(len(records))
    print(records[0])

