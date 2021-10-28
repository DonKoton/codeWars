import re

def increment_string(strng):
    pattern = r'\d+'
    if len(strng) > 0:
        num = re.findall(pattern, strng)
        if num:
            no_num_str = strng[:-len(num[-1])]
            new_num = int(num[-1]) + 1
            new_strng = no_num_str + str(new_num).zfill(len(str(num[-1])))
            return new_strng
        else:
            return strng + '1'
    else:
        return '1'
