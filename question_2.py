text = ""

while True:
    text = input("Enter a string: ")
    if (list(text).count(" ") > 99):
        print("Invalid paragraph, too long, enter again")
    else:
        break

palindrom = ''
        
Words = text.split()
for x in Words:
    if (x.lower() == x[::-1].lower()):
        palindrom += x + " "
    
if (len(palindrom) == 0):
    print("No palindromic words found")
else:
    print("The palindromic words are: " + palindrom)
