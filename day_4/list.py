# list creation
colors = ["Black", "White"]
print(colors)

# adding single item
colors.append("Rad")
print(colors)

# updating item
colors[2] = "Red"
print(colors)

# adding multiple items
colors.extend(["Green", "Blue", "Transparent"])
print(colors)

# removing color
colors.remove(colors[-1]) # removing the last item from the list
print(colors)

# accessing out of index can occur, index out of range error
# colors[100]

# range in a range
animes = ["Naruto", "Attack On Titan", "Demon Slayer"]
movies = ["Lord of the Rings","Harry Potter"]
favourites = [animes, movies]
print(favourites)