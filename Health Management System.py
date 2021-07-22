def getdate():
    import datetime
    return datetime.datetime.now()


def opn(n, d):
    f = open(f"{n}-{d}", "a")
    x = input("Enter data: ")
    f.write("\n")
    f.write(x)


def enter():
    name = {1: "Sneh", 2: "Saurav", 3: "Sam"}
    work = {1: "F", 2: "E"}
    b = int(input("1. Food\n 2. Exercise: "))
    c = int(input("Enter client no. \n 1. Sneh\n 2. Saurav\n 3. Sam: "))
    opn(name[c], work[b])


def read(n, w):
    g = open(f"{n}-{w}")
    f = g.read()
    print(getdate())
    print(f)


def retrieve():
    name = {1: "Sneh", 2: "Saurav", 3: "Sam"}
    work = {1: "F", 2: "E"}
    c = int(input("Choose 1 client:\n 1. Sneh\n 2. Saurav\n 3. Sam: "))
    b = int(input("For Food retrieval: Press 1\nFor Exercise retrieval: Press 2: "))
    read(name[c], work[b])


while 1:
    a = input("1. Enter data\n2. Check data:\n ")
    if a == "1":
        enter()
    elif a == "2":
        retrieve()
    else:
        print("\nInvalid\n")
    a = input("If want to go through this process again then press 1: ")
    if a == '1':
        continue
    else:
        break
