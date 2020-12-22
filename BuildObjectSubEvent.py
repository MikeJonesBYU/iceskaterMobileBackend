class BuildObjectSubEvent:

    def buildType(self, namespace):
        try:
            result = namespace.type
            return result
        except AttributeError:
            return None

    def buildValue(self, namespace):
        try:
            result = namespace.value
            return result
        except AttributeError:
            return None