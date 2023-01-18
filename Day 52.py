# Lambda function.

def double(x):
    return x*2

# We can also write like this using lambda function.
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2

def random(fx,value):
    return 5+fx(value)

print(double(50))
print(cube(50))
print(avg(50,100))

# We can also pass function as argument.
print(random(cube,3))