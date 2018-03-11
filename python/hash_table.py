class HashTable:
    def __init__(self):
        # NOTE: I could change None to an empty array
        self.data = [None for _ in range(10)]

    def get(self, key):
        h = hash(key)
        slot = h % len(self.data)

        if self.data[slot]:
            for v, k in self.data[slot]:
                if k == key:
                    return v

    def put(self, key, value):
        h = hash(key)
        slot = h % len(self.data)

        if not self.data[slot]:
            self.data[slot] = [(value, key)]
        else:
            index = -1
            for i, vk in enumerate(self.data[slot]):
                _, k = vk
                if k == key:
                    index = i
                    break
            
            if index == -1:
                self.data[slot].append((value, key))
            else:
                print("updating")
                self.data[slot][index] = (value, key)

def random_key():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

if __name__=='__main__':
    import random
    import string
    from random import randrange
    mh = HashTable()
    keys = [random_key() for _ in range(5)]
    for x in keys:
        mh.put(x, x)
    print(mh.data)
    print(mh.get(keys[0]))
