# Give me a palindrome implementation in the language of your choice.
# Valid Palindrome: Check if a string is a palindrome, ignoring case and 
# non-alphanumeric characters (e.g., "A man, a plan, a canal: Panama")
# How do you test it?

#string = "A man, a plan, a canal: Panama"

#pointer a loop from the beginning
def test_palindrome(string):
    print("length: ", len(string), "\n-------------------")
    #initialise pointers
    a = 0
    b = len(string)-1
    
    while a < len(string)-1:
        #if character is not letter
        print("char a: ", string[a])
        if not string[a].isalpha():
            #skip it
            print("SKIP a, b4 +1:", a)
            a += 1
            print("after +1:", a, "\n-------------------")
        elif string[a].isalpha():
            #pointer b loop from the end
            while b > 0:
                #if character is not letter
                print("char b:", b, string[b])
                if not string[b].isalpha():
                    #skip it
                    print("SKIP b, b4 -1:", b)
                    b -= 1
                    print("after -1:", b)
                else: 
                    #if poiner a == pointer b regardless of upper or lower case
                    if string[a].lower() == string[b].lower() :
                        #go to next character
                        print("a and b shd hv the same letter:", string[a], string[b], "\n-------------------")
                        b -= 1
                        a += 1
                        break
                        #if pointer a !== pointer b
                    elif string[a].lower() != string[b].lower():
                        #test fail
                        print(False)
                        return False
        #test pass
    print(True)
    return True

#test_palindrome()
#assert test_palindrome("A man, a plan, a canal: Panama") == True #worked
#assert test_palindrome("") == True #need work
#assert test_palindrome(" ") == True #need work

#assert test_palindrome("0P0") == True #worked
#assert test_palindrome("a") == True #worked
#assert test_palindrome("a25236") == False #need work

