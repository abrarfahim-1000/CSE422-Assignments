import heapq

def a_star(graph,heuristic,start,goal):
    pqueue=[]
    path={}
    visited = set()
    final_path=''
    heapq.heappush(pqueue,(heuristic[start],start,None,0))
    while pqueue:
        node=heapq.heappop(pqueue)
        path[node[1]]=node[2]
        visited.add(node[1])
        if node[1]==goal:
            tempPar=node[2]
            final_path=goal
            while tempPar!=None:
                final_path=tempPar+' -> '+final_path
                if tempPar not in path.keys():
                    return 'No path found'
                tempPar=path[tempPar]
            print(f'Path: {final_path}\nTotal distance: {node[3]} km')
            return
        nodename,gscore=node[1],node[3]
        for nd in graph[nodename]:
            if nd[0] not in visited:
                heapq.heappush(pqueue,(gscore+nd[1]+heuristic[nd[0]],nd[0],nodename,gscore+nd[1]))

with open('input.txt','r') as fin:
    file=fin.readlines()
    heuristic={}
    graph={}
    for i in file:
        line=i.strip().split(' ')
        heuristic[line[0]]=int(line[1])
        graph[line[0]]=[]
        length=len(line)
        k=2
        while k<length:
            graph[line[0]].append([line[k],int(line[k+1])])
            k+=2

a_star(graph,heuristic,'Arad','Bucharest')
