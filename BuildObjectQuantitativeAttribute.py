class BuildObjectQuantitativeAttribute:
    def buildType(self, namespace):
        try:
            result = namespace.type
            return result
        except AttributeError:
            return None

    def buildUnits(self, namespace):
        try:
            result = namespace.units
            return result
        except AttributeError:
            return None

    def buildValue(self, namespace):
        try:
            result = namespace.value
            return result
        except AttributeError:
            return None
