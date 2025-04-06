def modify_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Generate a new filename for the modified file
    new_filename = "modified_" + filename
    
    try:
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified file has been saved as '{new_filename}'.")
    except IOError:
        print(f"Error: The file '{new_filename}' could not be written.")
        
if __name__ == "__main__":
    main()
