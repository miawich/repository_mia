# exceptions

# exception - a condition that results in an abnormal program flow
# exception handling - what we actively do to accommodate

x = 2
y = 0
# divide by zero

try:
    print(x / y)
except:
    print("infinity")

try:
    int("T")
except:
    print("number is not valid")

done = False

while not done:
    try:
        user_input = int(input("Enter an integer:"))
        done = True
    except:
        print("Number is not valid")


try:
    file = open("AliceInWonderland.txt")
except:
    print("cannot open file")


# built in error types for python to check what error occurred
try:
    #  my_file = ("myfile.txt")
    int("hello")
except FileNotFoundError:
    print("file not found")
except ValueError as e:
    print("Invalid conversion")
    print(e)
except ZeroDivisionError as e:
    print("error:", e)


# formatting numbers
import random
# round function round(n, digits)

print(round(3.14159265, 2))

# format method(string method)
a = 2345676548908
b = 34565437578885.5633
print("my number is {}".format(a))  # is the formatted number "a"
print("my number is {:.3f}".format(b))
print("my number are {} and {}".format(a, b))  # places them sequentially unless otherwise specified
print("my number are {1:.3f} and {0: ,}".format(a, b))  # otherwise specified

# oder:spaceholder+justification+width+commas+precision+datatype+notation

# fixed width
for i in range(20):
    c = random.randrange(10000)
    print("{:5}".format(c))

# justification ^ center <left right>
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:^12}".format(c))

# add commas
for i in range(20):
    c = random.random()
    print("{:12,}".format(c))

# precision(f for float, d for decimal, b for binary)
for i in range(20):
    c = random.random()
    print("{:11.5f}".format(c))

# scientific notation
# add commas
for i in range(20):
    c = random.random()
    print("{:.2e}".format(c))  # scinot to two decimal places
