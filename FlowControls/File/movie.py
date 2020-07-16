f=open("C:/Users/user/Downloads/movies.csv","r")
dict={}
i=0
for line in f:
    words=(line.rstrip("\n").split(","))
    #print(words)
    yr=words[2]
    if(yr not in dict):
        dict[yr]=1  
    else:
        dict[yr]+=1
    i+=1
    if(i==100):
        break
print(dict)
