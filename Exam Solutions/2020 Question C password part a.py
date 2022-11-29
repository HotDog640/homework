# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Ans (iii):
DIGITS = "0123456789" # Ans (v)

# The variables lowercase and uppercase indicate the presence of ...
# ... lowercase and uppercase characters in the password
lowercase = False # True if password contains at least 1 lowercase letter
uppercase = False # True if password contains at least 1 uppercase letter
digits = False

# Loop through each character in the password and ...
# ... check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS: # Ans (iii):
        uppercase = True
    if character in DIGITS: # Ans (v)
        digits = True


# Calculate the score based on the rules

score = 0 # Ans (i): initialise score

# Rule 1
# Ans (viii)
if len(password) > 7:
    score = score + 5
elif len(password) >= 4 and len(password) <= 7:
    score = score + 2
else:

    score = score - 2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# Ans (iv): Rule 4
if uppercase:
    score = score + 2

# Ans (v): Rule 5
if digits:
    score = score + 5

# Ans (vi): Rule 6
if password[0] in DIGITS:
    score = score + 1
if password[-1] in DIGITS:
    score = score + 1
if password[0] in DIGITS and password[-1] in DIGITS:
    score = score + 2

# Ans (vii): Rule 7
if digits and not lowercase and not uppercase:
    score = score - 10


# Display the score
#print(score)
# Ans (ii):
print("Password:", password)
print("Score:", score)