class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key): 
        # check to see if key exists in LL...if it does, return the node. If not, return None. 
        current = self.head
        while current is not None: 
            if current.key == key:
                return current
            current = current.next
        return None

    def insert_at_head(self, key, value): 
        # check list to see if key is already in LL
        # if it is, update it's value to the new value being passed in
        found_node = self.find(key)
        if found_node is not None: 
            found_node.value = value
            return 

        # if it's not there, make a new node and insert at head...existing head becomes new node's next value
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        # start at head
        curr = self.head

        # if we want to delete the head, reassign self.head to curr.next and set curr to None
        if curr is not None: 
            if curr.key == key:
                self.head = curr.next
                curr = None
        
        # if it's not the head, search for the node we want to delete...keeep track of prev
        while curr is not None: 
            if curr.key == key: 
                break
            prev = curr
            curr = curr.next
        # if key not found 
        if curr is None: 
            return 
        # unlink node and set it's value to None
        prev.next = curr.next 
        curr = None

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
        # Day 1: self.storage = [None] * capacity
        self.storage = [LinkedList()] * capacity # change to LL instance
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
        pass


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
        # DAY 1: self.storage[self.hash_index(key)] = value

        # get hash index
        index = self.hash_index(key)
        # call insert_at_head LL method
        self.storage[index].insert_at_head(key, value)
        # increment item_count
        self.item_count += 1

        # check if load factor is >= 0.7
        if self.get_load_factor() > 0.7: 
            # if it is, resize w/ doubled capacity
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # DAY 1: 
        # if self.storage[self.hash_index(key)] is None:
        #     return("Key not found")
        # else:
        #     self.storage[self.hash_index(key)] = None

        # get hash index
        index = self.hash_index(key)
        # check if key is there...if not, print warning
        if self.storage[index].find(key) is None: 
            print("Key not found")
            return
        # call LL delete method
        self.storage[index].delete(key)
        # decrement item_count
        self.item_count -= 1

        # check if load factor is < 0.2 and if capacity is greater than double the minimum capacity
        if self.get_load_factor() < 0.2 and self.capacity > (MIN_CAPACITY * 2): 
            # resize to half the capacity
            new_capacity = self.capacity / 2
            self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # DAY 1: return self.storage[self.hash_index(key)]

        # get hash index
        index = self.hash_index(key)
        # call LL find method
        found_node = self.storage[index].find(key)
        if found_node is not None: 
            return found_node.value
        else: 
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_storage = [LinkedList()] * new_capacity
        # self.capacity = new_capacity
        for i in range(len(self.storage)):
            cur = self.storage[i].head
            while cur is not None: 
                new_storage[i].insert_at_head(cur.key, cur.value)
                cur = cur.next
        self.capacity = new_capacity
        self.storage = new_storage


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
