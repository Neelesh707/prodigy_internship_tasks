import re

def assess_password_strength(password):
    length_criteria = len(password)>=8
    upper_criteria = bool(re.search(r'[A-Z]',password))
    lower_criteria = bool(re.search(r'[a-z]',password))
    digit_criteria = bool(re.search(r'[0-9]',password))
    special_criteria = bool(re.search(r'[\W]',password))

    #calculate strength score
    criteria_met=sum([length_criteria,upper_criteria,lower_criteria,digit_criteria,special_criteria])
    
    #feedback
    if criteria_met==5:
        feedback="Your password is very strong."
    elif criteria_met==4:
        feedback="Your password is strong."
    elif criteria_met==3:
        feedback="Your password is moderate."
    elif criteria_met==2:
        feedback="Your password is weak."
    else:
        feedback="Your password is very weak."
    
    details=[]
    #detail feedback
    if not length_criteria:
        details.append("Password must be atleast 8 characters long.")
    if not upper_criteria:
        details.append("Password must contain atleast one uppercase letter.")
    if not lower_criteria:
        details.append("Password must contain atleast one lowercase letter.")
    if not digit_criteria:
        details.append("Password must contain atleast one digit.")
    if not special_criteria:
        details.append("Password must contain atleast one special character.")
        
    return feedback,details

# Prompt the user for a password and assess its strength

password = input("Enter your password to check its strength: ")
feedback, details = assess_password_strength(password)

# Output the results
print("\nPassword Strength: " + feedback)
if details:
    print("Suggestions for improvement:")
    for detail in details:
        print("- " + detail)