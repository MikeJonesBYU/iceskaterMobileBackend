from BuildObjectReading import BuildObjectReading as extractor
class Reading:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.timestamp = None
        self.sensorID = None
        self.magnetometerReading = None
        self.gyroscopeReading = None
        self.accelerometerReading = None
        self.logTag = None
        self.sessionIndex = None

    def buildObject(self):
        self.timestamp = extractor.buildTimestamp(self, self.namespaceObj)
        self.sensorID = extractor.buildSensorID(self, self.namespaceObj)
        self.magnetometerReading = extractor.buildMagnetometerReading(self, self.namespaceObj)
        self.gyroscopeReading = extractor.buildGyroscopeReading(self, self.namespaceObj)
        self.accelerometerReading = extractor.buildAccelerometerReading(self, self.namespaceObj)
        self.logTag = extractor.buildlogTag(self, self.namespaceObj)
        self.sessionIndex = extractor.buildSessionIndex(self, self.namespaceObj)


    def get_timestamp(self):
        return self.timestamp

    def get_sensorID(self):
        return self.sensorID

    def get_magnetometerReading(self):
        return self.magnetometerReading

    def get_gyroscopeReading(self):
        return self.gyroscopeReading

    def get_accelerometerReading(self):
        return self.accelerometerReading

    def get_logTag(self):
        return self.logTag

    def get_sessionIndex(self):
        return self.sessionIndex