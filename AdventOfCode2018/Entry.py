import datetime

class Entry:
    oDate = datetime.datetime.now()
    txtDate = ""
    entry = ""

    def __init__(self, inDate, inTxtDate, inEntry):
        self.oDate = inDate
        self.txtDate = inTxtDate
        self.entry = inEntry
