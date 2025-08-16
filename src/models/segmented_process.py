from random import choice, shuffle
from src.models.process import Process
from src.models.segment import Segment

class SegmentedProcess(Process):

    def __init__(self, pid, address_space, segments_amount):
        super().__init__(pid, address_space)
        self.segments_amount = segments_amount
        self.segments = []

    def populate_memory_with_segments(self, free_slots):
        while len(self.segments) < self.segments_amount and free_slots:
            slot = choice(free_slots)
            free_slots.remove(slot)
            segment = Segment(len(self.segments), slot)
            self.segments.append(segment)

    def get_process_seg_table(self):
        return self.segments

    def __str__(self):
        out = f"Process=[pid={self.pid},address_space_size_B={self.address_space},segments={self.segments}]"
        return out

    def __repr__(self):
        out = f"Process=[pid={self.pid},address_space_size_B={self.address_space},segments={self.segments}]"
        return out

            

