even=[]
odd=[]
for i in range(1,21):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers from 1-20:", even)
print ("Odd numbers from 1-20:", odd)