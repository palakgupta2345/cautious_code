print("=============== TO - DO LIST ================")
l = []
def ins():
    e = input("enter task: ")
    l.append(e)
def dis():
    print("-------You TO-DO LIST contains---------")
    for i in l:
        print(i)
def dell():
    n = int(input("enter task number to be deleted: "))
    c = 0
    for i in range(1, len(l)):
        if (i == n):
            l.pop(i-1)
            c += 1
            print("task successfully deleted")
    if (c == 0):
        print("number not present in list")
def modi():
    n = int(input("enter task number to be modified: "))
    c = 0
    for i in range (1,len(l)):
        if (i == n):
            l[i-1] = input("enter modified task: ")
            c += 1
            print("task successfully modified")
    if(c == 0):
        print("number not pressent in list")
def choice(n):
    match n:
        case 1:
            return ins()
        case 2:
            return dis()
        case 3:
            return dell()
        case 4:
            return modi()
        case default:
            print("wrong choice")

ch = 'y'
while(ch == 'y' or ch == 'Y'):
    print("1.add task \n2.display task \n3.delete task \n4.modify task")
    n = int(input("Enter your choice :"))
    choice(n)
    ch = input("do you want to continue:")
    print("\n")