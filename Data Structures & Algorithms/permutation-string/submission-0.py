class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2= len(s1),len(s2)
        if n1>n2:
            return False
        
        freq1={}
        freq2={}

        for right in range(n1):
            freq1[s1[right]]= freq1.get(s1[right],0)+1
        left =0
        for right in range(n2):
            freq2[s2[right]]= freq2.get(s2[right],0)+1
            if right-left+1>n1:
                freq2[s2[left]]-=1

                if freq2[s2[left]]==0:
                    del freq2[s2[left]]
                left+=1
            if freq1== freq2:
                return True
        return False