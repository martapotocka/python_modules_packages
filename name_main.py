print("I'm name_main, and I will be printed always")
print("My name is: {}".format(__name__))

if __name__ == '__main__':
    print("I was run directly")
else:
    print("I was imported")

# Now go to base_file.py, import me and see what happens
