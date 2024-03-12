import os.path
rover_count = 2
direction = ['N', 'E', 'S', 'W']
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
instructions = {'L': 'tleft', 'R': 'tright', 'M': 'move'}

class Rover:

    def __init__(self, x, y, xmax, ymax, position, intersection):
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.position = position
        self.intersection = set(intersection)

    def tright(self):
        self.position = direction[(direction.index(self.position) + 1) % len(direction)]

    def tleft(self):
        self.position = direction[(direction.index(self.position) - 1) % len(direction)]

    def move(self):
        xmod = self.x + move[self.position][0]
        ymod = self.y + move[self.position][1]
        if (xmod, ymod) not in self.intersection:
            if xmod <= self.xmax and xmod >= 0:
                self.x = xmod
            if ymod <= self.ymax and ymod >= 0:
                self.y = ymod
            else:
                print('Out of bounds, please try again!!')
                exit()
        else:
            print('rovers cannot occupy the same spot, try again!!')
            exit()


if __name__ == '__main__':
    auto = input('manual override or auto? Enter (A | auto) or (M | manual)\n')
    if auto in ['A', 'auto']:
        file = input('Select file name(make sure file is in this directory):\n')
        if os.path.exists(file):
            intersection = set([])
            data = []
            num_lines = sum(1 for line in open(file)) - 1
            rover_count = int(num_lines / 2)
            for line in open(file):
                data.append(line.rstrip())
            xmax, ymax = map(int, data[0].split())
            intersection = set([])
            results = []
            check_coords = []
            count_a = 1
            count_b = 2
            for _ in range(rover_count):
                x, y, position = data[count_a].split()
                count_a += 2
                if [x, y, position] not in check_coords:
                    check_coords.append([x, y, position])
                    rover = Rover(int(x), int(y), xmax, ymax, position, intersection)
                    for i in data[count_b]:
                        if i not in 'MRL':
                            print('invalid instruction "%s": use M or R or L - please try again' % i)
                            exit()
                        else:
                            getattr(rover, instructions[i])()
                    count_b += 2
                    intersection.add((rover.x, rover.y))
                    results.append((rover.x, rover.y, rover.position))
                else:
                    print('2 or more of your rovers share the same spot, please try again')
                    exit()
            for x, y, z in results:
                print(x, y, z)
        else:
            print('file does not exist, make sure file is in this directory)')
    elif auto in ['M', 'manual']:
        rover_count = int(input('How many rovers would you like to deploy?:'))
        xmax, ymax = map(int, input('Enter grid size:\n').split())
        intersection = set([])
        check_coords = []
        results = []
        count_a = 1
        count_b = 1
        for _ in range(rover_count):
            x, y, position = input('coordinates for rover %d:\n' % count_a).split()
            count_a += 1
            if [x, y, position] not in check_coords:
                check_coords.append([x, y, position])
                rover = Rover(int(x), int(y), xmax, ymax, position, intersection)
                for i in input('instructions for rover %d:\n' % count_b):
                    if i not in 'MRL':
                        print('invalid instruction "%s": use M or R or L - please try again' % i)
                        exit()
                    else:
                        getattr(rover, instructions[i])()
                count_b += 1
                intersection.add((rover.x, rover.y))
                results.append((rover.x, rover.y, rover.position))
            else:
                print('2 or more of your rovers share the same spot, please try again')
                exit()
        for x, y, z in results:
            print(x, y, z)
    else:
        print('Are you sure you typed the correct choice? Enter (A | auto) or (M | manual)')
        exit()
