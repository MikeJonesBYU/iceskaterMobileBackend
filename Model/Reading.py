from BuildObjectHelpers.BuildObjectReading import BuildObjectReading as extractor
class Reading:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.timestamp = None
        self.sensorID = None
        self.magnetometer = None
        self.gyroscope = None
        self.accelerometer = None
        self.logTag = None
        self.sessionIndex = None

    def buildObject(self):
        self.timestamp = extractor.buildTimestamp(self, self.namespaceObj)
        self.sensorID = extractor.buildSensorID(self, self.namespaceObj)
        self.magnetometer = extractor.buildMagnetometerReading(self, self.namespaceObj)
        self.gyroscope = extractor.buildGyroscopeReading(self, self.namespaceObj)
        self.accelerometer = extractor.buildAccelerometerReading(self, self.namespaceObj)
        self.logTag = extractor.buildlogTag(self, self.namespaceObj)
        self.sessionIndex = extractor.buildSessionIndex(self, self.namespaceObj)


    def get_timestamp(self):
        return self.timestamp

    def get_sensorID(self):
        return self.sensorID

    def get_magnetometerReading(self):
        return self.magnetometer

    def get_gyroscopeReading(self):
        return self.gyroscope

    def get_accelerometerReading(self):
        return self.accelerometer

    def get_logTag(self):
        return self.logTag

    def get_sessionIndex(self):
        return self.sessionIndex

    def __str__(self):
        printString = ""
        magString = "Magnetometer is: " + str(self.magnetometer.get_x()) + "\n" + str(self.magnetometer.get_y()) + "\n" + str(self.magnetometer.get_z()) + "\n"
        accString = "Accelerometer is: " + str(self.accelerometer.get_x()) + "\n" + str(self.accelerometer.get_y()) + "\n" + str(self.accelerometer.get_z()) + "\n"
        gyroString = "Gyroscope is: " + str(self.gyroscope.get_x()) + "\n" + str(self.gyroscope.get_y()) + "\n" + str(self.gyroscope.get_z()) + "\n"
        printString += magString
        printString += accString
        printString += gyroString
        return printString