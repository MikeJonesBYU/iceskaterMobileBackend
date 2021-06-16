import json
import os
from types import SimpleNamespace
from orion.tools import augment_with_window_size
from orion.tools import gather_rows_by_sampling
from Model.Session import Session
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sklearn


def handler(event, context):

    # event is {athleteID:..., endtime:..., events:..., sensors:..., etc.}
    # event is already type dict so no need to json.loads

    x = event #json.loads(event, object_hook=lambda d: SimpleNamespace(**d))
    session = Session(x)
    session.buildObject()
    print("done building session")

    sensors = session.get_sensors()
    print(sensors)
    print(type(sensors))
    key = next(iter(session.get_sensors())) #next(iter(session.sensors))
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
    test_df.columns = ["Accelerometer X", "Accelerometer Y", "Accelerometer Z", "Gyroscope X", "Gyroscope Y", "Gyroscope Z", "Magnetometer X", "Magnetometer Y", "Magnetometer Z"]
    # find center of jump

    pred = {}

    print("opening classifier")
    clf = None
    with open("RF_new.pkl", 'rb') as f:
        clf = pickle.load(f)
        f.close()

    print("successfully unpickled the classifier")

    reading_dict = sensor.readings

    for id, event in session.get_events().items():
        print("event id:")
        print(id)
        start = event.get_startTime()
        end = event.get_endTime()
        middle_of_jump = (start + (end-start)//2)

        print("start, end, middle:")
        print(start)
        print(end)
        print(middle_of_jump)

        found_middle = False

        for i in range(-5, 5):
            if str(middle_of_jump + i) in reading_dict.keys():
                middle_of_jump = middle_of_jump + i
                print("found actual middle:")
                print(middle_of_jump)
                found_middle = True
                break

        middle_index = reading_dict[str(middle_of_jump)].get_sessionIndex()
        print("middle index:")
        print(middle_index)

        # TODO: what if we can't find a timestamp?
        if not found_middle:
            raise ValueError("can't find middle of jump timestamp")

        center_of_jump = test_df.loc[middle_index]
        garbage, augmented_row = gather_rows_by_sampling(middle_index, center_of_jump, test_df, 5, 150, True, test_df.shape[0], "max")
        input_for_classifier = np.append(center_of_jump, augmented_row)

        prediction = clf.predict([input_for_classifier])
        print("got a prediction!")
        print(prediction)

        pred[id] = int(prediction[0])

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
