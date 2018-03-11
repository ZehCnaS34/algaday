
class Trie:
    def __init__(self, value=None):
        if value:
            self.node = {value: Trie()}
        else:
            self.node = {}
        self.indicator = False

    def insert(self, string):
        if not string:
            return

        head = string[0]
        tail = string[1:]
        if not tail:
            if self.node[head]:
                self.node[head].indicator = True
            else:
                self.node[head] = True
                self.node[head].indicator = True

        if head in self.node:
            self.node[head].insert(tail)
        else:
            self.node[head] = Trie()
            self.node[head].insert(tail)

    def set_word(self):
        self.indicator = True
