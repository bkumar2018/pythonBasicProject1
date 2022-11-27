#code for a simple calculator
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Squaring")
print("6. Cubing")
print("7. Rasing a number to a specific power")
print("8. Square root of a number")
print("9. Cube root of a number")
print("10. Area of a triangle through its height and base")
print("11. Area of a triangle through length of all sides")
print("12. Area of a rectangle")
print("13. Area of a circle")
print("14. Area of a square")
print("15. Area of a parallelogram")
print("16. Area of a semi circle")
print("17. TSA of cone")
print("18. TSA of sphere")
print("19. TSA of hemisphere")
print("20. TSA of cuboid")
print("21. TSA of cube")
print("22. TSA of cylinder")
print("23. CSA of cone")
print("24. CSA of hemisphere")
print("25. CSA of cylinder")
print("26. LSA of cuboid")
print("27. LSA of cube")
print("28. Volume of cone")
print("29. Volume of sphere")
print("30. Volume of hemisphere")
print("31. Volume of cuboid")
print("32. Volume of cube")
print("33. Volume of cylinder")
print("34. Convert celcius to fahrenheit")
print("35. Convert fahrenheit to celcius")
print("0. Exit")
choice=float(input("Enter a choice:"))
if choice==1:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    print("The sum of these numbers is",a+b)
elif choice==2:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    print("After subtracting number 1 from number 2 we get",b-a)
    print("After subtracting number 2 from number 1 we get",a-b)
elif choice==3:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    print("After dividing number 1 by number 2 we get",a/b)
    print("After dividing number 2 by number 1 we get",b/a)
elif choice==4:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    print("The product of the 2 numbers is",a*b)
elif choice==5:
    a=float(input("Enter a number:"))
    print("The square of the number is",a*a)
elif choice==6:
    a=float(input("Enter a number:"))
    print("The cube of the number is",a*a*a)
elif choice==7:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    print("After raising the 1st number to the 2nd number's power we get",a**b)
    print("After raising the 2nd number to the 1st number's power we get",b**a)
elif choice==8:
    a=float(input("Enter a number:"))
    print("The square root of the number is",a**0.5)
elif choice==9:
    a=float(input("Enter a number:"))
    print("The cube root of the number is",a**(1/3))
elif choice==10:
    a=float(input("Enter the height:"))
    b=float(input("Enter the base:"))
    print("The area of the triangle is",1/2*a*b)
elif choice==11:
    a=float(input("Enter the 1st side:"))
    b=float(input("Enter the 2nd side:"))
    c=float(input("Enter the 3rd side:"))
    s=(a+b+c)/2
    print("The area of the triagle is",(s*(s-a)*(s-b)*(s-c))**0.5)
elif choice==12:
    a=float(input("Enter the length:"))
    b=float(input("Enter the breadth:"))
    print("The are of the rectangle is",a*b)
elif choice==13:
    a=float(input("Enter the radius:"))
    print("The area of the circle is",22/7*r*r)
elif choice==14:
    a=float(input("Enter the side:"))
    print("The are of the square is",a*a)
elif choice==15:
    a=float(input("Enter the height:"))
    b=float(input("Enter the base:"))
    print("The are of the parallelogram is",a*b)
elif choice==16:
    a=float(input("Enter the radius:"))
    print("The area of the circle is",22/7*r*r*1/2)
elif choice==17:
    a=float(input("Enter the radius:"))
    b=float(input("Enter the slant height:"))
    print("The TSA of the cone is",22/7*a*a+22/7*a*b)
elif choice==18:
    a=float(input("Enter the radius:"))
    print("The TSA of the sphere is",22/7*4*a*a)
elif choice==19:
    a=float(input("Enter the radius:"))
    print("The TSA of the hemisphere is",22/7*3*a*a)
elif choice==20:
    a=float(input("Enter the length:"))
    b=float(input("Enter the breadth:"))
    c=float(input("Enter the height:"))
    print("The TSA of the cuboid is",2*((a*b)+(b*c)+(c*a)))
elif choice==21:
    a=float(input("Enter the side:"))
    print("The TSA of the cube is",6*(a*a))
elif choice==22:
    a=float(input("Enter the height:"))
    b=float(input("Enter the radius:"))
    print("The TSA of the cylinder is",(22/7*2*b*b)+(22/7*b*a*2))
elif choice==23:
    a=float(input("Enter the radius:"))
    b=float(input("Enter the slant height:"))
    print("The CSA of the cone is",22/7*a*b)
elif choice==24:
    a=float(input("Enter the radius:"))
    print("The CSA of the hemisphere is",22/7*2*a*a)
elif choice==25:
    a=float(input("Enter the radius:"))
    b=float(input("Enter the height:"))
    print("The TSA of the cylinder is",2*22/7*a*b)
elif choice==26:
    a=float(input("Enter the length:"))
    b=float(input("Enter the breadth:"))
    c=float(input("Enter the height:"))
    print("The LSA of the cuboid is",(2*c*b)+(2*a*b))
elif choice==27:
    a=float(input("Enter the side:"))
    print("The LSA of the cube is",4*r*r)
elif choice==28:
    a=float(input("Enter the height:"))
    b=float(input("Enter the radius:"))
    print("The volume of the cone is",1/3*22/7*b*b*a)
elif choice==29:
    a=float(input("Enter the radius:"))
    print("The volume of the sphere is",4/3*22/7*a*a*a)
elif choice==30:
    a=float(input("Enter the radius:"))
    print("The volume of the hemisphere is",2/3*22/7*a*a*a)
elif choice==31:
    a=float(input("Enter the length:"))
    b=float(input("Enter the breadth:"))
    c=float(input("Enter the height:"))
    print("The volume of the cuboid is",a*b*c)
elif choice==32:
    a=float(input("Enter the side"))
    print("The volume of the cube is",a*a*a)
elif choice==33:
    a=float(input("Enter the radius:"))
    b=float(input("Enter the height:"))
    print("The volume of the cylinder is",22/7*a*a*b)
elif choice==34:
    a=float(input("Enter the temperature in celcius:"))
    print("The temperature in fahrenheit is",(a*9/5)+32,"degree fahrenheit")
elif choice==35:
    a=float(input("Enter the temperature in fahrenheit:"))
    print("The temperature in celcius is",(a-32)*5/9,"degree celcius")
elif choice==0:
    exit();
else:
    print("ERROR")



