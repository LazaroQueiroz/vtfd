from random import randint as ri, shuffle
from src.models.model import Model
from src.models.process import Process
from src.models.segmented_process import SegmentedProcess
from math import ceil, log

class Segmentation(Model):

    def __init__(self, physical_memory_size_B, kernel_space_B, segment_amount, processes_amount):
        address_space = (physical_memory_size_B - kernel_space_B) // processes_amount
        super().__init__(physical_memory_size_B, kernel_space_B, address_space)
        self.processes_amount = processes_amount
        self.segment_amount = segment_amount
        self.segment_size = self.address_space // segment_amount
        self.slots = [(base + kernel_space_B, base + kernel_space_B + self.segment_size) for base in range(0, self.physical_memory_size_B, self.segment_size)]
        self.populate_memory_with_processes()

    def remove_all_processes(self):
        self.processes = []

    def populate_memory_with_processes(self):
        process_ids = list(range(self.processes_amount))
        shuffle(process_ids)
        for pid in process_ids:
            p = SegmentedProcess(pid, self.address_space, self.segment_amount)
            p.populate_memory_with_segments(self.slots)
            self.processes.append(p)

    def get_process_seg_table(self, process_id):
        for pos, process in enumerate(self.processes):
            process = self.processes[pos]
            if process.get_pid() == process_id:
                return process.get_process_seg_table()
        return []

    def generate_random_virtual_address(self):
        position = self.generate_random_process_position()
        pid = self.processes[position].get_pid()
        return pid, self.processes[position].generate_random_virtual_address()

    def generate_random_process_position(self):
        return ri(0, len(self.processes) - 1)


    def translate_virtual_address(self, pid, virtual_address):
        seg_table = self.get_process_seg_table(pid)
        bit_count_address_space = ceil(log(self.address_space, 2))
        bit_count_seg_table = ceil(log(len(seg_table)))

        seg_id = virtual_address >> (bit_count_address_space - bit_count_seg_table)

        base, limit = seg_table[seg_id].get_base_limit()

        return hex(virtual_address + base)
    
    

    def start_loop(self):
        while True: 
            print("1. get random virtual address")
            print("2. translate virtual address")
            print("3. exit")
            i = int(input())
            if i == 3:
                return
            elif i == 1:
                print("here's your random virtual address: ", self.generate_random_virtual_address())
            elif i == 2: 
                bit_count_address_space = ceil(log(self.address_space, 2))
                address = int(input("type your virtual address (in hexadecimal, ex: ca, 1f, fff, 4cafe): "), 16)
                pid = int(input("type your process id: "))
                print("here's your base and limit regs: \nSEG_TABLE")
                for seg_id, segment in enumerate(self.get_process_seg_table(pid)):
                    print(f"segment {seg_id}: (base={segment.slot[0]:#0{bit_count_address_space + 2}b},limit={segment.slot[1]:#0{bit_count_address_space + 2}b})")
                while True:
                    reveal = input("reveal answer [y/N] ")
                    if reveal in "Yy" and reveal: break
                    else: continue
                physical_address_hex = self.translate_virtual_address(pid, address)
                bit_count_address_space = ceil(log(self.address_space, 2))
                physical_address_binary = f"{bin(int(physical_address_hex, 16)):#0{bit_count_address_space + 2}b}"
                print(f"heres your physical address: [hex={physical_address_hex},bin={physical_address_binary}]")

