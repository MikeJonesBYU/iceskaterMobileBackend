class BuildObjectMember:

    def buildSessionID(self, namespace):
        try:
            result = namespace.sessionID
            return result
        except AttributeError:
            return None

    def buildAthleteID(self, namespace):
        try:
            result = namespace.athleteID
            return result
        except AttributeError:
            return None

    def buildSport(self, namespace):
        try:
            result = namespace.sport
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

