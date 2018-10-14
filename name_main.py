print("I will be printed always")
print("My name is: {}".format(__name__))

if __name__ == '__main__':
    print("I was run directly")
else:
    print("I was imported")
