def validate_password(password):
    if len(password) < 8:
        return False
    
    uppercase = any(char.isupper() for char in password)
    if not uppercase:
        return False
    
    lower = any(char.islower() for char in password)
    if not lower:
        return False
    
    digit = any(char.isdigit() for char in password)
    if not digit:
        return False
    
    for char in password:
        if char == ' ':
            return False
    return True

print(validate_password("Password123"))

