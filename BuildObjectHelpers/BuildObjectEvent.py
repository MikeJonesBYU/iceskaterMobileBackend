import inspect

from Model.SubEvent import SubEvent
from Model.QuantitativeAttribute import QuantitativeAttribute

class BuildObjectEvent:

    def buildID(self, namespace):
        try:
            result = namespace.id
            return result
        except AttributeError:
            return None

    def buildLabel(self, namespace):
        try:
            result = namespace.label
            return result
        except AttributeError:
            return None

    def buildStartTime(self, namespace):
        try:
            result = namespace.startTime
            return result
        except AttributeError:
            return None

    def buildEndTime(self, namespace):
        try:
            result = namespace.endTime
            return result
        except AttributeError:
            return None

    def buildAthleteID(self, namespace):
        try:
            result = namespace.athleteID
            return result
        except AttributeError:
            return None

    def buildSessionID(self, namespace):
        try:
            result = namespace.sessionID
            return result
        except AttributeError:
            return None

    def buildSubEvents(self, namespace):
        try:
            x = namespace.subEvents
            list = self.purgeMethods(inspect.getmembers(x))
            result = []
            for a in list:
                event = SubEvent(a)
                event.buildObject()
                result.append(event)
            return result
        except AttributeError:
            return None

    def buildQualities(self, namespace):
        try:
            result = namespace.qualities
            return result
        except AttributeError:
            return None

    def buildQuantities(self, namespace):
        try:
            list = namespace.quantities
            result = []
            for a in list:
                quantity = QuantitativeAttribute(a)
                quantity.buildObject()
                result.append(quantity)
            return result
        except AttributeError:
            return None