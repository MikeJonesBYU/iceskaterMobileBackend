import inspect
from Model.Reading import Reading
class BuildObjectSensor:

    def buildSensorID(self, namespace):
        try:
            result = namespace["sensorID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sensor sensorid")
            return None

    def buildSensorLocation(self, namespace):
        try:
            result = namespace["sensorLocation"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN sensorlocation")
            return None

    def buildConnectionStatus(self, namespace):
        try:
            result = namespace["connectionStatus"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN connection")
            return None

    def buildReadings(self, namespace):
        try:
            x = namespace["readings"]
            # list = self.purgeMethods(inspect.getmembers(x))
            result = {}
            for key, value in x.items():
                # key = a[0]
                reading = Reading(value)
                reading.buildObject()
                result[key] = reading
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildreadings")
            return None
