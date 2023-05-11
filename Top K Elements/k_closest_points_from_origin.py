'''

PROBLEM: 

Given a list of points on a plane, where the plane is a 2-D array with (x, y) coordinates, 
find the k closest points to the origin (0,0).

Note: Here, the distance between two points on a plane is the Euclidean distance: x2 + y2

------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''


from point import Point
import heapq

def k_closest(points, k):

    if k > len(points) : return points
  
    max_heap = []

    for i in range(k) : 

        heapq.heappush(max_heap, points[i])

    for i in range(k, len(points)) :
        dist1 = points[i].distance
        dist2 = max_heap[0].distance

        if (dist1 < dist2) :
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, points[i])
        
        
    
    
    return list(max_heap)







import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = (self.x**2) + (self.y**2)

    def distance_from_origin(self) :
        return (self.x**2) + (self.y**2)
    
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()
  
    # Write your code here




# OTHER: 


'''

from point import Point
import heapq

def k_closest(points, k):

    if k > len(points) : return list(points)
    # elif k == len(points) :
    #     return [[point.x, point.y] for point in points]
  
    max_heap = []

    for i in range(k) : 
        # print("distance:", points[i].distance )
        # print("point1 - x:", points[i].x, ", y:", points[i].y)

        heapq.heappush(max_heap, [points[i].distance_from_origin() , points[i].x,  points[i].y])

    for i in range(k, len(points)) :
        # dist1 = points[i].distance
        # dist2 = max_heap[0].distance
        dist1 = points[i].distance_from_origin()
        dist2 = max_heap[0][1].distance_from_origin()

        print("point1 - x:", points[i].x, ", y:", points[i].y, "point2 - x:",max_heap[0][1].x, ", y:", max_heap[0][1].x )
        if (dist1 < dist2) :
            heapq.heappop(max_heap)
            # heapq.heappush(max_heap, [points[i].distance_from_origin() , points[i]])
            
            heapq.heappush(max_heap, [points[i].distance_from_origin() , points[i].x,  points[i].y])
        
        
        
    # x = [[point[1].x, point[1].y] for point in max_heap]
    # print("x:", x)

    res = []
    for i in range(len(max_heap)) :
        pair = max_heap[i]
        x,y = pair[1].x, pair[1].y
        print("x:",x,", y:",y)
        res.append([x,y])

    
    return res
    # return list(max_heap)



'''





