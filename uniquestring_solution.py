# Function which identifies whether a string contains all unique character
def isuniquestring(st):
    chars = set()

    for ch in st:
        if ch not in chars:
            chars.add(ch)
        else:
            return False

    return True
