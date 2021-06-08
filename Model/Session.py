from BuildObjectHelpers.BuildObjectSession import BuildObjectSession as extractor


class Session:
    def __init__(self, namespaceObj):
        self.namespaceObj = namespaceObj
        self.sessionID = None
        self.athleteID = None
        self.sport = None
        self.startTime = None
        self.endTime = None
        self.status = None
        self.sensors = None
        self.events = None
        self.deviceID = None

    def buildObject(self):
        print("building object")
        self.sessionID = extractor.buildSessionID(self, self.namespaceObj)
        self.athleteID = extractor.buildAthleteID(self, self.namespaceObj)
        self.sport = extractor.buildSport(self, self.namespaceObj)
        self.startTime = extractor.buildStartTime(self, self.namespaceObj)
        self.endTime = extractor.buildEndTime(self, self.namespaceObj)
        self.status = extractor.buildStatus(self, self.namespaceObj)
        self.sensors = extractor.buildSensors(self, self.namespaceObj)
        self.events = extractor.buildEvents(self, self.namespaceObj)

        # No device id in json as of 6/2/2021
        # self.deviceID = extractor.buildDeviceID(self, self.namespaceObj)



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

    def get_status(self):
        return self.status

    def get_deviceID(self):
        return self.deviceID

    def get_sensors(self):
        return self.sensors

    def get_events(self):
        return self.events

    def purgeMethods(self, list):
        print("why is this being called purgemethods?")
        new_list = []
        for el in list:
            name = el[0]
            if not "__" in name:
                new_list.append(el)
        return new_list

