my_list = ['!', 'a', 's','a','d', '@', 'c', '#', 'd', '$']
#You can use Your own input list
# my_list=input()
speacial_count=0
for chara in my_list:
    if chara.islower(): 
        print("")      #just ignore islower(), isupper(), isalpha(), isdigit()
    elif chara.isupper():
        print("")
    elif chara.isalpha():
        print("")
    elif chara.isdigit():
        print("")
    else:
        speacial_count=speacial_count+1 # count special character
print(speacial_count)
