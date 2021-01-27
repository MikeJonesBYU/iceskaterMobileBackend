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
    with open('test_files/json_sessions_104/cnp_24_json_session.txt', 'r') as file:
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

        # readings = readings[9152:9231]
        print("")
        jump_count = 0
        for event_id in session.events:
            event = session.events.get(event_id)
            start_index = 0
            end_index = 0
            for reading_index in range(len(readings)):
                if readings[reading_index].timestamp == event.startTime:
                    start_index = reading_index
                if readings[reading_index].timestamp == event.endTime:
                    end_index = reading_index
            reading_subset = readings[start_index:end_index]
            tool = Analyzer()
            input = tool.preprocess_type(reading_subset)
            jump_count = jump_count + 1
            print("Jump " + str(jump_count) + ": " + str(clf.predict(input)))


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
        # tool = Analyzer()
        # input = tool.preprocess_type(readings)
        # for reading in input:
        #     print(reading)
        # print(clf.predict(input))
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