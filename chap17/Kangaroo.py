# Exercise 17.2

class Kangaroo:

    def __init__(self):
        self.pouch_contents = []
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
    def __str__(self):
        kstr = 'Kangaroo with pouch: ['
        for item in self.pouch_contents:
            kstr += str(item) + ', '
        kstr = kstr[:-2] + ']'
        return kstr

def test():
    kanga = Kangaroo()
    roo = Kangaroo()
    roo.put_in_pouch("little wallet")
    roo.put_in_pouch("little keys")
    kanga.put_in_pouch("wallet")
    kanga.put_in_pouch("keys")
    kanga.put_in_pouch(roo)
    print("kanga:")
    print(kanga)
    print("roo:")
    print(roo)

if __name__ == '__main__':
    test()
