print("Writing to a text file with the write() method")

#Open the file in write mode
text_file=open("olympic_games.txt", "w")

text_file.write("This is Line 1\n")
text_file.write("Here is a list of multiple olumpic games \n")
text_file.write("London 1908, 1948, 2012 \n")
text_file.write("Athens 1896, 2004 \n")
text_file.write("Paris 1900, 1924 \n")
text_file.write("Los Angeles 1932, 1984 \n")


text_file.close()
