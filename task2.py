
def check_word(str, l):
    if str in l:
        return True
    else:
        return False

my_list = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']
print(check_word('bcd', my_list))
