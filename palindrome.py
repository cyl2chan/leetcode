# Give me a palindrome implementation in the language of your choice.
# Valid Palindrome: Check if a string is a palindrome, ignoring case and 
# non-alphanumeric characters (e.g., "A man, a plan, a canal: Panama")
# How do you test it?

string = "A man, a plan, a canal: Panama"

#initialise pointers
a = 0
b = -1

#pointer a loop from the beginning
def test_palindrome():
    for a in range(len(string)):
        #if character is not letter
        if not string[a].isalpha():
            #skip it
            a += 1
        else:
            #pointer b loop from the end
            for b in range(len(string[-1])):
                #if character is not letter
                if not string[b].isalpha():
                    #skip it
                    b -= 1
                else: 
                    #if poiner a == pointer b regardless of upper or lower case
                    if string[a].lower() == string[b].lower() :
                        #go to next character
                        b -= 1
                        break
                        #if pointer a !== pointer b
                    else: #string[a].lower() != string[b].lower()
                        #test fail
                        print(False)
                #test pass
                print(True)

test_palindrome()