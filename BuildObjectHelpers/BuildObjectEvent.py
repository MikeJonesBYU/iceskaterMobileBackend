import inspect

from Model.SubEvent import SubEvent
from Model.QuantitativeAttribute import QuantitativeAttribute

class BuildObjectEvent:

    def buildID(self, namespace):
        print("type of namespace in buildobjectevent:")
        print(type(namespace))
        try:
            result = namespace["id"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN ID")
            return None

    def buildLabel(self, namespace):
        try:
            result = namespace["label"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN label")
            return None

    def buildStartTime(self, namespace):
        try:
            result = namespace["startTime"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN starttime")
            return None

    def buildEndTime(self, namespace):
        try:
            result = namespace["endTime"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN endtime")
            return None

    def buildAthleteID(self, namespace):
        try:
            result = namespace["athleteID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildathleteid")
            return None

    def buildSessionID(self, namespace):
        try:
            result = namespace["sessionID"]
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildsessionid")
            return None

    def buildSubEvents(self, namespace):
        try:
            list = namespace["subEvents"]
            result = []
            for a in list:
                subEvent = SubEvent(a)
                subEvent.buildObject()
                result.append(subEvent)
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN buildSubEvents")
            return None

    def buildQualities(self, namespace):
        try:
            list = namespace["qualities"]
            result = []
            for a in list:
                try:
                    quality = a.type
                    result.append(quality)
                except AttributeError:
                    print("GOT ATTRIBUTEERROR IN buildQUALITIEs")
                    continue
            return result
        except AttributeError:
            return None
        #didn't test this

    def buildQuantities(self, namespace):
        try:
            list = namespace["quantities"]
            result = []
            for a in list:
                quantity = QuantitativeAttribute(a)
                quantity.buildObject()
                result.append(quantity)
            return result
        except AttributeError:
            print("GOT ATTRIBUTEERROR IN quantitites")
            return None