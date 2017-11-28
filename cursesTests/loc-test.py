def move_to_coords(str):
    col_txt = str[0]
    row_txt = str[1:]
    row_int = int(row_txt)
    col_int = 0
    if col_txt.islower():
        col_int = ord(col_txt) - 97
    else:
        col_int = ord(col_txt) + 26 - 65
    return (row_int, col_int)
def coords_to_str(t):
    row = t[0]
    col = t[1]
    return (chr(col + 97) if col < 26 else chr(col + 39) )+ str(row)
def test():
    from string import ascii_lowercase
    from string import ascii_uppercase
    for c in ascii_lowercase:
        for j in range(32):
            move = c+str(j)
            if (move != coords_to_str(move_to_coords(move))):
                print(move, coords_to_str(move_to_coords(move)))
                return False
    for c in ascii_uppercase:
        for j in range(32):
            move = c+str(j)
            if (move != coords_to_str(move_to_coords(move))):
                print(move, coords_to_str(move_to_coords(move)))
                return False
    return True
