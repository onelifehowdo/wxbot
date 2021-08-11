class message:
    def __init__(self, atlist, cpId, cpName, speakid, speaker, text, time):
        self.atList = atlist
        self.cpId = cpId
        self.cpName = cpName
        self.speakid = speakid
        self.speaker = speaker
        self.text = text
        self.time = time


class sqlMessage:
    cpid = ""
    cpName = ""
    speakerid = ""
    speaker = ""
    speakerType = ""
    text = ""
    time = 0

    type = ""
    model = None
    engineer = None
    status = None
    processor = None

    def __init__(self, msg, speakertype):
        self.cpid = msg.cpId
        self.cpName = msg.cpName
        self.speakerid = msg.speakid
        self.speaker = msg.speaker
        self.text = msg.text
        self.time = msg.time
        self.speakerType = speakertype

    # def setCpName(self,id):
    #     self.id=id
    def setType(self, type):
        self.type = type

    def setModle(self, model):
        self.model = model

    def setEngineer(self, engineer):
        self.engineer = engineer

    def setStatus(self, rspstu):
        self.status = rspstu

    def setPerson(self, solstu):
        self.processor = solstu
