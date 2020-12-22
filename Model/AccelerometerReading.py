class AccelerometerReading:
    def __init__(self, namespaceObj):
        self.x = namespaceObj.x
        self.y = namespaceObj.y
        self.z = namespaceObj.z


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

