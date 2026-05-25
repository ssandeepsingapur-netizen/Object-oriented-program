try:
    file = open('file.py', mode = 'w')
    file.write("Hello, World!")
    file.close()
    print("saved successfully")
except FileNotFoundError:
    print("file2.txt file not found")
