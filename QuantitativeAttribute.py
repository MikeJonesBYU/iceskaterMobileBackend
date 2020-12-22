from BuildObjectQuantitativeAttribute import BuildObjectQuantitativeAttribute as extractor

class QuantitativeAttribute:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.type = None
        self.units = None
        self.value = None

    def buildObject(self):
        self.type = extractor.buildType(self, self.namespaceObj)
        self.units = extractor.buildUnits(self, self.namespaceObj)
        self.value = extractor.buildValue(self, self.namespaceObj)


    def get_type(self):
        return self.type

    def get_units(self):
        return self.units

    def get_value(self):
        return self.value