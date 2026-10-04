string=str(input( "Please enter a string "))
char=(input(" Please enter one character "))
i=0
count=0
while(i<len(string)):
    if (string[i]==char):
        count = count + 1
    i=i+1
print("The total number of times  " ,char,"Has occured  =" ,count)


