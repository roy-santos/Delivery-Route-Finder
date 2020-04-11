# Hash table implementation that utilizes linear probing to resolve collisions


# Class for representing an empty bucket
class EmptyBucket:
    pass


class HashTable:

    def __init__(self, capacity=10):

        # Constants to be used to represent the two types of empty buckets
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        self.array = [self.EMPTY_SINCE_START] * capacity

    def hash(self, key):
        capacity = len(self.array)
        return key % capacity

    # Runtime complexity: Average case O(1), Worst case O(N)
    def insert(self, value):
        bucket = self.hash(value.package_id)
        buckets_probed = 0

        while buckets_probed < len(self.array):
            if type(self.array[bucket]) is EmptyBucket:
                self.array[bucket] = value
                return True

            bucket = (bucket + 1) % len(self.array)
            buckets_probed += 1

        return False

    # Runtime complexity: Average case O(1), Worst case O(N)
    def remove(self, key):
        bucket = self.hash(key)
        buckets_probed = 0

        while self.array[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.array):
            if self.array[bucket] == key:
                self.array[bucket] = self.EMPTY_AFTER_REMOVAL

            bucket = (bucket + 1) % len(self.array)
            buckets_probed += 1

    # Runtime complexity: Average case O(1), Worst case O(N)
    def search(self, key):
        bucket = self.hash(key)
        buckets_probed = 0

        while self.array[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.array):
            if self.array[bucket] == key:
                return self.array[bucket]

            bucket = (bucket + 1) % len(self.array)
            buckets_probed += 1

        return None


