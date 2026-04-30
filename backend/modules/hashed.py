from bcrypt import hashpw,checkpw,gensalt

def create_hashed_password(data:str)->bytes:
    new_password=hashpw(data.encode("Utf-8"),gensalt(16))
    return new_password

def check_password(data:str,old_pw:bytes)->bool:
    return checkpw(data.encode("Utf-8"),old_pw)