from random import randint as ri

class Process():
    def __init__(self, pid, address_space):
        self.pid = pid
        self.address_space = address_space

    def get_pid(self):
        return self.pid

    def generate_random_virtual_address(self):
        return hex(ri(0, self.address_space - 1))

    def __str__(self):
        out = f"Process:\npid: {self.pid}\naddress space size(B): {self.address_space}"
        return out

    def __repr__(self):
        out = f"Process=[pid:={self.pid},address_space_size_B={self.address_space}]"
        return out
