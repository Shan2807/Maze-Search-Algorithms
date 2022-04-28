from BFSdemo import BFS
from astardemo import aStar
from DFSDemo1 import DFS
from pyamaze1 import maze,agent,COLOR,textLabel
from timeit import timeit

myMaze=maze(20,30)
myMaze.CreateMaze(loopPercent=50)
# myMaze.CreateMaze()
searchPath,aPath,fwdPath=aStar(myMaze)
bSearch,bfsPath,fwdBFSPath=BFS(myMaze)
searchPath,dfsPath,fwdDFSPath=DFS(myMaze)

l=textLabel(myMaze,'A-Star PLength',len(fwdPath)+1)
l=textLabel(myMaze,'BFS PLength',len(fwdBFSPath)+1)
textLabel(myMaze,'DFS PLength',len(fwdDFSPath)+1)
l=textLabel(myMaze,'A-Star SLength',len(searchPath))
l=textLabel(myMaze,'BFS SLength',len(bSearch)+1)
l=textLabel(myMaze,'DFS SLength',len(searchPath)+1)

a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
b=agent(myMaze,footprints=True,color=COLOR.yellow)
c=agent(myMaze,footprints=True,color=COLOR.red,filled=False)
myMaze.tracePath({a:fwdBFSPath},delay=100)
myMaze.tracePath({b:fwdPath},delay=100)
myMaze.tracePath({c:fwdDFSPath},delay=100)

t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
t3=timeit(stmt='DFS(myMaze)',number=10,globals=globals())
t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())

textLabel(myMaze,'T1',t1)
textLabel(myMaze,'T2',t2)
textLabel(myMaze,'T3',t3)

# textLabel(myMaze,'Time for A-Star Maze',t1)
# textLabel(myMaze,'Time for BFS Maze',t2)
# textLabel(myMaze,'Time for DFS Maze',t3)


myMaze.run()