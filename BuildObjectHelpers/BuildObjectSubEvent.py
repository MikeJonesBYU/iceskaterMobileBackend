class BuildObjectSubEvent:

    def buildType(self, namespace):
        try:
            result = namespace["type"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN subeventtype")
            return None

    def buildValue(self, namespace):
        try:
            result = namespace["value"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN subeventvalue")
            return None