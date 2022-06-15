import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from orion.tools import gather_rows_by_sampling


def classify_skating(reading_dict, events, test_df):
    print("opening classifier")
    with open("classifiers/skating.pkl", 'rb') as f:
        clf = pickle.load(f)
        f.close()

    print("successfully unpickled the classifier")

    pred = {}

    for id, event in events.items():
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
        garbage, augmented_row = gather_rows_by_sampling(middle_index, center_of_jump, test_df, 5, 150, True,
                                                         test_df.shape[0], "max")
        input_for_classifier = np.append(center_of_jump, augmented_row)

        prediction = clf.predict([input_for_classifier])
        print("got a prediction!")
        print(prediction)

        pred[id] = {"resultIndex": int(prediction[0])}

    return pred


def classify_volleyball(reading_dict, events, test_df):
    print("opening classifier")
    with open("classifiers/volleyball.pkl", 'rb') as f:
        clf = pickle.load(f)
        f.close()

    print("successfully unpickled the classifier")

    pred = {}

    # TODO: figure out how to do this for volleyball
    for id, event in events.items():
        start = event.get_startTime()
        end = event.get_endTime()
        middle_of_jump = (start + (end - start) // 2)

        middle_index = reading_dict[str(middle_of_jump)].get_sessionIndex()
        center_of_jump = test_df.loc[middle_index]

        garbage, augmented_row = gather_rows_by_sampling(middle_index, center_of_jump, test_df, 5, 150, True,
                                                         test_df.shape[0], "max")
        input_for_classifier = np.append(center_of_jump, augmented_row)

        prediction = clf.predict([input_for_classifier])
        print("got a prediction!")
        print(prediction)

        pred[id] = {"resultIndex": int(prediction[0])}

    return pred
