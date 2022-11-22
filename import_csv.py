import csv 

file = file = open("TitanicSurvival.csv","r")
data = list(csv.reader(file, delimiter= ","))
##last_element = data [len(data)-1]
file.close()

zimmer = data[-1] #assign last element 
zimmer[4] = ('1st') #change the 5th element 
zimmer.append('Good person') #combine element 
print(data[-1])
