from pygame import Vector2
import random

class GoLModel:

    def __init__(self,w,h):
        self._width = w + 2
        self._height = h + 2
        self._grid = [[0] * self._width for i in range(self._height)]
        self.randomCell()
    

    def update(self):
        pass    

    def randomCell(self):
        for i in range(1, self._width - 1):
            for j in range(1, self._height -1):
                rand = random.randrange(10)
                if rand > 7:
                    self._grid[j][i] = 1
                else:
                    self._grid[j][i] = 0


    def neighbors(self, y, x):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                count += self._grid[j][i]
        count -= self._grid[y][x]
        return count
    
    def DeadOrAlive(self):
        next = [[0] * self._width for i in range(self._height)]
        for x in range(1, self._width - 1):
            for y in range(1, self._height-1):
                count = self.neighbors(y,x)
                if self._grid[y][x] == 1 and 2<=count<=3:
                    next[y][x] = 1
                elif self._grid[y][x] == 0 and count == 3:
                    next[y][x] = 1
                elif self._grid[y][x] == 1 and 0<=count<=1:
                    next[y][x] = 0
                    
        self._grid = next
    
    def getSize(self):
        return self._width,self._height

    def getGrid(self):
        return [self._grid[i][1:-1] for i in range(1,self._height - 1)]
    
    def toggle(self):
        pass



if __name__ == '__main__':
    m = GoLModel(10,10)
    m._grid[2][2] = 1
    m._grid[2][3] = 1
    m._grid[2][4] = 1
    for r in m._grid:
        print(r)
    print()
    m.DeadOrAlive()
    for r in m._grid:
        print(r)
class Cell:
    def __init__(self):
        '''
        Class holding init status of cell (dead).
        Ability to set- and fetch new statuses with functions
        '''
        self._status = 'Dead'

    def set_dead(self):
        '''
        method sets the cell status to DEAD
        '''
        self._status = 'Dead'

    def set_alive(self):
        '''
        method sets the cell status to ALIVE
        '''
        self._status = 'Alive'

    def is_alive(self):
        '''
        method checks if the cell is ALIVE
        returns True if it is alive, False if not.
        '''
        if self._status == 'Alive':
            return True
        return False

    def get_print_character(self):
        '''
        method returning a status character of our choice to print on the board
        '''
        if self.is_alive():
            return 'O'
        return '.'

