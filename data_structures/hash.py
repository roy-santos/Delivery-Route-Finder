# Hash table implementation that utilizes linear probing to resolve collisions


# Class for representing an empty bucket
class EmptyBucket:
    pass


class HashTable:

    # Initialize hash table with the provided size and each bucket with an empty since start type.
    def __init__(self, capacity=10):
        # Constants to be used to represent the two types of empty buckets
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        self.array = [self.EMPTY_SINCE_START] * capacity

    def __iter__(self):
        return iter(self.array)

    # Hash function that hash table uses to determine which bucket the provided key is in.
    def hash(self, key):
        capacity = len(self.array)
        return key % capacity

    # Insert function that adds package to the hash table.Runtime complexity: Average case O(1), Worst case O(N)
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

    # Delete function removes the package with the matching key. Runtime complexity: Average case O(1), Worst case O(N)
    def remove(self, key):
        bucket = self.hash(key)
        buckets_probed = 0

        while self.array[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.array):
            if self.array[bucket] == key:
                self.array[bucket] = self.EMPTY_AFTER_REMOVAL

            bucket = (bucket + 1) % len(self.array)
            buckets_probed += 1

    # Look-up function that returns a package object. Runtime complexity: Average case O(1), Worst case O(N)
    def search(self, key):
        bucket = self.hash(key)
        buckets_probed = 0

        while self.array[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.array):
            if self.array[bucket] == key:
                return self.array[bucket]

            bucket = (bucket + 1) % len(self.array)
            buckets_probed += 1

        return None

    # Function that prints all off the packages held in the hash table. O(N) runtime complexity.
    def print_table(self):
        for item in self.array:
            #if type(item) is not EmptyBucket:
                print(item)


