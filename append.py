#First open the file in append mode
text_file=open("olympic_games.txt", "a")

# Now we add the winter games host to the file
text_file.write("\n\nWinter Olympics\n")
text_file.write("Lace Placid 1932, 1980\n")
text_file.write("Innsbruck 1964, 1976\n")
text_file.write("St. Moritz 1928, 1948\n")

#Now close the file
text_file.close()
