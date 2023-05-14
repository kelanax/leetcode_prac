'''

PROBLEM: 

You need to find the minimum number of refueling stops that a car needs to make to cover 
a distance, target. For simplicity, assume that the car has to travel from west to east 
in a straight line. There are various fuel stations on the way that are represented as 
a 2-D array of stations, i.e., stations[i] =[d i ​ ,f i ​ ] , where  i ​ is the 
distance (in miles) of the i th gas station from the starting position, and i ​ is the 
amount of fuel (in liters) that it stores. Initially, the car starts with k liters of fuel. 

The car consumes one liter of fuel for every mile traveled. Upon reaching a gas station, 
the car can stop and refuel using all the petrol stored at the station. In case it cannot 
reach the target, the program simply returns − 1 −1 . 

Note: If the car reaches a station with 0 0 fuel left, it can refuel from that station, 
and all the fuel from that station can be transferred to the car. If the car reaches the 
target with 0 0 fuel left, it is still considered to have arrived.

---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''




import heapq

def min_refuel_stops(target, start_fuel, stations): 

    if start_fuel >= target or not stations : return 0

    max_heap = []
    num_stops = 0

    max_dist = start_fuel
    station = 0

    while max_dist < target :

        j = station
        for i in range(station, len(stations)) :
            if stations[i][0] <= max_dist :
                fuel_gained = stations[i][1]
                heapq.heappush(max_heap, -fuel_gained)
                j += 1
            station = j

        if max_heap : 
            max_dist = max_dist + (-heapq.heappop(max_heap))
            num_stops += 1
        else : return -1

    return num_stops












