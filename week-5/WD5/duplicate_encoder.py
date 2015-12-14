# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
# "din" => "((("
# "recede" => "()()()"
# "Success" => ")())())"
# "(( @" => "))(("

class CodeWars():
    def __init__(self, string):
        self.string = string.lower()

    def change_characters(self, char):
        return "(" if self.string.count(char) == 1 else ")"

    def encode(self):
        output = ""
        for char in self.string:
            output = self.change_caharcters(char)
