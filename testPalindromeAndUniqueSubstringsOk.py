def isPalindrome(s):
    return s == s[::-1]
 
 
def find_Unique(mia_Parola):
    for x in range(len(mia_Parola)):
                
        my_Set.add(mia_Parola[x])
    print("The longest substring contains", len(my_Set),"characters")
    print("The unique characters are: ",my_Set)
    

my_Word = "radar"
answer = isPalindrome(my_Word)
 
if answer:
    print("Yes, the word",my_Word, "is a palindrome.")
else:
    print("No, the word",my_Word, "is not a palindrome.")

my_Set = {'a'}
my_Set.clear()
find_Unique("ppppppi")
