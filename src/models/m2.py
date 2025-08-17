from random import randint as ri
from process import Process
from model import Model
from random import shuffle
import os
from math import ceil, log

class M2(Model):

    # TODO: add reallocation and real process locations

    def __init__(self, physical_memory_size_B, kernel_space_B, partition_amount):
        self.partition_size = (physical_memory_size_B - kernel_space_B) // partition_amount
        super().__init__(physical_memory_size_B, kernel_space_B, self.partition_size)
        self.partition_amount = partition_amount
        self.populate_memory_with_processes()

    def remove_all_processes(self):
        self.processes = []

    def populate_memory_with_processes(self):
        processes_ids = list(range(self.partition_amount))
        shuffle(processes_ids)
        for pid in processes_ids:
            p = Process(pid, self.address_space)
            self.processes.append(p)

    def generate_random_virtual_address(self):
        position = self.generate_random_process_position()
        pid = self.processes[position].get_pid()
        return pid, self.processes[position].generate_random_virtual_address()

    def translate_virtual_address(self, pid, virtual_address):
        base, limit = self.get_process_base_limit(pid)
        physical_address = virtual_address + base
        return hex(physical_address)

    def get_process_base_limit(self, pid):
        for pos, process in enumerate(self.processes):
            if process.get_pid() == pid:
                base = pos * self.partition_size
                limit = base + self.partition_size - 1
                return (base, limit)
        return (-1, -1)


    def generate_random_process_position(self):
        return ri(0, self.partition_amount - 1)


    def start_loop(self):
        os.system('clear')
        print(f"MODEL 2\n{'-' * 30}\nphy. mem. size (B): {self.physical_memory_size_B}\nkernel space size (B): {self.kernel_space_B}\namount of processes: {self.partition_amount}\n{'-' * 30}")
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
                print(f"\nhere's your base reg: [hex={hex(address)},bin={bin(address):#0{bit_count_address_space + 2}b}]")
                pid = int(input("type your process id: "))
                print(f"\nhere's your base and limit regs: {self.get_process_base_limit(pid)}\n")
                while True:
                    reveal = input("reveal answer [y/N] ")
                    if reveal in "Yy" and reveal: break
                    else: continue
                physical_address_hex = self.translate_virtual_address(pid, address)
                bit_count_address_space = ceil(log(self.address_space, 2))
                physical_address_binary = f"{bin(int(physical_address_hex, 16)):#0{bit_count_address_space + 2}b}"
                print(f"\nhere's your physical address: [hex={physical_address_hex},bin={physical_address_binary}]")

