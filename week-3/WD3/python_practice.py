class MySuperString:
    def __init__(self, my_str):
        self.my_str = my_str

    def reverse(self):
        n = len(self.my_str)
        reversed = ''
        for i in range(n):
            reversed = self.my_str[i] + reversed
        return reversed

"""class MySuperString:
    def __init__(self, my_str):
        self.my_str = my_str

    def reverse(self):
        n = len(self.my_str)
        reversed = ''
        for i in range(n-1, -1, -1):
            reversed += self.my_str[i]
        return reversed"""

"""class MySuperString:
    def __init__(self, my_str):
        self.my_str = my_str

    def reverse(self):
        reversed = ''
        for i in self.my_str:
            reversed = i + reversed
        return reversed"""
