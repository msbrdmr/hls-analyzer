class VideoFramesInfo:

    def __init__(self):
        self.count = 0
        self.lastKfi = 0
        self.minKfi = 0
        self.maxKfi = 0
        self.lastKfPts = -1
        self.segmentsFirstFramePts = dict()
        self.media_sequence = -1
