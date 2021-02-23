class MagnetometerReading:
    def __init__(self, namespaceObj):
        self.x = namespaceObj.x
        self.y = namespaceObj.y
        self.z = namespaceObj.z

    # def __init__(self, x, y, z):
    #     self.x = x
    #     self.y = y
    #     self.z = z


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


