s = int(input("Enter the subject: "))
m = []

if s > 0:
    i = 0
    while  i < s:
        marks = float(input("Enter the marks:"))
        if marks > 0 and marks <= 100:
            m.append(marks)
            i = i+1
        else:
            print("Enter the valid marks and try again")
    print("Total marks: ", sum(m))
    print("Average marks: ",sum(m)/s)
else:
    print("Subject must be greater than 1")