import csv
from types import new_class
with open('C:/class-python/class-104/height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    # csv.reader meathod reads and return to  the current row then moves too the next
    file_data=list(reader)

file_data.pop(0)
#print(file_data)

new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

#print(new_data)

n=len(new_data)
#print(n)

total=0
for x in new_data:
    total+=x

mean=total/n
print("mean of height on dataset is: "+str(mean))    
