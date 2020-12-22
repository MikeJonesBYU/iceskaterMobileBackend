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
