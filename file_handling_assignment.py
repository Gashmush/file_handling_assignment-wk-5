file = open("my_file.txt", "w")
file.write("This is line 1.\n")
file.write("Line 2 with numbers: 12345.\n")
file.write("And this is line 3.\n")
file.close()
print("File 'my_file.txt' created and written successfully.")
file = open("my_file.txt", "r")
contents = file.read()
print("\nContents of my_file.txt:")
print(contents)
file.close()
file = open("my_file.txt", "a")
file.write("This is line 4.\n")
file.write("Line 5 with numbers: 67890.\n")
file.write("And this is line 6.\n")
file.close()

# Error handling

try:
    # Open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1.\n")
        file.write("Line 2 with numbers: 12345.\n")
        file.write("And this is line 3.\n")
    print("File 'my_file.txt' created and written successfully.")
    
    # Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file and display them on the console
        contents = file.read()
        print("\nContents of my_file.txt:")
        print(contents)
    
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4.\n")
        file.write("Line 5 with numbers: 67890.\n")
        file.write("And this is line 6.\n")
    print("\nThree additional lines appended to 'my_file.txt'.")
    
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Script execution completed.")
