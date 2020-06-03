class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        # If nothing found
        return None
    
    def delete(self, value):
        cur = self.head
        # Special case of deleting the head of list
        if cur.value == value:
            self.head = cur.next
            return cur
        
        while cur.next is not None:
            if cur.next.value == value:
                deleted = cur.next
                cur.next = cur.next.next
                return deleted
            cur = cur.next

        

if __name__ == "__main__":
     ll = LinkedList()
     ll.insert_at_head(Node(11))


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)}'


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
        self.capacity = [None] * capacity
        self.num_stored = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def custom_hash(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        string_bytes = key.encode()
        total = 0

        for b in string_bytes:
            total += b
        return total

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.get_num_slots()
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.num_stored += 1
        
        slot = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        # if empty
        if self.capacity[slot] is None:
            # insert
            self.capacity[slot] = new_entry
        # if not empty
        else:
            # insert at head
            new_entry.next = self.capacity[slot]
            self.capacity[slot] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        cur = self.capacity[slot]

        # if that slot is not empty
        if cur:
            # if head ( first one ) is the desired node
            if cur.key == key:
                deleted = cur
                self.capacity[slot] = cur.next
                self.num_stored -= 1
                return deleted
            else:
                while cur.next is not None:
                    if cur.next.key == key:
                        deleted = cur.next
                        cur.next = cur.next.next
                        self.num_stored -= 1
                        return deleted
                    cur = cur.next
                return 'nothing by that key to delete'
        return 'slot is empty'

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        cur = self.capacity[slot]
        # if that slot is not empty
        if cur:
            if cur.key == key:
                return self.capacity[slot].value
            else:
                while cur is not None:
                    if cur.key == key:
                        return cur.value
                    cur = cur.next
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_cap = self.capacity
        self.capacity = [None] * new_capacity

if __name__ == "__main__":
    ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("\nMy Logs:\n")
    ht.put('Country','voight')
    ht.put('shawn','Tompke')
    ht.put('bar','bar_value')
    ht.put('baz','baz_value' ) # overwrites bar
    ht.put('bal','bal_value')


    # ht.delete('Country')
    print(ht.delete('baz'))
    print(ht.delete('baz'))
    print(ht.delete('bar'))
    print(ht.delete('bar'))


    print(ht.capacity)
    print(ht.num_stored)
    print(len(ht.capacity))
    print(ht.resize(16))
    print(len(ht.capacity))