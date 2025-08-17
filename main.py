from src.models.m0 import M0
from src.models.m1 import M1
from src.models.segmentation import Segmentation
from src.models.pagination import Pagination
import os

def handle_models():

    while True:
        print("Select a model:\n0.M0\n1.M1\n2.M2\n3.Segmentation\n4.Pagination\n5.Exit VTFD")

        i = int(input("Your choice: "))
        os.system('clear')
        if i == 5:
            return
        elif i == 0:
            print("#" * 80)
            print()
            print("Hey, you chose Model 0")
            physical_memory_size_B = int(input("Enter your physical memory size (in bytes): "))
            kernel_space_B = int(input("Enter you kernel space size (in bytes): "))
            address_space_B = physical_memory_size_B - kernel_space_B
            model = M0(physical_memory_size_B, kernel_space_B, address_space_B)
            model.start_loop()
        elif i == 1:
            print("#" * 80)
            print()
            print("Hey, you chose Model 1")
            physical_memory_size_B = int(input("Enter your physical memory size (in bytes): "))
            kernel_space_B = int(input("Enter you kernel space size (in bytes): "))
            partition_amount = int(input("Enter the amount of process in the system: "))
            model = M1(physical_memory_size_B, kernel_space_B, partition_amount)
            model.start_loop()
        elif i == 2:
            print("#" * 80)
            print()
            print("Hey, you chose Model 2")
            physical_memory_size_B = int(input("Enter your physical memory size (in bytes): "))
            kernel_space_B = int(input("Enter you kernel space size (in bytes): "))
            partition_amount = int(input("Enter the amount of process in the system: "))
            model = M1(physical_memory_size_B, kernel_space_B, partition_amount)
            model.start_loop()
        elif i == 3:
            print("#" * 80)
            print()
            print("Hey, you chose Segmentation Model")
            physical_memory_size_B = int(input("Enter your physical memory size (in bytes): "))
            kernel_space_B = int(input("Enter you kernel space size (in bytes): "))
            partition_amount = int(input("Enter the amount of process in the system: "))
            segments_amount = int(input("Enter the amount of segments for each process: "))
            model = Segmentation(physical_memory_size_B, kernel_space_B, segments_amount, partition_amount)
            model.start_loop()
        elif i == 4:
            print("#" * 80)
            print()
            print("Hey, you chose Pagination Model")
            physical_memory_size_B = int(input("Enter your physical memory size (in bytes): "))
            kernel_space_B = int(input("Enter you kernel space size (in bytes): "))
            partition_amount = int(input("Enter the amount of process in the system: "))
            pages_amount = int(input("Enter the amount of pages for each process: "))
            model = Pagination(physical_memory_size_B, kernel_space_B, pages_amount, partition_amount)
            model.start_loop()
        else:
            return
        os.system('clear') 

def main():
    os.system("clear")
    print("░██    ░██ ░██████████░██████████░███████\n░██    ░██     ░██    ░██        ░██   ░██\n░██    ░██     ░██    ░██        ░██    ░██\n░██    ░██     ░██    ░█████████ ░██    ░██\n ░██  ░██      ░██    ░██        ░██    ░██\n  ░██░██       ░██    ░██        ░██   ░██\n   ░███        ░██    ░██        ░███████")
    print("\nWelcome to the Virtual Translator For Dynamic Memory =)")
    handle_models()

if __name__ == "__main__":
    main()


