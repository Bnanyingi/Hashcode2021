def read_input(fileName):

    # Print data to console
    print("a.txt")
    print("b.txt")
    print("c.txt")
    print("d.txt")
    print("e.txt")
    print(fileName)
    print("f.txt")
    print("INPUT:")

    #  Read the open file by name
    inputFile = open(inputFilesDirectory + fileName)

    # first line
    firstLineData = inputFile.readline().split()
    seconds = firstLineData[0]
    intersections = firstLineData[1]
    num_streets = firstLineData[2]
    num_cars = firstLineData[3]
    points = firstLineData[4]

    # read streets
    streets_data = []
    i = int(num_streets)
    while i > 0:
        temp_street = inputFile.readline().split()
        streets_data.append(
            {
                "start": temp_street[0],
                "end": temp_street[1],
                "name": temp_street[2],
                "duration": temp_street[3]
            }
        )
        i -= 1
    print("streets data --------------->")
    print(streets_data)

    # read cars
    cars_data = []
    i = int(num_cars)
    while i > 0:
        temp_car = inputFile.readline().split()
        cars_data.append(
            {
                "total_streets": temp_car[0],
                "streets": temp_car[1:],
            }
        )
        i -= 1
    print("cars data --------------->")
    print(cars_data)

    inputFile.close()

    # # calculate car movement


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
inputFilesDirectory = "Input/"  # Location of input files
outputFilesDirectory = "Output/"  # Location of output files

fileNames = ["a.txt"]  # File names

for fileName in fileNames:  # Take each and every file and solve
    read_input(fileName)
