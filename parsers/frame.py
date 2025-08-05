
class Frame:

    def __init__(self, frameType, timeUs):
        self.type = frameType
        self.timeUs = timeUs

    def isKeyframe(self):
        if self.type == "I":
            return True
        return False
