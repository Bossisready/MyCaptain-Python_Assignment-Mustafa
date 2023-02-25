def most_frequent(string):
    string = string.lower()
    a = {}
    for char in string:
        if char.isalpha():
            if char in a:
                a[char] = a[char] + 1
            else:
                a[char] = 1
    sorted_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_a:
        print (item[0], ":", item[1])
                
        
freq = input("Enter a string ")    
most_frequent(freq)