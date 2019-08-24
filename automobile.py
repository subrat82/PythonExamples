log="""0 93 manual
1 92.34 autonomous
2 91.92 autonomous
3 91.45 manual
4 90.853333333 autonomous
60 89.45333333 autonomous"""
automode = log.split("\n")
print(automode)

x=len(automode)
print(x)

count = 0;
batteryPercentage = 0;
avg = 0.0;
percentageDecrease = []
minutes=[]
size = 0.0;
total = 0.0;
print(range(len(automode)))
for i in range(len(automode)):

    if i < max(range(len(automode))):
        #i=[0,93,auto]
        y = automode[i].split(" ")
        z = automode[i+1].split(" ")
        print(y)
        print(z)
        batteryPercentage = y[1] #93

        if y[2] == 'manual' and z[2] == 'autonomous':
            size = float(y[1])-float(z[1])
            percentageDecrease.append(size)
            count += 1


for i in range(len(percentageDecrease)):
    total += percentageDecrease[i]


print(percentageDecrease)
print(count)
print(total)
avg = total/count
print("Average of battery percentage",round(avg, 7))



