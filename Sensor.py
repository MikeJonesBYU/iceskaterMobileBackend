from BuildObjectSensor import BuildObjectSensor as extractor

class Sensor:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.sensorID = None
        self.sensorLocation = None
        self.connectionStatus = None


    def buildObject(self):
        self.sensorID = extractor.buildSensorID(self, self.namespaceObj)
        self.sensorLocation = extractor.buildSensorLocation(self, self.namespaceObj)
        self.connectionStatus = extractor.buildConnectionStatus(self, self.namespaceObj)




    def get_sensorID(self):
        return self.sensorID

    def get_sensorLocation(self):
        return self.sensorLocation

    def get_connectionStatus(self):
        return self.connectionStatus
