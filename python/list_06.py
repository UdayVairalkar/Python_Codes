#palindrome
list=[1,2,3,2,1]
cpy=list.copy()
cpy.reverse()
if(list==cpy):
    print("palindrome")
else:
    print("not palindrome" )