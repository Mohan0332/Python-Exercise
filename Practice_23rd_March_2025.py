Year = 2019
month ='August'
res = f'The year is {Year} and the month is {month}' # Formatted String
print(res)

list = [5,2,5,2,2]
print(list.index(5))

#See what are magic methods

#UNPACKING
coordinates = (1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

x,y,z = coordinates #Does the same job as the previous 3 lines of code

a,b,c = coordinates

print(f'value of a and b are {a} , {b}.')