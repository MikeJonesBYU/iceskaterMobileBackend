import inspect
from Reading import Reading
class BuildObjectSensor:

    def buildSensorID(self, namespace):
        try:
            result = namespace.sensorID
            return result
        except AttributeError:
            return None

    def buildSensorLocation(self, namespace):
        try:
            result = namespace.sensorLocation
            return result
        except AttributeError:
            return None

    def buildConnectionStatus(self, namespace):
        try:
            result = namespace.connectionStatus
            return result
        except AttributeError:
            return None

    def buildReadings(self, namespace):
        try:
            x = namespace.readings
            list = self.purgeMethods(inspect.getmembers(x))
            result = {}
            for a in list:
                key = a[0]
                value = Reading(a[1])
                value.buildObject()
                result[key] = value
            return result
        except AttributeError:
            return None
