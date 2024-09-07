#kathleen hambrick 012 sorter

num = input("enter 0's, 1's, and 2's ")
good=1
#check that what was entered is a number
try:
        ans=int(num)
except Exception as e:
        good=0
        print("invalid entry")

#create function
def sorter(list):
    list.sort() 

#test number entered
if good:
    for x in num:
        #print(x)
        x=int(x)
        if x < 0 or x > 2:
            print("only numbers of 0's, 1's, and 2's allowed")
            good=0
            break

#perform sort and print answer
if good:
    new_list=list(num)
    sorter(new_list)
    print(new_list)