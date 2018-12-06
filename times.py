import pandas as pd

import read

data = read.load_data()

import dateutil

def extract_hour(timestamp):
    date_time = dateutil.parser.parse(timestamp)
    hour = date_time.hour
    return hour

if __name__ == "__main__":
    hours = data["submission_time"].apply(extract_hour)
    hour_counts = hours.value_counts()
    print(hour_counts)