s = input()

def isPalindrome(string) :
    return string == string[-1::-1]


if isPalindrome(s) :
    print("Yes")
else :
    print("No")