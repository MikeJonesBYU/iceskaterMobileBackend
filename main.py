import json
from types import SimpleNamespace
from Session import Session
import inspect

def main():
    with open('example_session.txt', 'r') as file:
        data = file.read()
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        session = Session(x)
        session.buildObject()
        print(session.get_sessionID())
        print(session.get_athleteID())
        print(session.get_sport())
        print(session.get_startTime())
        print(session.get_endTime())
        # for a in inspect.getmembers(x):
        #     print(a)












if __name__ == '__main__':
    main()