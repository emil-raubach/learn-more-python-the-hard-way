from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        self.map = DoubleLinkedList() # create new dllist
        # Create a new dllist for each bucket in the map
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())
    
    def hash_key(self, key):
        """Given a key this will create a number and then convert it to
        an index for the aMap's buckets."""
        # uses a key to get a unique integer, modulus to get the index
        return hash(key) % self.map.count()
    
    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        # gets index for a key and assigns it to a bucket
        bucket_id = self.hash_key(key)
        # uses index to get the value of the bucket (which is a dllist node)
        return self.map.get(bucket_id) # calls the dllist get() function! OMG!!

    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        """
        # gets ref to the slot dllist for a given key
        bucket = self.get_bucket(key) # slot not bucket right?
        # if the slot in the bucket is not None
        if bucket:
            # initialize to first node in the slot dllist
            node = bucket.begin # set to first node
            i = 0
            # traverse the slot dllist & check for keys existance
            while node:
                # if the key matches the first element of the key/value tuple
                if key == node.value[0]:
                    return bucket, node # return the bucket and a ref to the slot / node
                else:
                    node = node.next 
                    i += 1 # not sure what this is for...
        # fall through for both if and while above
        return bucket, None # if key isn't already in the list

    def get(self, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        # gets the bucket and slot for a given key
        bucket, node = self.get_slot(key, default=default)
        # ternary operation; if there's a node it returns
        # it's value, if it exists, else the default (None)
        return node and node.value[1] or default

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        # gets the bucket and slot for a new key/value pair
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        # gets the bucket (slot) for the key to be removed
        bucket = self.get_bucket(key)
        node = bucket.begin
        # traverse the slot dllist
        while node:
            # unpack the tuple to get the key for comparison
            k, v = node.value
            # check if the keys match
            if key == k:
                # if so, remove the node and exit the loop
                bucket.detach_node(node)
                break
            else: # otherwise, keep going
                node = node.next

    def list(self):
        """Prints out what's in the Map."""
        # start at the first node of the map
        bucket_node = self.map.begin
        # iterate over the buckets
        while bucket_node:
            # get the first node of the slot list in the given bucket
            slot_node = bucket_node.value.begin
            # iterate through the slot list
            while slot_node:
                # print the value and get the next node
                print(slot_node.value)
                slot_node = slot_node.next
            # get the next bucket
            bucket_node = bucket_node.next