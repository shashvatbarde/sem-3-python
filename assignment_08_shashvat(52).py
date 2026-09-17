# Open input file in read mode
file = open("C:\\Users\\Lenovo\\Desktop\\APP\\input.txt", "r")
# Read all lines
lines = file.readlines()
# Count number of lines
count = len(lines)
# Extract first two lines
first_two = lines[:2]
# Open output file in write mode
output = open(r"C:\Users\Lenovo\Desktop\APP\output123.txt", "w")
# Write first two lines into output file
output.writelines(first_two)
# Close both files
file.close()
output.close()
# Display number of lines
print("Total number of lines:", count)
print("First two lines have been written to output.txt")