# File creation

try:
  # Open the file "my_file.txt" in write mode ('w')
  with open("my_file.txt", "w") as file:
    # Write three lines of text with a mix of strings and numbers
    file.write("This is the first line of text.\n")
    file.write("Here's a line with a number: 42\n")
    file.write("And a final line.\n")
    print("Successfully created and wrote to 'my_file.txt'.")

except FileNotFoundError:
  print("Error: File 'my_file.txt' not found.")

except PermissionError:
  print("Error: Insufficient permissions to write to the file.")

# File Reading and Display

try:
  # Open the file "my_file.txt" in read mode ('r')
  with open("my_file.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()
    # Display the contents on the console
    print("\nContents of 'my_file.txt':")
    print(contents)

except FileNotFoundError:
  print("Error: File 'my_file.txt' not found.")

# File Appending

try:
  # Open the file "my_file.txt" in append mode ('a')
  with open("my_file.txt", "a") as file:
    # Append three additional lines of text
    file.write("\nHere are some additional lines:\n")
    file.write("This is Line 4\n")
    file.write("This is Line 5\n")
    print("\nSuccessfully appended text to 'my_file.txt'.")

except PermissionError:
  print("Error: Insufficient permissions to append to the file.")

# Finally block (always executes)

finally:
  print("\nFile handling operations completed.")
