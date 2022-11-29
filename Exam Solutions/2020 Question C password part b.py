# Question 16(b)
# Examination Number:

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

# Ans (iv)
def is_strong(password):
    return (calculate_score(password) == 11)

# Ans (iv) - version 1
def is_strong_v1(password):
    strong = False

    if calculate_score(password) == 11:
        strong = True

    return strong

# Ans (iv) - version 2
def is_strong_v2(password):
    strong = False

    lowercase = False # True if password contains a lowercase letter
    uppercase = False # True if password contains an uppercase letter

    # Loop through each character in the password and ...
    # ...check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True

    if len(password) > 7 and lowercase and uppercase:
        strong = True

    return strong

def calculate_score(password):

    # The variables lowercase and uppercase indicate the presence of ...
    # ... lowercase and uppercase characters in the password
    lowercase = False # True if password contains at least 1 lowercase letter

    uppercase = False # True if password contains at least 1 uppercase letter

# Loop through each character in the password and ...
    # ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True

    # Calculate the score based on the rules

    score = 0

    # Rule 1
    if len(password) > 7:
        score = score + 5

    # Rule 2
    if lowercase:
        score = score + 1

    # Rule 3
    if lowercase and uppercase:
        score = score + 5


    return score

# Test driver ...
test_passwords = ["sun", "Sun", "Sunshine", "12345", "123456789"]
test_passwords[4] = "Moonlight" # Ans (ii)

print("Score\tPassword") # Ans (i)
print("-----\t--------") # Ans (i)
lowest_score = 999 # Ans (iii)
weakest_password = "" # Ans (iii)
for password in test_passwords:
    pass_score = calculate_score(password)
    if pass_score < lowest_score: # Ans (iii)
        lowest_score = pass_score # Ans (iii)
        weakest_password = password # Ans (iii)
    print(pass_score, "\t", password) # Ans (i)

print()# Ans (iii)
print("The weakest password is:", weakest_password) # Ans (iii)
print("Score:", lowest_score) # Ans (iii)


# Ans (v)
# Modify the program so that it calls the function is_strong for each password in the list, test_passwords, and
# ... displays the password if it is strong
print()
print("The strong passwords are:")
for password in test_passwords:
    if is_strong(password):
        print(password)
