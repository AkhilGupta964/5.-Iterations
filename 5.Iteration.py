# while loop

n = 5
while n > 0:
    print(n)
    n = n - 1
    print('Blastoff!')

while True:
    line = input('> ')
    if line in ('done', 'Done'):
        break
    print(line)
print('Done!')

# continue and break

while True:
    line = input('> ')
    if line[0] == '#':
        continue # start loop from beginning with next tem in list
    if line == 'done':
        break # breaks out of the loop
    print(line)
print('Done!')

# finding prime number using loop and break

## random includes bracket values too while range excludes

for n in range(2, 10):
    for x in range(2, n): # range(2,2) doesnt exist
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: # used with for loop
        print(n, 'is a prime number')

# for loop

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

n = 0
a = ['akhil','suraj','sai','abhishek']
for name in a:
    n = n + 1
print (n)

p = len(a)
print (p)

# finding maximum
#[3, 41, 12, 9, 74, 15]

a = [3, -41, -12, -9, -74, -15]
c = None
for num in a:
    if c is None or c < num:
        c = num
print (c)

p = type(None)
# None is a special constant value which we can store
# in a variable to mark the variable as “empty”.
print(p)

# finding minimum
#[3, 41, 12, 9, 74, 15]

a = [-3, -41, -12, -9, -74, -15]
c = None
for num in a:
    if c is None or c > num:
        c = num
print (c)

for a in range(0,10,2): # start from 0 to 10 with interval of 2
    print (a)

# Quiz

largest = 0
smallest = 0
average = 0
count = 0
total = 0

x = None
y = None

while x != 'done' :
    num = input('Enter:')
    try:
        a = int(num)
        count = count + 1
        total = total + a
    except:
        if num == 'done':
            x = 'done'
        else:
            print('Invalid Input')


    av = total/count

    try:
        if x == None or a > x:
            largest = a
            x = a
    except:
        m = 3

    try:
        if y == None or a < y:
            smallest = a
            y = a
    except:
        m = 3

print ('Maximum is ',largest)
print ('Minimum is ',smallest)
average = total/count
print ('Count is %d, Total is %d, Average is %g' % (count, total, float(average)))
