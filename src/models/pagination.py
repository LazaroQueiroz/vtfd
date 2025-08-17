from random import randint as ri, shuffle
from src.models.model import Model
from src.models.process import Process
from src.models.paginated_process import PaginatedProcess
from math import ceil, log
import os

class Pagination(Model):

    def __init__(self, physical_memory_size_B, kernel_space_B, pages_amount, processes_amount):
        address_space = (physical_memory_size_B - kernel_space_B) // processes_amount
        super().__init__(physical_memory_size_B, kernel_space_B, address_space)
        self.processes_amount = processes_amount
        self.pages_amount = pages_amount
        self.page_size = self.address_space // pages_amount
        self.slots = [(base + kernel_space_B, base + kernel_space_B + self.page_size) for base in range(0, self.physical_memory_size_B, self.page_size)]
        self.populate_memory_with_processes()

    def remove_all_processes(self):
        self.processes = []

    def populate_memory_with_processes(self):
        process_ids = list(range(self.processes_amount))
        shuffle(process_ids)
        for pid in process_ids:
            p = PaginatedProcess(pid, self.address_space, self.pages_amount)
            p.populate_memory_with_pages(self.slots)
            self.processes.append(p)

    def get_process_page_table(self, process_id):
        for pos, process in enumerate(self.processes):
            process = self.processes[pos]
            if process.get_pid() == process_id:
                return process.get_process_page_table()
        return []

    def generate_random_virtual_address(self):
        position = self.generate_random_process_position()
        pid = self.processes[position].get_pid()
        return pid, self.processes[position].generate_random_virtual_address()

    def generate_random_process_position(self):
        return ri(0, len(self.processes) - 1)


    def translate_virtual_address(self, pid, virtual_address):
        page_table = self.get_process_page_table(pid)
        bit_count_address_space = ceil(log(self.address_space, 2))
        bit_count_seg_table = ceil(log(len(page_table)))

        page_id = virtual_address >> (bit_count_address_space - bit_count_seg_table)

        base, limit = page_table[page_id].get_base_limit()

        return hex(virtual_address + base)
    
    

    def start_loop(self):
        os.system("clear")
        print(f"Pagination\n{'-' * 30}\nphy. mem. size (B): {self.physical_memory_size_B}\nkernel space size (B): {self.kernel_space_B}\namount of processes: {self.processes_amount}\npages per process: {self.pages_amount}\n{'-' * 30}")
        while True: 
            print("1. get random virtual address")
            print("2. translate virtual address")
            print("3. exit")
            i = int(input())
            if i == 3:
                os.system('clear') 
                return
            elif i == 1:
                print("\nhere's your random virtual address: ", self.generate_random_virtual_address())
            elif i == 2: 
                bit_count_address_space = ceil(log(self.address_space, 2))
                address = int(input("type your virtual address (in hexadecimal, ex: ca, 1f, fff, 4cafe): "), 16)
                pid = int(input("type your process id: "))
                print(f"\nhere's your virtual address: [hex={hex(address)},bin={address:#0{bit_count_address_space + 2}b}]\n")
                print('-'*80)
                for seg_id, segment in enumerate(self.get_process_page_table(pid)):
                    print(f"segment {seg_id}: base=[hex={hex(segment.slot[0])},bin={segment.slot[0]:#0{bit_count_address_space + 2}b}],\tlimit=[hex={hex(segment.slot[1])},bin={segment.slot[1]:#0{bit_count_address_space + 2}b}]\n")
                print('-'*80)
                while True:
                    reveal = input("reveal answer [y/N] ")
                    if reveal in "Yy" and reveal: break
                    else: continue
                physical_address_hex = self.translate_virtual_address(pid, address)
                bit_count_address_space = ceil(log(self.address_space, 2))
                physical_address_binary = f"{int(physical_address_hex, 16):#0{bit_count_address_space + 2}b}"
                print(f"\nheres your physical address: [hex={physical_address_hex},bin={physical_address_binary}]")

