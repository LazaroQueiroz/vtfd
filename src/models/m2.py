from random import randint as ri
from process import Process
from model import Model

class M2(Model):

    # TODO: add reallocation and real process locations

    def __init__(self, physical_memory_size_B, kernel_space_B, address_space, partition_amount):
        super.__init__(physical_memory_size_B, kernel_space_B, address_space)
        self.partition_amount = partition_amount
        self.partition_size = self.physical_memory_size_B // partition_amount
        self.processes = []

    def remove_all_processes(self):
        self.processes = []

    def populate_memory_with_processes(self):
        process_ids = set(range(self.partition_amount))
        for pid in process_ids:
            p = Process(pid, self.address_space)
            self.processes.append(p)

    def generate_random_virtual_address(self):
        process_id = self.generate_random_process_number()
        return process_id, self.processes[process_id].generate_random_virtual_address()

    def generate_random_process_number(self):
        return ri(0, self.partition_amount - 1)

    def translate_virtual_address(self, virtual_address, process_number):
        base_reg = self.partition_size * process_number
        return hex(virtual_address + base_reg)
