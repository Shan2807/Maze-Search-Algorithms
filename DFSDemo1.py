
from pyamaze1 import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(10,30) # Change to any size
    m.CreateMaze(loopPercent=100) 
    dSeacrh,dfsPath,fwdPath=DFS(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)
    
    m.tracePath({a:dSeacrh},delay=100)
    m.tracePath({b:dfsPath},delay=100)
    m.tracePath({c:fwdPath},delay=100)
    
    l=textLabel(m,'DFS Path Length',len(fwdPath)+1)
    l=textLabel(m,'DFS Search Length',len(dSeacrh)+1)
    
    m.run()

   

    # m=maze()
    # m.CreateMaze(loadMaze='demo.csv')

    # dSeacrh,dfsPath,fwdPath=DFS(m)

    # a=agent(m,footprints=True,shape='square',color=COLOR.green)
    # b=agent(m,1,1,goal=(5,5),footprints=True,filled=True,color=COLOR.cyan)
    # c=agent(m,footprints=True,color=COLOR.yellow)
    # m.tracePath({a:dSeacrh},showMarked=True)
    # m.tracePath({b:dfsPath})
    # m.tracePath({c:fwdPath})
    # m.run()