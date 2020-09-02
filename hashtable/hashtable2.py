class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity > MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        self.storage = [None] * capacity
        self.item_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.item_count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211 

        hash_var = FNV_offset_basis
        string_bytes = key.encode()
        for b in string_bytes: 
            hash_var = hash_var * FNV_prime
            hash_var = hash_var ^ b
        return hash_var


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_var = 5381
        string_bytes = key.encode()
        for b in string_bytes:
            hash_var = ((hash_var << 5) + hash_var) + b
        return hash_var


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        # DAY 1: self.storage[self.hash_index(key)] = value

        # DAY 2: 
        # get hash index & the current node at that index (if any)
        index = self.hash_index(key)
        current = self.storage[index]

        # insert or update value
        # first check to see if the current node is there
        if current: 
            # if it is, loop thru
            while current: 
                # if you found the key
                if current.key == key: 
                    # update the value
                    current.value = value
                    return 
                # if it's not, move on to the next (if there is one)
                if current.next: 
                    current = current.next
                # otherwise, if there's no next value, create a new node and make it the next one
                else: 
                    current.next = HashTableEntry(key, value)
                    # current.next = HashTableEntry(key, value)
                    # incremement item_count
                    self.item_count += 1

        # if it's not there, make a new node & insert it at that index
        else: 
            self.storage[index] = HashTableEntry(key, value)
            # increment item_count
            self.item_count += 1

        # # check if load factor is >= 0.7
        if self.get_load_factor() > 0.7:
            # if it is, resize w/doubled capacity
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.storage[index]

        # check if key is NOT there
        if current is None: 
            # if it's not, print warning & return 
            print("Warning: key not found")
            return 

        # otherwise
        else: 
            # if it is, loop thru looking for key
            while current is not None: 
                # if find key
                if current.key == key: 
                    # remove by setting self.storage[index] to next node
                    self.storage[index] = current.next
                # otherwise keep iterating
                current = current.next

            # decrement item_count
            self.item_count -= 1

        # check if load factor is < 0.2 & if capacity is greater than double minimum capacity
        if self.get_load_factor() < 0.2 and self.capacity > (MIN_CAPACITY * 2):
            # resize to half capacity
            new_capacity = self.capacity / 2
            self.resize(new_capacity)


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.storage[index]

        # check if you can find something at that index
        if current is not None: 
            # if so, loop thru
            while current is not None: 
                # when you find the key
                if current.key == key: 
                    # return the value
                    return current.value
                # keep iterating
                current = current.next
        # if key not found, return None
        else: 
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        # store old storage
        old_storage = self.storage
        # update capacity & storage
        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        # iterate thru old
        for i in old_storage: 
            current = i
            while current is not None: 
                # rehash index
                index = self.hash_index(current.key)
                # restore
                self.storage[index] = current
                # keep iterating
                current = current.next







if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")