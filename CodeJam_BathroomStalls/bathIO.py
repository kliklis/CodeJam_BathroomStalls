import os.path

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start



#opens the input file (file must be in the same dir)
fname = input("File name:")
if not os.path.exists(fname):
    input("File not found.Press [Enter] to abort...")
    quit()
f = open(fname,"r")

str = f.read()

#reads number of cases
number_of_cases=int(str[:str.index('\n')])
    
#a list whith the num. of every case
cases=range(1, int(number_of_cases)+1)

#the array for the input data
data = []
dataBuf = []
Ndata = []
Kdata = []

print("Number of Cases:",number_of_cases)
start=str.index('\n')+1
end=find_nth(str,'\n',2)

#number of \n
i=3
                #basic loop
for c in cases:
    data.append(str[start:end])
    print('Case #',c,': ', sep="")
    print(str[start:end])
    start=end+1
    end=find_nth(str,'\n',i)
    i=i+1

#separates Ns from Ks
for d in data:
    dataBuf.append(d.split(" "))
data.clear()

#gets 2 arrays with Ns and Ks respectively
a=0
while a<number_of_cases:
    b=0
    while b<2:
        if(b==0):
            Ndata.append(int(dataBuf[a][b]))
        elif(b==1):
            Kdata.append(int(dataBuf[a][b]))
        b=b+1
    a=a+1






                #end of basic loop
    
#closes the f file
f.close()

wait = input("PRESS ENTER TO EXIT.")
