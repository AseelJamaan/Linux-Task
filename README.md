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

![image alt](https://github.com/AseelJamaan/Linux-Task/blob/b48dd0652407bf2be4513676fd4cbc613e85bc3d/File%20Permission%20Flowchart%20(1).png)

### Flowchart
The process is as follows:

Start:

The process begins by initializing the program to analyze a permission string and determine its type and numeric representation.


Input Permission String:

The user provides a permission string (e.g., drwxr-xr-- or -rw-rw-r--) which represents the type and access permissions for a file or directory in Linux.


Determine Type (File or Directory):

The program examines the first character of the string:

If it’s d, the process identifies it as a directory.

If it’s -, the process identifies it as a file.

Extract the 9 Permission Characters:
After identifying the type, the process focuses on the next 9 characters of the string, which indicate the permissions for the:


Owner (first 3 characters).

Group (next 3 characters).

Others (last 3 characters).

Split Into 3 Permission Groups:

The process separates these 9 characters into the three groups:

Owner: Example, rwx.

Group: Example, r-x.

Others: Example, r--.

Map Permissions to Numeric Values:

Each group is converted to a numeric value using the rules:

r = 4 (read).

w = 2 (write).

x = 1 (execute).

- = 0 (no permission).
- 
For example:

Owner (rwx) = 4 + 2 + 1 = 7.

Group (r-x) = 4 + 0 + 1 = 5.

Others (r--) = 4 + 0 + 0 = 4.

Combine Numeric Values:

The process combines the numeric values from the three groups into a single number:

Example: Owner: 7, Group: 5, Others: 4 → 754.

Output Numeric Representation:

The process outputs the numeric equivalent of the permission string (e.g., Permissions: 754).

End:

The process is complete, and the program terminates.

### Python Code Explanation
Input: The user enters a permission string and the filename.

Validation: The script checks if the permission string contains only valid characters (r, w, x, -), and if the length is exactly 9 characters.

Convert to Numeric Format: The valid permission string is converted to a numeric value (e.g., rwxrwxr-x → 775).

Change Permissions: The script applies the new permissions to the file using the os.chmod() function.


### How to Use
Clone or download this repository.

Run the script and provide the file name and permission string when prompted.

The script will check if the permission string is valid and change the file permissions if valid.
