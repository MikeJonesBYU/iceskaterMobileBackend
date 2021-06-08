import inspect

from Model.Event import Event
from Model.Sensor import Sensor


class BuildObjectSession:

    def buildSessionID(self, namespace):
        print("type of namespace in buildobjectsession:")
        print(type(namespace))
        try:
            result = namespace["sessionID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sessionid")
            return None

    def buildAthleteID(self, namespace):
        try:
            result = namespace["athleteID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sess athlete")
            return None

    def buildSport(self, namespace):
        try:
            result = namespace["sport"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sport")
            return None

    def buildStartTime(self, namespace):
        try:
            result = namespace["startTime"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sess start")
            return None

    def buildEndTime(self, namespace):
        try:
            result = namespace["endTime"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN session endtime")
            return None

    def buildStatus(self, namespace):
        try:
            result = namespace["status"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN status")
            return None

    def buildDeviceID(self, namespace):
        try:
            result = namespace["deviceID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN deviceid")
            return None

    def buildSensors(self, namespace):
        print("building sensors")
        try:
            x = namespace["sensors"]
            # list = self.purgeMethods(inspect.getmembers(x))
            result = {}
            for key, value in x.items():
                # name = a[0]
                sensor = Sensor(value)
                sensor.buildObject()
                result[key] = sensor
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sensors")
            return None
#---------------------------------------fixme: subevents & qualities missing
    def buildEvents(self, namespace):
        try:
            x = namespace["events"]
            result = {}

            for key, value in x.items():
                event = Event(value)
                event.buildObject()
                result[key] = event
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN events")
            return None
