from BuildObjectHelpers.BuildObjectSensor import BuildObjectSensor as extractor

class Sensor:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.sensorID = None
        self.sensorLocation = None
        self.connectionStatus = None
        self.readings = None


    def buildObject(self):
        self.sensorID = extractor.buildSensorID(self, self.namespaceObj)
        self.sensorLocation = extractor.buildSensorLocation(self, self.namespaceObj)
        self.connectionStatus = extractor.buildConnectionStatus(self, self.namespaceObj)
        self.readings = extractor.buildReadings(self, self.namespaceObj)

    def get_sensorID(self):
        return self.sensorID

    def get_sensorLocation(self):
        return self.sensorLocation

    def get_connectionStatus(self):
        return self.connectionStatus

    def get_readings(self):
        list = []
        result = []
        for key in self.readings.keys():
            list.append(key)
            # list.append(self.readings.get(key).get_timestamp())
        sorted(list)
        for val in list:
            result.append(self.readings.get(val))
        return result

    def purgeMethods(self, list):
        new_list = []
        for el in list:
            name = el[0]
            if not "__" in name:
                new_list.append(el)
        return new_list
