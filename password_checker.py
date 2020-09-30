import re


def check_valid(password):
    pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
    pwd_is_valid = pattern.fullmatch(password)
    return pwd_is_valid is not None
