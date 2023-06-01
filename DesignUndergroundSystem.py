from collections import defaultdict
from typing import DefaultDict


class UndergroundSystem:

    def __init__(self):
        #customerid: (timestart, startstation)
        self.i = defaultdict(tuple)

        #(start, end): timeend-timestart
        self.o = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime, startstation = self.i[id]
        total = t - starttime
        self.o[(startstation, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.o[startStation, endStation])/len(self.o[startStation, endStation])


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45,"Leyton",3)
obj.checkOut(45,"Waterloo",15)
obj.checkIn(27,"Leyton",10)
obj.checkOut(27,"Waterloo",20)
# (12 + 10) / 2 = 11.0
param_3 = obj.getAverageTime("Leyton","Waterloo")
print(param_3)