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
        # No sensorlocation in json as of 6/2/2021
        # self.sensorLocation = extractor.buildSensorLocation(self, self.namespaceObj)

        # No connectionstatus, there is a "status" in the json but it's on the top level
        # self.connectionStatus = extractor.buildConnectionStatus(self, self.namespaceObj)
        self.readings = extractor.buildReadings(self, self.namespaceObj)

    def get_sensorID(self):
        return self.sensorID

    def get_sensorLocation(self):
        return self.sensorLocation

    def get_connectionStatus(self):
        return self.connectionStatus

    # TODO: Does this happen every time get reading is called? Couldn't it be stored somewhere?
    def get_readings(self):
        list = []
        result = []
        for key in self.readings.keys():
            list.append(key)
            # list.append(self.readings.get(key).get_timestamp())
        list.sort(key=int)
        for val in list:
            result.append(self.readings.get(val))
        return result
