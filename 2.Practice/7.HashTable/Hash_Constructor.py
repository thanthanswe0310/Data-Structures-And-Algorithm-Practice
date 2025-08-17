from mypy.reachability import mark_block_mypy_only


class HashTable:
    def __init__(self,size =7):
        self.data_map  = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash +ord(letter) *23)% len(self.data_map)

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i," : ", val)

my_hash_table = HashTable()
my_hash_table.print_table()
