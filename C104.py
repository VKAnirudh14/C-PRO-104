from collections import Counter
import csv 
with open('C 104.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader) 

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

#Getting The Mean Of An Array
n=len(newData)
total=0
for x in newData:
    total=total+x

mean=total/n
print("Mean Average Is "+str(mean))

#Getting The Median Of An Array
newData.sort()
if n%2==0:
    m1=float(newData[n//2])
    m2=float(newData[n//2-1])
    median=(m1+m2)/2
else:
    median=newData[n//2]

print("Length Of An Array "+str(n))
print("Median Is "+str(median))

#Getting The Moded Of An Array
data=Counter(newData)
modeData={
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurrence in data.items():
    if 50<float(height)<60:
        modeData["50-60"]+=occurrence
    elif 60<float(height)<70:
        modeData["60-70"]+=occurrence
    elif 70<float(height)<80:
        modeData["70-80"]+=occurrence

mode_range,mode_occurrence=0,0
for range,occurrence in modeData.items():
    if occurrence>mode_occurrence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode Is {mode:2f}")    
