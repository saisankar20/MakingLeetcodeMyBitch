class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        # Initialize the hashmap with a fixed size of buckets.
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key):
        # Simple hash function to map a key to a bucket index.
        return key % self.size

    def put(self, key, value):
        # Insert a key-value pair.
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value  # Update the value if the key exists.
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key, value)  # Add a new node at the end.

    def get(self, key):
        # Retrieve the value associated with the key.
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1  # Return -1 if the key does not exist.

    def remove(self, key):
        # Remove the key-value pair if it exists.
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return
            prev = current
            current = current.next
