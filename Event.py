from BuildObjectEvent import BuildObjectEvent as extractor
class Event:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.id = None
        self.label = None
        self.startTime = None
        self.endTime = None
        self.athleteID = None
        self.sessionID = None
        #self.subEvents = None missing!!!
        #self.qualities = None missing!!!
        self.quantities = None





    def buildObject(self):
        self.id = extractor.buildID(self, self.namespaceObj)
        self.label = extractor.buildLabel(self, self.namespaceObj)
        self.startTime = extractor.buildStartTime(self, self.namespaceObj)
        self.endTime = extractor.buildEndTime(self, self.namespaceObj)
        self.athleteID = extractor.buildAthleteID(self, self.namespaceObj)
        self.sessionID = extractor.buildSessionID(self, self.namespaceObj)
        #self.subEvents = extractor.buildSubEvents(self, self.namespaceObj)
        #self.qualities = extractor.buildQualities(self, self.namespaceObj)
        self.quantities = extractor.buildQuantities(self, self.namespaceObj)



    def get_ID(self):
        return self.id

    def get_label(self):
        return self.label

    def get_startTime(self):
        return self.startTime

    def get_endTime(self):
        return self.endTime

    def get_athleteID(self):
        return self.athleteID

    def get_sessionID(self):
        return self.sessionID

    def get_subEvents(self):
        return self.subEvents

    def get_quantities(self):
        return self.quantities

    def purgeMethods(self, list):
        new_list = []
        for el in list:
            name = el[0]
            if not "__" in name:
                new_list.append(el)
        return new_list