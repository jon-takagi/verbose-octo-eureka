import math
def str_to_coords(str):
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

def distance_between(p1, p2):
    # if isinstance(p1, location) and isinstance(p2, location):
        return math.sqrt((p1.row - p2.row)**2 + (p1.col - p2.col)**2)
    # return (chr(col + 97) if col < 26 else chr(col + 39) )+ str(row)
