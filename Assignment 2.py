f = input("Enter the Filename: ")
e = f.split(".")[-1]
if e == 'py':
    print("The extension of the file is : 'Python'")
elif e == 'c':
    print("The extension of the file is : 'C/C++'")
elif e == 'java':
    print("The extension of the file is : 'Java'")
elif e == 'cs':
    print("The extension of the file is : 'C#'")
elif e == 'PHP':
    print("The extension of the file is : 'PHP'")
elif e == 'swift':
    print("The extension of the file is : 'Swift'")
elif e == 'vb':
    print("The extension of the file is : 'Visual Basic'")
else:
    print("Filename Exception")
