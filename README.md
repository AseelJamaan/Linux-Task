## File Permission Changer Linux Task
### Flowchart
The process is as follows:
Input: The user provides a permission string .
Process: The permission string is split into three parts: Owner, Group, and Others.
Decision: The script checks if the permission string is valid.
Yes: If valid, it proceeds to the next step.
No: If invalid, an error message is displayed.
Convert: If the permission string is valid, it is converted into a numeric format (e.g., rwxrwxr-x → 775).
Execute: The chmod 775 filename command is executed to change the file permissions.
End: The process finishes.
### Python Code Explanation
Input: The user enters a permission string and the filename.
Validation: The script checks if the permission string contains only valid characters (r, w, x, -), and if the length is exactly 9 characters.
Convert to Numeric Format: The valid permission string is converted to a numeric value (e.g., rwxrwxr-x → 775).
Change Permissions: The script applies the new permissions to the file using the os.chmod() function.
### How to Use
Clone or download this repository.
Run the script and provide the file name and permission string when prompted.
The script will check if the permission string is valid and change the file permissions if valid.
