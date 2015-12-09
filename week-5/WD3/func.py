
# def adder(array):
#     def add(n):
#         return n+1
#     return list(map(add, array))

    def adder(array):
        return list(map(lambda x : x + 1, array))

    def filterArray(array):
        return list(filter(lambda x : x % 3 == 0, array))
