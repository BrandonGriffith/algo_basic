class TwoSum:
    def brute_force(self, arr, num):
        for i in range(len(arr)):
            for x in range(1+i, len(arr)):
                if arr[i] + arr[x] == num:
                    return [i, x]
    
    def hashing(self, arr, num):
        hash = {}
        for i in range(len(arr)):
            x = num - arr[i]
            if x in hash:
                return [hash[x], i]
            hash[arr[i]] = i