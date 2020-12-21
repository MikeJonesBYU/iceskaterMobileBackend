from BuildObjectMember import BuildObjectMember as extractor
class Session:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.sessionID = None
        self.athleteID = None
        self.sport = None
        self.startTime = None
        self.endTime = None


    def buildObject(self):
        self.sessionID = extractor.buildSessionID(self, self.namespaceObj)
        self.athleteID = extractor.buildAthleteID(self, self.namespaceObj)
        self.sport = extractor.buildSport(self, self.namespaceObj)
        self.startTime = extractor.buildStartTime(self, self.namespaceObj)
        self.endTime = extractor.buildEndTime(self, self.namespaceObj)







    def get_athleteID(self):
        return self.athleteID

    def get_sessionID(self):
        return self.sessionID

    def get_sport(self):
        return self.sport

    def get_startTime(self):
        return self.startTime

    def get_endTime(self):
        return self.endTime

