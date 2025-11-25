#student management system
data = []

# Load old data
try:
    data = eval(open("student.txt").read())
except Exception:
    data = []

while True:
    print("\n1 Add  2 View  3 Search  4 Delete  5 Exit")
    ch = input("Choice: ")

    if ch == "1":
        r = input("Roll: ")
        n = input("Name: ")
        m = float(input("Mark: "))
        data.append({"roll": r, "name": n, "mark": m})
        print("Added")

    elif ch == "2":
        for s in data:
            print(s)

    elif ch == "3":
        r = input("Roll: ")
        for s in data:
            if s["roll"] == r:
                print(s)
                break
        else:
            print("Not found")

    elif ch == "4":
        r = input("Roll: ")
        data = [s for s in data if s["roll"] != r]
        print("Deleted")

    elif ch == "5":
        break

    else:
        print("Invalid")

# Save data
open("student.txt", "w").write(str(data))
print("Saved & Exit")