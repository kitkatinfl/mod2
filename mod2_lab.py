# Kathleen Hambrick
# Program mod2_lab.py in Ktest
# Check students GPA for honor role or Dean's list levels

last_name=''
first_name=''
gpa=''

while last_name!='zzz':
    last_name = input('Last Name : ')

    #end program when zzz entered
    if last_name=='zzz':
        continue

    first_name = input('First Name : ')
    gpa = float(input('GPA :'))

    #check gpa for honor roll or deans list
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Deans list!")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll!")
    else:
        print(first_name + " " + last_name + " did not obtain an honor ranking")