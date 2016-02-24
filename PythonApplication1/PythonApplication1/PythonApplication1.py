import csv

#calculating the distance between the original coordinates and the coordinates of the pharmacy
def distance(apteka, x, y):
    res = ((float(apteka[2])-float(x))**2+(float(apteka[3])-float(y))**2)**0.5
    return res

#Input : file name , longitude, latitude
filename = input("Name of file: ")
x_coord = input("Longitude: ")
y_coord = input("Latitude ")

f = open(filename, 'r', encoding="UTF-8")

#read the first line - name of column in the file and the data on the first pharmacy
apteka1 = f.readline() 
apteka1 = f.readline()
apteka1 = apteka1.split('|')
apteka1.append(distance(apteka1,x_coord,y_coord))

#reading and generation of data on the second pharmacy
apteka2 = f.readline()
apteka2 = apteka2.split('|')
apteka2.append(distance(apteka2,x_coord,y_coord))

apteka3 = f.readline()
apteka3 = apteka3.split('|')
apteka3.append(distance(apteka3,x_coord,y_coord))

#Sort three pharmacies on the shortest distance 
if apteka3[4]<apteka1[4]:
    temp = apteka1
    apteka1 = apteka3
    apteka3 = temp
if apteka2[4]<apteka1[4]:
    temp = apteka1
    apteka1 = apteka2
    apteka2 = temp
if apteka3[4]<apteka2[4]:
    temp = apteka2
    apteka2 = apteka3
    apteka3 = temp

#read the next pharmacy in the file and if it is closer than the others , put it on the right place
apteka_new = f.readline()
while apteka_new:
    apteka_new = apteka_new.split('|')
    apteka_new.append(distance(apteka_new,x_coord,y_coord))

    if apteka_new[4]<apteka3[4]:
        if apteka_new[4]<apteka2[4]:
            if apteka_new[4]<apteka1[4]:
                apteka3 = apteka2
                apteka2 = apteka1
                apteka1 = apteka_new

            else:
                apteka3 = apteka2
                apteka2 = apteka_new
        else:
            apteka3 = apteka_new
    apteka_new = f.readline()
       
f.close()

#data of three nearest pharmacies
print('{0}|{1}'.format(apteka1[0], apteka1[1]))
print('{0}|{1}'.format(apteka2[0], apteka2[1]))
print('{0}|{1}'.format(apteka3[0], apteka3[1]))


