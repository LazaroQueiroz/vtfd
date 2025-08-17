from random import choice, shuffle
from src.models.process import Process
from src.models.segment import Segment

class PaginatedProcess(Process):

    def __init__(self, pid, address_space, pages_amount):
        super().__init__(pid, address_space)
        self.segments_amount = pages_amount
        self.page_table = []

    def populate_memory_with_pages(self, free_slots):
        while len(self.page_table) < self.segments_amount and free_slots:
            slot = choice(free_slots)
            free_slots.remove(slot)
            segment = Segment(len(self.page_table), slot)
            self.page_table.append(segment)

    def get_process_page_table(self):
        return self.page_table

    def __str__(self):
        out = f"Process=[pid={self.pid},address_space_size_B={self.address_space},page_table={self.segments}]"
        return out

    def __repr__(self):
        out = f"Process=[pid={self.pid},address_space_size_B={self.address_space},page_table={self.segments}]"
        return out

