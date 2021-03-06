# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r ** 2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and prints results in scientific notation to 2 decimals.


done = False


def force_o_gravity(m1, m2, r):
    force = 6.67e-11 * (m1 * m2) / r ** 2
    return force


while not done:
    try:
        m1 = float(input("enter mass one:"))
        m2 = float(input("enter mass two:"))
        r = float(input("enter the distance between objects:"))
        force = force_o_gravity(m1, m2, r)
        print("The force of gravity in Newtons is {:.2e}".format(force))
        done = True
    except ZeroDivisionError as e:
        print("input is not valid:", e)
        done = False
    except ValueError as e:
        print("input is not valid:", e)
        done = False


