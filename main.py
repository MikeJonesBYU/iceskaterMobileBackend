import json
import os
from types import SimpleNamespace
from orion.tools import augment_with_window_size
from Model.Session import Session
import pickle
import pandas as pd


def main():
    print("Run test_createTest.py not main()")

def createTest(filename, beginning, end, expected):
    folder = "Test_Files/"
    with open(folder + filename, 'r') as file:
        data = file.read()
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        session = Session(x)
        session.buildObject()
        key = next(iter(session.sensors))
        sensor = session.sensors.get(key)
        readings = sensor.get_readings()

        readings = readings[beginning:end]
        test_df = pd.DataFrame(create_dataframe_list(readings))
        test_df.columns = ["Accelerometer X", "Accelerometer Y", "Accelerometer Z", "Gyroscope X", "Gyroscope Y", "Gyroscope Z", "Magnetometer X", "Magnetometer Y", "Magnetometer Z"]
        result_miki, desired_rows = augment_with_window_size(test_df, 150, 5, True, True, "max", None)

        clf = None
        with open("RF_new.pkl", 'rb') as f:
            clf = pickle.load(f)
            f.close()
        prediction = clf.predict([desired_rows])
        pred = int(prediction[0])
        if pred == expected:
            print("Prediction for " + filename + " is Correct")
        else:
            print("Prediction for " + filename + " is incorrect")
            print("Expected: " + str(expected))
            print("Actual: " + str(pred))
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

if __name__ == '__main__':
    main()
