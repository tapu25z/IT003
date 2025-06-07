t = ("blue", "red", "yellow", "orange") 

print(t[1])

cnt = t.count("blue")

if "blue" in t:
    print("Ton tai mau blue trong tuple")
else:
    print("Khong ton tai mau blue trong tuple")

for i in t:
    print(i, end = " ")