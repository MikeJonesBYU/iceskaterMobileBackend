import json
import os
from types import SimpleNamespace
from orion.tools import augment_with_window_size
from orion.tools import gather_rows_by_sampling
from Model.Session import Session
import pickle
import pandas as pd
import numpy as np


def handler(event, context):
    x = json.loads(event, object_hook=lambda d: SimpleNamespace(**d))
    session = Session(x)
    session.buildObject()
    key = next(iter(session.sensors))
    sensor = session.sensors.get(key)
    readings = sensor.get_readings()

    # readings = readings[beginning:end]
    test_df = pd.DataFrame(create_dataframe_list(readings))
    test_df.columns = ["Accelerometer X", "Accelerometer Y", "Accelerometer Z", "Gyroscope X", "Gyroscope Y", "Gyroscope Z", "Magnetometer X", "Magnetometer Y", "Magnetometer Z"]
    # find center of jump

    #middle_of_jump = (beginning + (end-beginning)//2)
    middle_of_jump = 100
    center_of_jump = test_df.loc[middle_of_jump]
    garbage, augmented_row = gather_rows_by_sampling(middle_of_jump, center_of_jump, test_df, 5, 150, True, test_df.shape[0], "max")
    input_for_classifier = np.append(center_of_jump, augmented_row)
    clf = None
    with open("RF_new.pkl", 'rb') as f:
        clf = pickle.load(f)
        f.close()
    prediction = clf.predict([input_for_classifier])
    pred = int(prediction[0])
    return pred

def create_dataframe_list(readings):
    list = []
    for reading in readings:
        innerList = []
        innerList.append(reading.get_accelerometerReading().x)
        innerList.append(reading.get_accelerometerReading().y)
        innerList.append(reading.get_accelerometerReading().z)
        innerList.append(reading.get_gyroscopeReading().x)
        innerList.append(reading.get_gyroscopeReading().y)
        innerList.append(reading.get_gyroscopeReading().z)
        innerList.append(reading.get_magnetometerReading().x)
        innerList.append(reading.get_magnetometerReading().y)
        innerList.append(reading.get_magnetometerReading().z)
        list.append(innerList)
    return list