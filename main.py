import json
from types import SimpleNamespace
from Model.Session import Session
from tools.analyzer import Analyzer as tool, Analyzer
import pickle
from sklearn.ensemble import RandomForestClassifier
import sklearn.ensemble._forest
import pandas as pd
import numpy as np
def main():
    with open('example_cnp_05.txt', 'r') as file:
        data = file.read()
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        session = Session(x)
        session.buildObject()
        print("Done")
        clf = None
        with open("RF_new.pkl", 'rb') as f:
            clf = pickle.load(f)
            f.close()
        key = next(iter(session.sensors))
        sensor = session.sensors.get(key)
        readings = sensor.get_readings()
        readings = readings[4100:4300]
        #Jump Types:
        #"axel" = 0;
        #"toe" = 1;
        #"flip" = 2;
        #"lutz" = 3;
        #"loop" = 4;
        #"sal" = 5;
        #"half-loop" = 6;
        #"waltz" = 7;
        #print(readings[0].get_magnetometerReading().get_x())
        tool = Analyzer()
        input = tool.preprocess_type(readings)
        # for reading in input:
        #     print(reading)
        print(clf.predict(input))
        # print(session.get_sessionID())
        # print(session.get_athleteID())
        # print(session.get_sport())
        # print(session.get_startTime())
        # print(session.get_endTime())
        # print(session.get_status())
        # print(session.get_deviceID())
        # print(session.get_sensors())
        # for a in inspect.getmembers(x):
        #     print(a)


if __name__ == '__main__':
    main()