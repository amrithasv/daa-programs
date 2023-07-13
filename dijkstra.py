def dijsktra(graph,start):
    distances={node:float('inf') for node in graph}
    distances[start]=0
    heap=[(0,start)]
    while heap:
        current_dist,current_node=heapq.heappop(heap)
        if current_dist>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node].items():
            distance=current_dist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
    return distances
def find_optimal_route(graph,start,destination):
    distances= dijsktra(graph,start)
    if distances[destination]==float('inf'):
        return None
    route=[]
    node=destination
    while node!=start:
        route.append(node)
        neighbors=graph[node]
        min_distance=float('inf')
        next_node=None
        for neighbor,weight in neighbors.item():
            if distances[neighbor]+weight==distances[node]and distances[neighbor]<min_distance:
                min_distance=distances[neighbor]
                next_node=neighbor
                if next_node is None or next_node in route:
                    return None
                node=next_node
    route.append(start)
    route.reverse()
    return route
graph={
    'A':{'B':3,'C':99,'D':7,'E':99},
    'B':{'A':3,'C':4,'D':2,'E':99},
    'C':{'A':99,'B':4,'D':5,'E':6},
    'D':{'A':7,'B':2,'C':5,'E':4},
    'E':{'A':99,'B':99,'C':6 ,'D':4},


}
start_location='A'
destination_loaction='E'
optimal_route=find_optimal_route(graph,start_location,destination_loaction)
if optimal_route is None:
    print("No valid route from start to dest")
else:print("optimal route:",'->'.join(optimal_route))



    


