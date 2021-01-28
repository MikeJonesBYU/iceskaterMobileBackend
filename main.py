import json
from types import SimpleNamespace
from Model.Session import Session
from tools.analyzer import Analyzer
import pickle
import math
import warnings
import file_data

jump_types = {
    0: "axel",
    1: "toe",
    2: "flip",
    3: "lutz",
    4: "loop",
    5: "sal",
    6: "half-loop",
    7: "waltz"
}

total_jump_count = 0
total_correct_count = 0

# change these values to change the tests being run
margin = 0
test_files = file_data.files_104
test_file_path = "test_files/json_sessions_104/"

def main():

    warnings.filterwarnings("ignore")
    print("")
    # Tests can be run all at once, or one at a time.
    run_all_tests()
    # run_test("cnp_22")


# Runs the given file through the classifier
def run_test(file_name):

    global margin
    global total_jump_count
    global total_correct_count
    global test_files
    global test_file_path

    with open(test_file_path + file_name + ".txt", 'r') as file:

        # Open file and extract readings from session object
        data = file.read()
        session = Session(json.loads(data, object_hook=lambda d: SimpleNamespace(**d)))
        session.buildObject()
        readings = session.sensors.get(next(iter(session.sensors))).get_readings()

        # Open classifier
        clf = None
        with open("RF_new.pkl", 'rb') as f:
            clf = pickle.load(f)
            f.close()

        jump_count = 0
        correct_count = 0;
        print(file_name + ": ")

        # Pass each jump in session through the classifier
        for event_index in range(len(session.get_events())):

            event = session.get_events()[event_index]
            start_index = 0
            end_index = 0

            # find the correct indices for the start and end of the jump
            for reading_index in range(len(readings)):
                if readings[reading_index].timestamp == event.startTime:
                    start_index = reading_index
                if readings[reading_index].timestamp == event.endTime:
                    end_index = reading_index

            # pass all readings between start and end indices to the classifier (with optional margin)
            reading_subset = readings[start_index - margin:end_index + margin]
            tool = Analyzer()
            input = tool.preprocess_type(reading_subset)

            jump_count = jump_count + 1
            total_jump_count = total_jump_count + 1

            # format and print output
            clf_pred = math.trunc(clf.predict(input)[0])
            jump_type = jump_types.get(clf_pred)
            formatted_jump_type = "{0:>5}".format(jump_type)
            correct_pred = test_files.get(file_name).get("jumps").get(event_index)
            print(" " + str(jump_count) + ": " + formatted_jump_type + " | correct: " + str(correct_pred))

            if jump_type == correct_pred:
                correct_count = correct_count + 1
                total_correct_count = total_correct_count + 1

        print("Correct: " + str(correct_count) + "/" + str(len(session.get_events())))
        print("")

# run each test in file_data.py
def run_all_tests():
    global total_jump_count
    global total_correct_count
    global test_files

    for file_name in test_files:
        run_test(file_name)

    print("")
    print("Total: " + str(total_correct_count) + "/" + str(total_jump_count))
    print("")

if __name__ == '__main__':
    main()