import csv
import os
import time
category=input("your category:")
quota=input("HS/OS:")
pool=input("Male/Female:")
if pool.lower()=="male":
    pool="Gender-Neutral"
else:
    pool="Female-Only"
rank=int(input("your rank:"))
count=1
pref=[]
no=1
ans="yes"
found=False
enlist=[]
f=open("enlisted_institutes.txt","w")
print("(in josaa you need to select the specific branch too), here you dont need to do that. I'll show you all branch you get")
while ans.lower()=="yes":
    a=input("enter college name")
    pref.append(a)
    print(no,a)
    ans=input("want to select more?(yes/no)")
    no+=1
with open(os.getcwd()+'//dataset.csv') as file:
    csvFile = list(csv.reader(file))
    for i in pref:
        for j in csvFile:
            if i in j[0]:
                if quota.upper()==j[2]:
                    if category.upper()==j[3]:
                        if pool.lower()==j[4].lower():
                            if rank<=int(j[6]):
                                enlist.append(str(count)+"| "+j[0]+" | "+j[1]+" | "+j[2]+" | "+j[3]+"\n")
                                count+=1
                                found=True
            
if found==False:
    print("sorry no college alotted")
f.writelines(enlist)
f.close()
print("the name of institutes have been saved in a file[enlisted_institutes.txt] in this folder")
time.sleep(10)
