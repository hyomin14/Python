a = "Life is too short, You need Python"
print(len(a))

#indexing
print(a[0])
print(a[3])
print(a[-1])
print(a[-5])

#slicing
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])       # 0 <= a < 4
print(a[5:7])
print(a[:17])
print(a[19:])
print(a[:])
print(a[19:-7])     #a[19] ~ a[-8]

#formatting
number = 10
day = 'three'
print("I ate %d apples, so i was sick for %s days." % (number, day))
print("I ate {0} apples, so i was sick for {1} days.".format(number, day))
print("I ate {0} apples, so i was sick for {day} days.".format(10, day=3))

print("%10s" % "hi")
print("%-10sjane." % "hi")
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:!<10}".format("hi"))

y=3.421342345
print("{0:10.4f}".format(y))
print("{{ and }}".format())

#3.6v
name = 'pey'
age = 30
print(f'My name is {name}. I am {age} years old.')
print(f'{"hi":<10}')

#function
print("\n")
b = "Life is too short"

print(b.count('i'))
print(b.find('t'))
print(b.find('q'))
print(b.index('t'))             #print(a.index('q'))

print(",".join('abcd'))

c = "Life Is Too Short"
print(c.upper())
print(c.lower())

d = " hi "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

print(b.replace("Life", "He"))

print(b.split())

