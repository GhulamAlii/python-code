#################     Import/Export       ###################

def writeData(data):
    if data == 1:
        print("\t\t\t################## Karachi DATABASE ###################\n")
        cat = int(input("Enter The Unit Number To Open\n1) Import Unit\n2) Export Unit\n"))
        if cat == 1:
            print("\t\t\t*********** Import Unit ***********")
            entry = input("Write Your Data\n")
            with open("Karachi_imp.txt", "a") as karImp:
                karImp.write(entry + "\n")
                print("Your Data Was Saved!")

        elif cat == 2:
            print("\t\t\t*********** Export Unit ***********")
            entry = input("Write Your Data\n")
            with open("Karachi_exp.txt", "a") as karExp:
                karExp.write(entry + "\n")
                print("Your Data Was Saved!")

    elif data == 2:
        print("\t\t\t################## LAHORE DATABASE ###################")
        cat = int(input("Enter The Unit Number To Open\n1) Import Unit\n2) Export Unit\n"))

        if cat == 1:
            print("\t\t\t*********** Import Unit ***********")
            entry = input("Write Your Data\n")
            with open("lhr_imp.txt", "a") as lhrImp:
                lhrImp.write(entry + "\n")
                print("Your Data Was Saved!")

        elif cat == 2:
            print("\t\t\t*********** Export Unit ***********")
            entry = input("Write Your Data\n")
            with open("lhr_exp.txt", "a") as lhrExp:
                lhrExp.write(entry + "\n")
                print("Your Data Was Saved!")

    else:
        print("Please Enter The Valid Commend")


def showData(data):
    if data == 1:
        print("\t\t\t################## Karachi DATABASE ###################\n")
        cat = int(input("Enter The Unit Number To Open\n1) Import Unit\n2) Export Unit\n"))
        if cat == 1:
            print("\t\t\t*********** Import Unit ***********")
            with open("Karachi_imp.txt") as karImp:
               a = karImp.read()
               print(a)

        elif cat == 2:
            print("\t\t\t*********** Export Unit ***********")
            with open("Karachi_exp.txt") as karExp:
               a = karExp.read()
               print(a)
    elif data == 2:
        print("\t\t\t################## LAHORE DATABASE ###################")
        cat = int(input("Enter The Unit Number To Open\n1) Import Unit\n2) Export Unit\n"))

        if cat == 1:
            print("\t\t\t*********** Import Unit ***********")
            with open("Karachi_imp.txt") as lhrImp:
                a=lhrImp.read()
                print(a)

        elif cat == 2:
            print("\t\t\t*********** Export Unit ***********")
            with open("lahore_exp.txt") as lhrExp:
                a=lhrExp.read()
                print(a)
    else:
        print("Please Enter The Valid Commend")


#####################################   STRUCTURE   ############################################
print("\t\t\t####################################################")
print("\t\t\t####################################################")
print("\t\t\t################## IMPORT/EXPORT ###################")
print("\t\t\t##################   Management  ###################")
print("\t\t\t##################    SOFTWARE   ###################")
print("\t\t\t####################################################")
print("\t\t\t####################################################\n")

stop = True
while stop:
    print("Which Command You Want To Perform\n1) Data Entry\n2) Show Data \n3) Exit\n")
    action = int(input("Enter Your Command Number\n"))
    if action == 1:
        print("Which Region You Want To Exceed\n1) Karachi\n2) Lahore\n")
        region = int(input("Enter Your Region Number To Access Them\n"))
        writeData(region)

    elif action == 2:
        print("Which Region You Want To Exceed\n1) Karachi\n2) Lahore\n")
        region = int(input("Enter Your Region Number To Access Them\n"))
        showData(region)
    elif action == 3:
        stop = False
    else:
        print(" Please Enter The Correct Task Input")
