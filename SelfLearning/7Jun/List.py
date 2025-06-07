lst = ["A", "B", "C", "D", "E"]

lst.append("F")
lst[1] = "BB"

lst.pop(len(lst) - 1)

print(lst)
