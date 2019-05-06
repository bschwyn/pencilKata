class Pencil:

    def __init__(self, length, durability, eraser):
        self.length = length
        self.original_durability = durability
        self.current_durability = durability
        self.eraser = eraser

    def _decrease_durability(self, char):
        if char.isupper():
            self.current_durability -=2
        elif char.islower():
            self.current_durability -=1
        else:
            self.current_durability -=0


    def write(self, text, paper):

        char_list = list(text)
        paper = list(paper)
        while char_list:
            next_char = char_list.pop(0)
            self._decrease_durability(next_char)
            paper.append(next_char) if self.current_durability >= 0 else paper.append(' ')
        return ''.join(paper)

    def sharpen(self):
        if self.length > 0:
            self.current_durability = self.original_durability
            self.length -=1


    def erase(self, tobeerased, paper):
        index = paper.rfind(tobeerased)
        paper_list = list(paper)
        if index > -1:
            for i in range(len(tobeerased)-1, -1, -1):
                if self.eraser >0 and paper_list[index + i] != ' ':
                    paper_list[index + i] = ' '
                    self.eraser -=1

        return ''.join(paper_list)




    def edit(self, writein, paper):
        pass
