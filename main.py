import json
import sys
import pandas as pd
from Model.Session import Session
from classify import *


def handler(event, context):

    # event is {athleteID:..., end_time:..., events:..., sensors:..., etc.}
    # event is already type dict so no need to json.loads

    session = Session(event)
    session.buildObject()
    print("done building session")

    sensors = session.get_sensors()
    print(sensors)
    print(type(sensors))
    key = next(iter(session.get_sensors()))  # next(iter(session.sensors))
    print("key:")
    print(key)
    sensor = session.sensors.get(key)
    readings = sensor.get_readings()
    print("got readings")
    print(type(readings))
    print(len(readings))
    # print("example reading timestamps:")
    # print(readings[0].get_timestamp())
    # print(readings[1].get_timestamp())
    # print(readings[2].get_timestamp())
    # print(readings[3].get_timestamp())

    # readings = readings[beginning:end]
    test_df = pd.DataFrame(create_dataframe_list(readings))
    test_df.columns = ["Accelerometer X", "Accelerometer Y", "Accelerometer Z", "Gyroscope X", "Gyroscope Y",
                       "Gyroscope Z", "Magnetometer X", "Magnetometer Y", "Magnetometer Z"]
    # find center of jump

    reading_dict = sensor.readings
    events = session.get_events()
    sport = session.sport

    if sport == "SKATING":
        pred = classify_skating(reading_dict, events, test_df)
    elif sport == "VOLLEYBALL":
        pred = classify_volleyball(reading_dict, events, test_df)
    else:
        pred = None

    return {"classificationResults": pred}


def create_dataframe_list(readings):
    df_list = []
    for reading in readings:
        innerList = [reading.get_accelerometerReading().x, reading.get_accelerometerReading().y,
                     reading.get_accelerometerReading().z, reading.get_gyroscopeReading().x,
                     reading.get_gyroscopeReading().y, reading.get_gyroscopeReading().z,
                     reading.get_magnetometerReading().x, reading.get_magnetometerReading().y,
                     reading.get_magnetometerReading().z]
        df_list.append(innerList)
    return df_list


if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        e = json.load(f)

    handler(e)