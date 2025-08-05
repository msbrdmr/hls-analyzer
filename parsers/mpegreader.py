
from bitreader import BitReader
from parsers.payloadreader import PayloadReader

class MpegReader(PayloadReader):

    def __init__(self):
        PayloadReader.__init__(self)
        self.firstTimeStamp = -1
        self.timeUs = -1

    def getMimeType(self):
        return "audio/mpeg"

    def getFormat(self):
        return "MPEG Audio (MP3)"

    def getFirstPTS(self):
        return self.firstTimeStamp

    def getLastPTS(self):
        return self.timeUs

    def consumeData(self, pts):
        if(self.firstTimeStamp == -1):
            self.firstTimeStamp = pts;

        if(pts != -1):
            self.timeUs = pts
