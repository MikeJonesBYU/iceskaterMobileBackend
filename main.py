import json
from types import SimpleNamespace
from Model.Session import Session
from tools.analyzer import Analyzer as tool, Analyzer
import pickle
from sklearn.ensemble import RandomForestClassifier
import sklearn.ensemble._forest
import pandas as pd
import numpy as np

files = {
    "cnp_10": "cnp_10.txt",
    "cnp_12": "cnp_12.txt",
    "cnp_17": "cnp_17.txt",
    "cnp_21": "cnp_21.txt",
    "cnp_22": "cnp_22.txt",
    "cnp_24": "cnp_24.txt",
    "cnp_27": "cnp_27.txt",
    "cnp_28": "cnp_28.txt"

}

def main():

    # Tests can be run all at once, or one at a time.
    run_all_tests()
    run_test("cnp_22")


# Runs the given file through the classifier
def run_test(file_name):
    with open('test_files/json_sessions_104/' + files.get(file_name), 'r') as file:
        data = file.read()
        session = Session(json.loads(data, object_hook=lambda d: SimpleNamespace(**d)))
        session.buildObject()
        clf = None
        with open("RF_new.pkl", 'rb') as f:
            clf = pickle.load(f)
            f.close()
        readings = session.sensors.get(next(iter(session.sensors))).get_readings()
        jump_count = 0

        print(file_name + ": ")
        # For each event in the session, find the reading index of the event start and event end.
        # Pass all readings between those indices to the classifier.
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
        print("")


def run_all_tests():
    for file_name in files:
        run_test(file_name)



if __name__ == '__main__':
    main()