# Given an array arr. Your task is to find the minimum and maximum elements in the array.
numberList=[]
n=int(input('Enter the count of elements in the array : '))
for i in range(n):
    element=int(input('Enter the integer element to add in the array : '))
    numberList.append(element)
# print(numberList)
min=numberList[0]
max=numberList[0]
for i in range(1,len(numberList)):
    if(min>numberList[i]):
        min=numberList[i]
    if(max<numberList[i]):
        max=numberList[i]
print("Maximum : ", max)
print("Minimum : ", min)
