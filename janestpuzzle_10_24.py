
#Solution to Jane St Puzzle "Knight Moves 6"

#Part 1: Generating the set of valid paths a knight can make from any start square target square on a chessboard
def is_valid_move(x, y, board_size):
    return 0 <= x < board_size and 0 <= y < board_size

def knight_moves(): #valid knight moves
    return [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

def find_paths(current_pos, target_pos, path, all_paths, board_size, max_steps):
    # If the current position is the target position and the path length is within max steps
    if current_pos == target_pos and len(path) <= max_steps:
        all_paths.append(path.copy())
        return
    
    # If the path has reached the maximum allowed steps, return
    if len(path) >= max_steps:
        return

    # Explore all knight moves
    x, y = current_pos
    for move in knight_moves():
        next_x, next_y = x + move[0], y + move[1]
        
        # Check if the next move is valid and not already in the path
        if is_valid_move(next_x, next_y, board_size) and (next_x, next_y) not in path:
            path.append((next_x, next_y))  # Add the move to the path
            find_paths((next_x, next_y), target_pos, path, all_paths, board_size, max_steps)  # Recur
            path.pop()  # Backtrack

def generate_knight_paths():
    board_size = 6 #configureable, 6 chosen as the question specifies
    start_pos = (0, 0)  # a1
    target_pos = (5, 5)  # f6
    all_paths = []
    path = [start_pos]  # Start path with the initial position
    max_steps = 10  # Maximum steps capped at 10 for computing power reasons. To minimize a+b+c, this may need to be changed.
    find_paths(start_pos, target_pos, path, all_paths, board_size, max_steps)
    return all_paths
paths=generate_knight_paths()
#matrix is 2d matrix representing the chessboard given in the question
matrix = [["a","a","a","a","a","a"],["a","a","a","a","b","b"],["a","a","b","b","b","b"],["b","b","b","b","c","c"],["b","b","c","c","c","c"],["c","c","c","c","c","c"]];

track="a" #tracks the letter from the previous step in path
track2="" #tracks the letter from the current step in path
i=0 #tracks the step position in the path 
j=0 #used to match up the preprogrammed matrix from the question with the set of all knight moves
k=1 #used to match up the preprogrammed matrix from the question with the set of all knight moves
capa=0 #capital a
capb=0 #capital b
capc=0 #capital c
x=0 #tracks the path position in the set of all paths, capped at 1000 for computing power purposes.
fin=capa #running total of sum
while capc<3:
    while capb<11:
        while capa<11: #3 while loops feeding in different variables for a, b and c until conditions satisfied
            while x<1000: #while loop feeding in the set of all knight paths into the question matrix
                
                curpath=paths[x] #curpath = the current path being analysed from the set of all paths
                while i<len(curpath): #while loop calculating the sum for each path
                    j=curpath[i][0]
                    k=curpath[i][1]
                    track2=matrix[j][k]
                    if track2=="a" and track=="a": #conditions laid out in the question
                        fin=fin+capa
                    elif track2=="b" and track=="a":
                        fin=fin*capb
                    elif track2=="c" and track=="a":
                        fin=fin*capc
                    elif track2=="b" and track=="b":
                        fin=fin+capb
                    elif track2=="a" and track=="b":
                        fin=fin*capa
                    elif track2=="c" and track=="b":
                        fin=fin*capc
                    elif track2=="c" and track=="c":
                        fin=fin+capc
                    elif track2=="b" and track=="c":
                        fin=fin*capb
                    elif track2=="a" and track=="c":
                        fin=fin*capa
                    
                    track=track2
                    i=i+1
                if fin==2024:  #prints the path, and values for a, b, c for all valid pairs
                        print(curpath)
                        print(capa)
                        print(capb)
                        print(capc)
                        print("     ")
                track2=""
                track="a"
                x=x+1
                i=0
                fin=0
            capa=capa+1
            x=0
        capa=0
        capb=capb+1
    capb=0
    capc=capc+1
print(fin)


