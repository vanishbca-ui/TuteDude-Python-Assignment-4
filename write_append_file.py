
data = input("Enter some text to write into the file: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

print("Data written successfully.")

append_data = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(append_data + "\n")
file.close()

print("Data appended successfully.")
print("\nFinal content of the file:")

file = open("output.txt", "r")
content = file.read()
print(content)

file.close()