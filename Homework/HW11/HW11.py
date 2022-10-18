#Task 1. Creating a geometric progression generator
def geometric_progression(start, ratio):
    n = 1
    while True:
        yield start * (ratio ** (n - 1))
        n += 1
        
start = float(input("start:"))
ratio = float(input("ratio:"))

geometric_gen = geometric_progression(start,ratio)

print(next(geometric_gen))
print(next(geometric_gen))
print(next(geometric_gen))
