class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result=[]
        for hrs in range(12):
            for mins in range(60):
                if((bin(hrs)+bin(mins)).count('1')==turnedOn):
                    time='%d:%02d'%(hrs,mins)
                    result.append(time)
        return result