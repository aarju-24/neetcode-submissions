class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        for n in nums:
            count[n]= count.get(n,0)+1

        freq_map ={}
        for n, freq in count.items():
            if freq not in freq_map:
                freq_map[freq]= []
            freq_map[freq].append(n)
        
        result =[]
        for i in range(len(nums), 0,-1):
            if i in freq_map:
                for num in freq_map[i]:
                    result.append(num)
                    if len(result)==k:
                        return result