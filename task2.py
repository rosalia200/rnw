# def input_3_variables(a,b,c):
#     if a > b and a > c:
#         print (a)
#     elif b > a and b > c :
#         print (b)
#     else:
#         print(c)
#input_3_variables(25,56,75)
a = int(input("ent var 1:"))
b = int(input ("ent var 2:"))
c = int(input( "ent var 3:" ))
if a >= b and a >= c:
         print (a)
elif b >= a and b >= c :
         print (b)
elif c >= a and c >= b:
        print(c)
else :
    print("all equal")