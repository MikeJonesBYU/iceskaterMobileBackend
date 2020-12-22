from Model.MagnetometerReading import MagnetometerReading as Mag
from Model.GyroscopeReading import GyroscopeReading as Gyro
from Model.AccelerometerReading import AccelerometerReading as Accel

class BuildObjectReading:
    def buildTimestamp(self, namespace):
        try:
            result = namespace.timestamp
            return result
        except AttributeError:
            return None

    def buildSensorID(self, namespace):
        try:
            result = namespace.sensorID
            return result
        except AttributeError:
            return None

    def buildMagnetometerReading(self, namespace):
        try:
            x = namespace.magnetometerReading
            result = Mag(x)
            return result
        except AttributeError:
            return None

    def buildGyroscopeReading(self, namespace):
        try:
            x = namespace.gyroscopeReading
            result = Gyro(x)
            return result
        except AttributeError:
            return None

    def buildAccelerometerReading(self, namespace):
        try:
            x = namespace.accelerometerReading
            result = Accel(x)
            return result
        except AttributeError:
            return None

    def buildlogTag(self, namespace):
        try:
            result = namespace.logTag
            return result
        except AttributeError:
            return None

    def buildSessionIndex(self, namespace):
        try:
            result = namespace.sessionIndex
            return result
        except AttributeError:
            return None