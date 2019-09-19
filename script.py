#Akshar Amin
#This code is to be used for train clearance tests. This code will generate the outer most points in a data set to insure clearance.

import csv
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

#Extracting data from csv
points = []
with open('data.csv') as csvfile:   #Opening CSV
    readCSV = csv.reader(csvfile, delimiter = ',')

    for row in readCSV:             #Iterating each line of the CSV
        number = row[0]
        y1 = row[3]
        z1 = row[4]
        y2 = row[5]
        z2 = row[6]
        if y1=='' or y1 == 'Y1':    #Remove extra lines in code
            continue

        points.append([float(y1), float(z1)])
        points.append([float(y2), float(z2)])

    pointsx = [i[0] for i in points]    #Splitting x and y values
    pointsy = [i[1] for i in points]
    hull = ConvexHull(points)           #Running the ConvexHull module

#Generating hull points
    print('Coordinates for Clearance:')
    for i in hull.vertices:             #Printing the outermost coordinates
        print(points[i])

#Graphing data
    plt.plot(pointsx, pointsy, 'o')     #Outputting a graph that displays the outer clearance.
    for simplex in hull.simplices:
        a = simplex[0]
        b = simplex[1]
        list1 = [pointsx[a], pointsx[b]]
        list2 = [pointsy[a], pointsy[b]]
        plt.plot(list1, list2)
    plt.show()




