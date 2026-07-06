class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since the array is sorted already
        l,r = 0, len(numbers)-1

        while(l<r):
            sum_numbers = numbers[l]+numbers[r]
            if sum_numbers < target:
                l+=1
            elif sum_numbers > target :
                r-=1
            else :
                return [l+1,r+1]
        return []