special_chars = ['!', '"', '#', '$', '%', '&', "'", '(', 
')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
given_chars = ')tr^tai@f$ grg%'
special_chars_counter = 0
for char in given_chars:
    if char in special_chars:
        special_chars_counter += 1
print(special_chars_counter)