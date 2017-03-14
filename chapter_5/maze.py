from chapter_5.sstack import *
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def mark(maze,  pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=' ')
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1]+dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=' ')
                return True
    return False
def print_path(end, pos, st):
    pass
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = LStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print_path(end, pos, st)
                    return
                if passable(maze, nextp):
                    st.push((pos,i+1))
                    mark(maze, nextp)
                    st.push((nextp, 0))
                    break
    print('No path found.')

