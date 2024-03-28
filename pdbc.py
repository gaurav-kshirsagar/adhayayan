import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', password='root', db='pdbc')
curs = conn.cursor()
conn.autocommit('on')

#query = 'create table student (roll int primary key auto_increment,'\
#       'fname varchar(20), marks float)'
#curs.execute(query)
#print('table created')


def add_student():
    roll = int(input("Enter the roll number: "))
    fname = input("Enter the name: ")
    marks = float(input("Enter the marks: "))
    query = f'insert into student values ({roll}, "{fname}",{marks})'
    curs.execute(query)
    print(f'record of {fname} added')

def show_stu_info():
    query = 'select * from student'
    curs.execute(query)
    all_data = curs.fetchall()
    print(all_data)

def delete_stu_info():
    roll = int(input('Enter the roll number'))
    query = 'delete from student where roll = {roll}'
    curs.execute(query)
    print('record deleted')

def update_stu_info():
    roll = int(input('Enter the roll number'))
    ch = input('What do you want to update 1.name 2. marks')
    if ch ==1:
        new_name = input('Enter the new name')
        query = f'update student set fname="{new_name}" where roll = {roll}'
    elif ch ==2:
        new_marks = float(input('Enter the marks'))
        query = f'update student set marks={new_marks} where roll = {roll}'
    curs.execute(query)

while True:
    ch = int(input('Enter your choice\n 1 add student \t 2.show student\n 3.update stu info\t 4.Delete stud_info\n 5.Exit '))
    match ch:
        case 1:
            add_student()
        case 2:
            show_stu_info()
        case 3:
            update_stu_info()
        case 4:
            delete_stu_info()
        case 5:
            print('Exit')
            break
        case _:
            print('Invalid choice')

#conn.close()



