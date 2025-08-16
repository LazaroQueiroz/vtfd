from process import Process

class SegmentedProcess(Process):

    def __init__(self, pid, address_space, segments_amount):
        super().__init__(pid, address_space)
        self.segments_amount = segments_amount
        self.segments = []


