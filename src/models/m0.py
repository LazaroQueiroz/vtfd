from random import randint as ri
from src.models.model import Model
from src.models.process import Process
from math import ceil, log

class M0(Model):
    def __init__(self, physical_memory_size_B, kernel_space_B, address_space):
        super().__init__(physical_memory_size_B, kernel_space_B, address_space)
        self.base_reg = self.kernel_space_B
        self.limit_reg = self.physical_memory_size_B - 1
        self.processes.append(Process(0, address_space))

    def remove_all_processes(self):
        self.processes = []

    def generate_random_virtual_address(self):
        return self.processes[0].pid, self.processes[0].generate_random_virtual_address()

    def translate_virtual_address(self, virtual_address):
        return hex(virtual_address + self.base_reg)

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
                print(f"here's your base reg: [hex={hex(address)},bin={address:#0{bit_count_address_space + 2}b}]")
                while True:
                    reveal = input("reveal answer [y/N] ")
                    if reveal in "Yy" and reveal: break
                    else: continue

                physical_address_hex = self.translate_virtual_address(address)
                physical_address_binary = f"{int(physical_address_hex,16):#0{bit_count_address_space + 2}b}"
                print(f"heres your physical address: [hex={physical_address_hex},bin={physical_address_binary}]")
