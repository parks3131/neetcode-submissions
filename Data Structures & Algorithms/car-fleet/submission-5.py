class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = list(zip(position,speed))
        sorted_car = sorted(car,key = lambda x:x[0],reverse = True)
        car = sorted_car

        fleet,max_speed = 1,0
        for i in range(1,len(position)):
            max_speed = max(max_speed,(target-car[i-1][0])/car[i-1][1])
            if max_speed < (target-car[i][0])/car[i][1]  :
                fleet+=1
        return fleet
        