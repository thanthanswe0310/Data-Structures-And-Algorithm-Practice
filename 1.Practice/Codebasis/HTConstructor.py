### HashTable ###

class HashTable:
    def __hash(self,key):
        my_hash = (my_hash + ord(letter)*23)% len(self.data_map)
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i," : ",val)


my_hash_table = HashTable()
my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('washers',50)

### Get function: Retrieves (gets) the value of a private variable=>getName() returns the name
### set function: Updates (sets) the value of a private variable=> setName("John") sets the name to John


