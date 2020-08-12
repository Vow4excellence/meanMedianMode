import csv
with open('height-weight.csv',newline='') as f:
    #for reading the csv and storing data in a list
    reader = csv.reader(f)
    fileData = list(reader)
    #to sort data from file_data to get the list of height from it.
    #First  remove the title list from the data using pop()
    fileData.pop(0)
    # create a empty list named newData
    newData = []
    # a for loop on fileData to get the elements inside the nested lists and append them to the new_data list.
    for i in range(len(fileData)):
        Total = fileData[i][1]
        newData.append(float(Total))
#sorting data to get height f people and print fileData
#get mean
n= len(newData)
total = 0
for counter in newData:
    total += counter
mean = total / n
print("Mean / Average height is "+str(mean))