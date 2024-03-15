
def read(layout):
    map = {'left': dict(), 'right': dict()}
    lines = layout.lower().split(' ')
    for y in range(len(lines)):
        line_length = len(lines[y])
        for x in range(line_length):
            if x < line_length / 2:
                map['left'][lines[y][x]] = (x,y)
            else:
                map['right'][lines[y][x]] = (x,y)
    return map
