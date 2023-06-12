def can_obtain_from_first_string(string_1, string_2):
    
    list_1 = list(string_1)
    list_2 = list(string_2)

    
    for char in list_2:
        if char in list_1:
            list_1.remove(char)
        
        else:
            return "NO"

    
    return "YES"


string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")


result = can_obtain_from_first_string(string_1, string_2)
print(result)
