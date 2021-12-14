import sys
class game:
    def __init__(self,level):
        with open(level) as l:
            pattern =l.read()
        #cheack player and goal
        if pattern.count('p') != 1 :
            raise Exception("game should have PLAYER!")
        if pattern .count('g') != 1 :
            raise Exception("game should have GOAL!")

        #finding frame
        pattern = pattern.splitlines()
        self.height = len(pattern)
        self.width = max(len(line) for line in pattern)
        

        #definig   walls Player Water Crate Goal BG
        self.walls=[]
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if pattern[i][j] == "p":
                        self.start = (i, j)
                        row.append(False)
                    elif pattern[i][j] == "g":
                        self.goal = (i, j)
                        row.append(False)
                        '''
                    elif pattern[i][j] == "w":
                        self.water = (i, j)
                        row.append(False)
                        '''
                    elif pattern[i][j] == ".":
                        
                        row.append(False)
                        
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        
        self.sol = None

    def print(self):
        solut = self.sol[1] if self.sol is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("P", end="")
                elif (i, j) == self.goal:
                    print("G", end="")
                    '''
                elif (i, j)  == self.water:
                    print("░",end="") 
                    '''
                
                #elif sol is not None and (i, j) in sol:
                    #print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()
