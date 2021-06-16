class BuildObjectQuantitativeAttribute:
    def buildType(self, namespace):
        try:
            result = namespace["label"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildtype")
            return None

    def buildUnits(self, namespace):
        try:
            result = namespace["units"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildunits")
            return None

    def buildValue(self, namespace):
        try:
            result = namespace["value"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildvalue")
            return None
