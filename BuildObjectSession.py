import inspect
from Sensor import Sensor

class BuildObjectSession:

    def buildSessionID(self, namespace):
        try:
            result = namespace.sessionID
            return result
        except AttributeError:
            return None

    def buildAthleteID(self, namespace):
        try:
            result = namespace.athleteID
            return result
        except AttributeError:
            return None

    def buildSport(self, namespace):
        try:
            result = namespace.sport
            return result
        except AttributeError:
            return None

    def buildStartTime(self, namespace):
        try:
            result = namespace.startTime
            return result
        except AttributeError:
            return None

    def buildEndTime(self, namespace):
        try:
            result = namespace.endTime
            return result
        except AttributeError:
            return None

    def buildStatus(self, namespace):
        try:
            result = namespace.status
            return result
        except AttributeError:
            return None

    def buildDeviceID(self, namespace):
        try:
            result = namespace.deviceID
            return result
        except AttributeError:
            return None

    def buildSensors(self, namespace):
        try:
            x = namespace.sensors
            list = self.purgeMethods(inspect.getmembers(x))
            result = {}
            for a in list:
                name = a[0]
                sensor = Sensor(a[1])
                sensor.buildObject()
                result[name] = sensor
            return result
        except AttributeError:
            return None

    def buildEvents(self, namespace):
        try:
            x = namespace.events
            list = self.purgeMethods(inspect.getmembers(x))
            result = {}
            for a in list:
                name = a[0]
                #sensor = Sensor(a[1])
                sensor.buildObject()
                result[name] = sensor
            return result
        except AttributeError:
            return None
