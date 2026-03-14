s = input("Enter a value: ")

try:
    num = int(s)
    print("Integer:", num)
except:
    try:
        num = float(s)
        print("Float:", num)
    except:
        print("Not a number")