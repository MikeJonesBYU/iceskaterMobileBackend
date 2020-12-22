from BuildObjectSubEvent import BuildObjectSubEvent as extractor

class SubEvent:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.type = None
        self.value = None

    def buildObject(self):
        self.type = extractor.buildType(self, self.namespaceObj)
        self.value = extractor.buildValue(self, self.namespaceObj)


    def get_type(self):
        return self.type

    def get_value(self):
        return self.value