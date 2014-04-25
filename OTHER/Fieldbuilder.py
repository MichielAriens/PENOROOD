import itertools
import random
import sys

#width and height of the field
width = 11
height = 13
colors = ['R', 'G', 'B', 'Y', 'W']
shapes = ['R', 'S', 'C', 'H']

colorshape_permutations = list(itertools.product(colors, shapes))

figure_number = {}
for figure in colorshape_permutations:
    figure_number[figure] = 10
    figure_number['WS'] = 8
    figure_number['BS'] = 5
    figure_number['RS'] = 8
    figure_number['YS'] = 8
    figure_number['GS'] = 9
    figure_number['WR'] = 7
    figure_number['BR'] = 9
    figure_number['RR'] = 10
    figure_number['YR'] = 8
    figure_number['GR'] = 10
    figure_number['WC'] = 9
    figure_number['BC'] = 10
    figure_number['RC'] = 7
    figure_number['YC'] = 10
    figure_number['GC'] = 8
    figure_number['WH'] = 8
    figure_number['BH'] = 9
    figure_number['RH'] = 8
    figure_number['YH'] = 8
    figure_number['GH'] = 10

class Point():

    #X is the position on the horizontal axis
    #Y is the position on the vertical axis
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []
        self.colorshape = ()
        self.inTriangle = False
        

#points is a dictionary with the position as key and the point as value
points = {}

#Make points:
#Width and height are the sizes of the field.
def build_points():
    for i in range(0, width):
        for j in range(0, height):
            point = Point(i,j)
            points[(i,j)] = point

#Lay links between neighbours
def link():
    couples = []
    #For points with even y: the neighbours are (x-1, y+1),(x, y+1), (x+1, y)
    #For points with uneven y: the neighbours are (x, y+1),(x+1, y+1), (x+1, y)
    #these are only 3 because the rest will have been linked already
    for j in range (0, height):
        for i in range(0, width):
            current_point = points[(i,j)]
            if j%2 == 0:
                try:
                    current_point.neighbours.append(points[(i-1,j+1)])
                    points[(i-1,j+1)].neighbours.append(current_point)
                    couples.append((current_point, points[(i-1,j+1)]))
                except KeyError:
                    pass
                try:
                    current_point.neighbours.append(points[(i,j+1)])
                    points[(i,j+1)].neighbours.append(current_point)
                    couples.append((current_point, points[(i,j+1)]))
                except KeyError:
                    pass
                try:
                    current_point.neighbours.append(points[(i+1, j)])
                    points[(i+1, j)].neighbours.append(current_point)
                    couples.append((current_point, points[(i+1, j)]))
                except KeyError:
                    pass

            if j%2 == 1:
                try:
                    current_point.neighbours.append(points[(i,j+1)])
                    points[(i,j+1)].neighbours.append(current_point)
                    couples.append((current_point, points[(i,j+1)]))
                except KeyError:
                    pass
                try:
                    current_point.neighbours.append(points[(i+1,j+1)])
                    points[(i+1,j+1)].neighbours.append(current_point)
                    couples.append((current_point, points[(i+1,j+1)]))
                except KeyError:
                    pass
                try:
                    current_point.neighbours.append(points[(i+1, j)])
                    points[(i+1, j)].neighbours.append(current_point)
                    couples.append((current_point, points[(i+1, j)]))
                except KeyError:
                    pass
#Make triangles:
triangles = []
#Add first triangle to get started.
#This function builds the field too
def build_triangles():
    triangles.append((points[(0,0)], points[(0,1)], points[(1,0)]))
    points[(0,0)].inTriangle = True
    points[(0,1)].inTriangle = True
    points[(1,0)].inTriangle = True

    points[(0,0)].colorshape = ('R','R')
    points[(0,1)].colorshape = ('R','S')
    points[(1,0)].colorshape = ('R','C')
    
    for triangle in triangles:
        
        for point in triangle[0].neighbours:
            if point in triangle[1].neighbours and not point.inTriangle:
                add_triangle(triangle[0], triangle[1], point)

        for point in triangle[1].neighbours:
            if point in triangle[2].neighbours and not point.inTriangle:
                add_triangle(triangle[1], triangle[2], point)

        for point in triangle[2].neighbours:
            if point in triangle[0].neighbours and not point.inTriangle:
                add_triangle(triangle[2], triangle[0], point)
    #We have to check if any points were left out, algorithm is flawed...
    for k, point in points.items():
        if not point.inTriangle:
            #Check it's neighbours.
            for check_point1 in point.neighbours:
                for check_point2 in point.neighbours:
                    if check_point1 in check_point2.neighbours:
                        add_triangle(check_point1, check_point2, point)

def add_triangle(a, b, c):
    triangles.append((a,b,c))
    a.inTriangle = True
    b.inTriangle = True
    c.inTriangle = True
    define_triangle(triangles[-1])

def define_triangle(new_triangle):
    for point in new_triangle:
        if point.colorshape == ():
            random.shuffle(colorshape_permutations) #This is to vary the field.
            for colorshape in colorshape_permutations:
                valid = True
                point.colorshape = colorshape
                
                for triangle_point in new_triangle:
                    if triangle_point.colorshape == colorshape and triangle_point != point:
                        print triangle_point.colorshape + colorshape
                        valid = False
                        break
                if not valid:
                    continue

                    
                #checks if the permutations appear in the field anywhere else
                triangle_permutations = list(itertools.permutations([new_triangle[0].colorshape, new_triangle[1].colorshape, new_triangle[2].colorshape]))
                for perm in triangle_permutations:
                    
                    for triangle in triangles:
                        if perm == (triangle[0].colorshape, triangle[1].colorshape, triangle[2].colorshape) and point not in triangle:
                            valid = False
                            break
                    if not valid:
                        break
                if figure_number[colorshape] != 0:
                    figure_number[colorshape] -= 1
                else:
                    valid = False
                
                #stop execution and break out of the loop
                if valid:
                    return
                            
build_points()
link()
build_triangles()

#Write to text file
output = open("field.txt", "w")
for j in range(0, height):
    for i in range(0, width):
        point = points[(i,j)]
        point_string = point.colorshape[0] + point.colorshape[1]
        if i < width - 1:
            output.write(point_string + ',')
        else:
            output.write(point_string)
    output.write('\n')
output.close()
        

