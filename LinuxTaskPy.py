import os

def set_permissions(filename):
    """
    Function to change the file permissions to rwxrwxr-x (775).
    """
    try:
        # Set permissions to rwxrwxr-x (775)
        os.chmod(filename, 0o775)
        print(f"Permissions for file '{filename}' have been successfully changed to rwxrwxr-x.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Take filename input from the user
    filename = input("Please enter the filename to change permissions: ")
    
    # Call the function to set permissions
    set_permissions(filename)
