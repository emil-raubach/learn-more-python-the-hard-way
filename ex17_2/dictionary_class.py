from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        self.map = DoubleLinkedList()
        
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        return hash(key) % self.map.count()


    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)


    def get_slot(self, key, default=None):
        bucket = self.get_bucket(key)

        if bucket:
            slot = bucket.begin

            while slot:
                if slot.value[0] == key:
                    return bucket, slot
                else:
                    slot = slot.next

        return bucket, default


    def get(self, key, default=None):
        bucket, slot = self.get_slot(key) # add `default=default`
        
        return slot and slot.value[1] or default


    def set(self, key, value):
        bucket, slot = self.get_slot(key)

        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))


    def delete(self, key):
        bucket = self.get_bucket(key)
        slot = bucket.begin

        while slot:
            k, v = slot.value

            if k == key:
                bucket.detach_node(slot)
                break
            else:
                slot = slot.next


    def list(self):
        bucket_node = self.map.begin

        while bucket_node:
            
            slot_node = bucket_node.value.begin

            while slot_node:
                print(slot_node.value)

                slot_node = slot_node.next

            bucket_node = bucket_node.next

