import array


class Board:
    board_arr = None

    def __init__(self):
        self.board_arr = [[0 for x in range(8)] for y in range(8)]
        for x in range(len(self.board_arr)):
            i = 0
            for y in range(len(self.board_arr[x])):
                if x % 2 == 1:
                    temp = 2 * i + 1
                else:
                    temp = 2 * i
                if temp < len(self.board_arr[x]) and x < 3:
                    self.board_arr[x][temp] = 1
                elif temp < len(self.board_arr[x]) and x > 4:
                    self.board_arr[x][temp] = 2
                i += 1

    def display(self):
        z = 0
        print "  ",
        for i in range(8):
            z += 1
            print " " + str(z) + " ",
        print
        x = 1
        for row in self.board_arr:
            print str(x) + " ",
            x += 1
            for item in row:
                print "[" + str(item) + "]",
            print

    def handle_move(self, x, y, a, b, player):
        temp = self.board_arr[y][x]
        if temp == 0:
            return
        if abs(x - a) > 2 or abs(y - b) > 2:
            return
        if abs(x - a) == 2 and abs(y - b) == 2:
            if temp == 1:
                if self.board_arr[y+1][x+1] != 2 or self.board_arr[y+1][x-1] != 2:
                    return
            elif temp == 2:
                if self.board_arr[y-1][x+1] != 1 or self.board_arr[y-1][x-1] != 1:
                    return
            if self.board_arr[b][a] != 0:
                return
            else:
                self.board_arr[b][a] = player
                self.board_arr[y][x] = 0
                self.board_arr[y+(-(y-b)/2)][x+(-(x-a)/2)] = 0
        if abs(x - a) == 1 and abs(y - b) == 1:
            if self.board_arr[b][a] != 0:
                return
            else:
                self.board_arr[b][a] = player
                self.board_arr[y][x] = 0
        self.display()


board = Board()
board.display()
board.handle_move(0, 0, 1, 1, 1)
print
board.handle_move(0, 0, 2, 2, 1)
print
board.handle_move(2, 2, 4, 4, 1)
print
board.handle_move(2, 2, 3, 3, 1)
print
board.handle_move(3, 3, 4, 4, 1)
print
board.handle_move(5, 5, 3, 3, 2)
