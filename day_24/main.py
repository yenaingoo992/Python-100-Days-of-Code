file = open("file.txt")
contents = file.read()
print(contents)
file.close()

# without closing manually
with open("file.txt") as file:
    contents = file.read()
    print(contents)

# to edit file, must change mode as w,
# this will erase all the contents and will write the new ones
# in the w mode, if the file doesn't exist, it will create one
with open("new_file.txt", mode="w") as file:
    file.write("This is the new one")
    contents = file.read()
    print(contents)
