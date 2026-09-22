a = float(input("pisan: "))
b = float(input("kepindo : "))
c = float(input("ketelu: "))

if a > b and a > c:
    largest = a
    print("ongko sek gede:", largest)
elif b > a and b > c:
    largest = b
    print("ongko sek gede:", largest)
elif c > a and c > b:
    largest = c
    print("ongko sek gede:", largest)

else:
    print ("mboten enten ongko sek gedi")