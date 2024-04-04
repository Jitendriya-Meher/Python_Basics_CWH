marks = [  3,4,6,9,"abs",1,2,3,4,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[-1])
print(marks[-3])

if 5 in marks:
    print("5 is present in marks")
else:
    print("5 is not present in marks")

if 0 in marks:
    print("0 is present in marks")
else:
    print("0 is not present in marks")

if "abs" in marks:
    print("abs is present in marks")
else:
    print("abs is not present in marks")

if "ten" in "jitendriya":
    print("ten is present in jitendriya")
else:
    print("ten is not present in jitendriya")

print(marks[:])
print(marks[2:6])
print(marks[:6])
print(marks[5:])
print(marks[1:8:3])

lst = [ i*i for i in range(2,20) if i%2==0]
print(lst)