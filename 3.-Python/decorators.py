def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

def announced(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper
    

@announce
def hello():
    print("Hello, world!")

hello()

@announced
def hi():
    print("Hi, world!")

hi()
""" Output:
About to run the function
Hello, world!
Done with the function
"""