class MyMath:
    def __init__(self, num_list):
        self.num_list = num_list

    def average_num(self):
        n = len(self.num_list)
        summa = 0
        for i in self.num_list:
            summa += i
        return summa / n
