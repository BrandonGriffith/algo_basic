class GroupAnagrams:
    def sorting(self, arr):
        hash = {}
        for i in arr:
            sorted_string = ''.join(sorted(i))
            if sorted_string in hash:
                hash[sorted_string].append(i)
            else:
                hash[sorted_string] = [i]
        return list(hash.values())

    def hashing(self, arr):
        result = []
        visited = [False] * len(arr)
        
        for i in range(len(arr)):
            if not visited[i]:
                hash = {}
                temp = []
                for x in arr[i]:
                    if x in hash:
                        hash[x] += 1
                    else:
                        hash[x] = 1
                for j in range(len(arr)):
                    if not visited[j]:
                        hash2 = {}
                        for x in arr[j]:
                            if x in hash2:
                                hash2[x] += 1
                            else:
                                hash2[x] = 1
                        if hash == hash2:
                            temp.append(arr[j])
                            visited[j] = True
                result.append(temp)
        return result