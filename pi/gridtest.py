import grid as gridimp


def loadGrid(path):
        import csv
        with open(path) as f:
            data=[tuple(line) for line in csv.reader(f)]
        list = []
        emptyrow = []
        for i in range(len(data)):
            list.append(emptyrow)
            row = data[i]
            for j in range(len(row)):
                oldstr = row[j]
                newstr = oldstr.replace("'", " ")
                list[i].append(newstr)
        list[0] = str(list[0]).replace("'", "")
        list[0] = str(list[0]).replace(" ", "")
        list[0] = str(list[0]).replace(",", "=")
        list[0] = str(list[0]).lower()
        number_of_rows = len(data);
        number_of_columns = len(data[0])
        init_string = list[0]
        grid = gridimp.GRID(number_of_columns, number_of_rows)
        grid.initiate(init_string);
        return grid

grid = loadGrid("C:\Users\Michiel\Documents\GitHub\PENOROOD\OTHER\grid25-04.csv")
pos = grid.getPos([("ys",3,3),("rr",2,3),("gs",1,1)],needsSorting = True)

print str(pos)

pos = grid.getPos([("bc",0,0),("bc",0,0),("wr",0,0)])

print str(pos)
