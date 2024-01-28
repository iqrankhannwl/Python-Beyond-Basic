from functools import partial

def power_1(base, exponent):
    return base ** exponent

def square(base):
    return power_1(base, 2)

def cube(base):
    return power_1(base, 3)

# ============ Example-01 =========

def power_2(base, exponent):
    return base ** exponent


square_1 = partial(power_2, exponent=2)
cube_1 = partial(power_2, exponent=3)
four_time = partial(power_2, exponent=4)

# print(f"sqaure : {square_1(5)} cube: {cube_1(5)} four_time: {four_time(5)}" )


# ============ Example-02 =========

power_3 = lambda base, exponent : base ** exponent
square_2 = partial(power_2, exponent=2)
# print(square_2(4))

# ============ Example-03 =========
square_2 = partial(lambda base, exponent : base ** exponent, exponent=2)
print(square_2(4))