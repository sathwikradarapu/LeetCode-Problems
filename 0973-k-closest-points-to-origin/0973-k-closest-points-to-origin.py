class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        length=len(points)
        hash_map={}
        for index in range(length):
            list1=points[index]
            distance=(list1[0]**2)+(list1[1]**2)
            if distance in hash_map:
                hash_map[distance].append(list1)
            else:
                hash_map[distance]=[list1]
        sorted_hash_map = dict(sorted(hash_map.items()))

        result = list(sorted_hash_map.values())

        answer = []

        for i in result:
            for j in i:
                answer.append(j)
                if len(answer) == k:
                    return answer

        return answer