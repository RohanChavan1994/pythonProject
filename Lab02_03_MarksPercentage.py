english = int(input("Enter English marks out of 100: "))
hindi = int(input("Enter Hindi marks out of 100: "))
physics = int(input("Enter Physics marks out of 100: "))
chemistry = int(input("Enter Chemistry marks out of 100: "))
maths = int(input("Enter Maths marks out of 100: "))
biology = int(input("Enter Biology marks out of 100: "))

total_marks = english + hindi + physics + chemistry + maths + biology
print("Final percentage:", round(((100 * total_marks)/600), 2))