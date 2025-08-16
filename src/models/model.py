from random import randint as ri

class Model:
    def __init__(self, physical_memory_size_B, kernel_space_B, address_space):
        self.physical_memory_size_B = physical_memory_size_B
        self.kernel_space_B = kernel_space_B
        self.user_space_B = self.physical_memory_size_B - self.kernel_space_B
        self.address_space = address_space
        self.processes = []
