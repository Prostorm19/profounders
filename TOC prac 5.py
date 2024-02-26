# Design a Program for creating machine that accepts the string always ending with 101.
def ends_with_101(string):
    return string.endswith('101')

accepted_strings = []

while True:
    user_input = input("Enter a string: ")
    
    if ends_with_101(user_input):
        accepted_strings.append(user_input)
        print("String accepted.")
    else:
        print("Error: String must end with 101.")
    
    user_choice = input("Exit and view accepted strings? (y/n): ")
    
    if user_choice.lower() == 'y':
        break

print("Accepted strings:")
for string in accepted_strings:
    print(string)