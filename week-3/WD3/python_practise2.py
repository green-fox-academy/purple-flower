class MySuperString:
    def __init__(self, my_str):
        self.my_str = my_str

    def count_characters(self, char):
        count = 0
        for actualchar in self.my_str:
             if char == actualchar:
                 count += 1
        return count

    def nospace(self):
        new_str = ''
        for i in self.my_str:
            if i == ' ':
                new_str = new_str + '_'
            else:
                new_str = new_str + i
        return new_str
