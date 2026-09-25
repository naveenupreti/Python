# Python script to take multi-line input as a paragraph

print("Enter your paragraph (type 'END' on a new line to finish):")

paragraph = ""  # Initialize empty string to store paragraph

while True:
    line = input()       # Read a line from user
    if line == "END":    # Stop input if user types 'END'
        break
    paragraph += line + "\n"  # Add line to paragraph with newline

# Print the entered paragraph
print("\nYou entered the following paragraph:\n")
print(paragraph)
