# class to represent an empty bucket
class EmptyBucket:
    pass


# Hash table class definition using linear probing for collision resolution
class LinearProbingHashTable:

    def __init__(self, initial_capacity=10):

        # Special constants to be used as the two types of empty buckets.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all the table buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

    def insert(self, item):
        bucket = hash(item) % len(self.table)
        buckets_probed = 0

        while buckets_probed < len(self.table):
            # if the bucket is empty, the item can be inserted at that index.
            # Else, continue probing to next index in table.
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                print(bucket)
                return True
            else:
                bucket = (bucket + 1) % len(self.table)
                buckets_probed = buckets_probed + 1

        # Entire table was full and the key could not be inserted.
        return False

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0

        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL

            # Bucket was occupied by a different key (or was previously occupied), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

    def search(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0

        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                return self.table[bucket]

            # Bucket was occupied by a different key (or was previously occupied), so continue probing.
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # Entire table was probed or  empty cell was found
        return None

    def __str__(self):
        s = "   --------\n"
        index = 0
        for bucket in self.table:
            value = str(bucket)
            if bucket is self.EMPTY_SINCE_START:
                value = 'E/S'
            elif bucket is self.EMPTY_AFTER_REMOVAL:
                value = 'E/R'
            s += '{:2}:|{:^6}|\n'.format(index, value)
            index += 1
        s += "   --------"
        return s
