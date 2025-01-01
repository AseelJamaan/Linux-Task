## File Permission Changer Linux Task


![image alt](https://github.com/AseelJamaan/Linux-Task/blob/81c53236ba2d5cbe4efc87e2b057ca0de4ef3660/WhatsApp%20Image%202025-01-02%20at%2001.55.15_85fc8af5.jpg)


### File Permissions Overview:In Linux, file permissions are based on three main entities: owner, group, and others. Permissions include:

r (read): Allows viewing the file's content.

w (write): Allows modifying the file.

x (execute): Allows executing the file if it is a script or program.

Permissions are displayed in a 10-character string:

First character indicates the type:

d: Directory

-: Regular file

Next three characters are for owner's permissions (read, write, execute).

Next three characters are for group's permissions.

Last three characters are for others' permissions.

For example, rwxrwxr-x means:

Owner: rwx (read, write, execute)
Group: rwx (read, write, execute)
Others: r-x (read and execute)

![image alt](https://github.com/AseelJamaan/Linux-Task/blob/b439c03880ad7ca1b85f50b2af5bb562316166d7/File%20Permission%20Flowchart.png)

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
