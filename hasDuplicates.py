class HasDuplicates:
    def brute_force(self, arr):
        for i in range(len(arr)):
            for x in range(i+1, len(arr)):
                if arr[i] == arr[x]:
                    return True
        return False
    
    def sorting(self,arr):
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return True
        return False
    
    def hashing(self, arr):
        hash_set = set()
        for i in arr:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False
    
    def hash_len(self, arr):
        return len(arr) != len(set(arr))
