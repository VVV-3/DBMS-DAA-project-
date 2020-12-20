from os import write
import subprocess as sp
import pymysql
import pymysql.cursors
import getpass

login_token = 1

def read_table(query):
    try:
        cur.execute(query)
        result = cur.fetchall()
        return(result)
    except Exception as e:
        print("Error Occured:  ",e)

def write_table(query):
    try:
        cur.execute(query)
        con.commit()
        print("Modification Sucessful!")
    except Exception as e:
        print("Error Occured:  ",e)  

def supplier():
    while(1):
        
        print("Would you like to retreive or modify information in Supplier table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show suppliers\": Gives a complete list of all the details of all the suppliers.")
                print("\"search supplier name\": Runs a partial text match and shows the details of all the suppliers whose names partial match with input string")
                print("\"show frequency\": Shows suppliers whose supply frequency is greater than x")
                print("\"average frequency\": Calculates the average supply frequency of all suppliers.")
                print("\"most frequent\": Shows the details of the supplier(s) who is/are the most frequent.")
                print("\"least frequent\": Shows the details of the supplier(s) who is/are the least frequent.")
                in2=input("Enter the Function Name as mentioned above ar enter \"back\" to go back to Supplier table: ")
                if(in2 == "show suppliers"):
                    query = "select * from suppliers s,Mat_supply m where s.PhoneNo=m.PhoneNo"
                    supp = read_table(query)
                    print(supp) 
                    print("\n")
                elif(in2 == "average frequency"): 
                    avg = read_table("select avg(Supply_frequency) from suppliers")
                    print(avg[0])
                    print("\n")
                elif(in2 == "most frequent"):
                    max = read_table("select * from suppliers s, Mat_supply m where m.PhoneNo=s.PhoneNo and Supply_frequency in (select max(Supply_frequency) from suppliers)")
                    print(max)
                    print("\n")
                elif(in2 == "least frequent"):
                    min = read_table("select * from suppliers s,Mat_supply m where s.PhoneNo=m.PhoneNo and Supply_frequency in (select min(Supply_frequency) from suppliers)")
                    print(min)
                    print("\n")
                elif(in2 == "show frequency"):
                    x = input("Enter the reference x: ")
                    gtx = read_table("select * from suppliers s, Mat_supply m where s.PhoneNo=m.PhoneNo and s.Supply_frequency >" +x+";")
                    print(gtx)
                    print("\n")
                elif(in2 == "search supplier name"):
                    name = input("Enter the name in First,Middle,Last name format: ")
                    name= name.replace(" ","")
                    temp = "select * from suppliers s ,Mat_supply m where s.PhoneNo=m.PhoneNo and concat(Fname,Mname,Lname) like " + "\"%"+name+"%\";"
                    res = read_table(temp)
                    print(res)
                    print("\n")
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="modify"):
            while(1):
                print("\nAdd Supplier: adds a new entry in supplier table")
                print("Update Supplier: updates an entry in supplier table")
                print("Delete Supplier: deletes an entry in supplier table")
                print("PhoneNo of supplier needed for update and delete function. If you don't have it, please go back and use retreive function to get it. \n")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back to Supplier table:")

                if(in2  == "Add Supplier"):
                    row={}
                    print("Enter new supplier's details: ")
                    row["PhoneNo"] = input("PhoneNo: ")
                    row["House_no"] = int(input("House_no: "))
                    row["Area"] = input("Area: ")
                    row["City"] = input("City: ")
                    row["Supply_frequency"] = int(input("Supply Frequency: "))
                    name = (input("Name (Fname Mname Lname): ")).split(' ')
                    row["Fname"] = name[0]
                    row["Mname"] = name[1]
                    row["Lname"] = name[2]
                    row["Material_supplied"] = (input("Materials supplied (should be comma(,) seperated): ")).split(',')
                    query="insert into suppliers values ('%s',%d,'%s','%s',%d,'%s','%s','%s')"%(row["PhoneNo"],row["House_no"],row["Area"],row["City"],row["Supply_frequency"],row["Fname"],row["Mname"],row["Lname"])
                    write_table(query)
                    for i in row["Material_supplied"]:
                        query="insert into Mat_supply values('%s','%s')"%(row["PhoneNo"],i)
                        write_table(query)

                elif(in2 == "Update Supplier"):
                    while(1):
                        print("\n")
                        print("Columns that can be modified House_no, Supply_frequency, Name, Material_supplied, PhoneNo, Area, City")
                        col = input("Enter name of column you would like to update or enter \"back\" to go back: ")
                        if(col == "back"):
                            break
                        pno = input("Enter Phone Number of supplier you want to modify: ")
                        
                        if( col == "House_no" or col=="Supply_frequency"):
                            new_val = int(input("Enter the updated value for %s: " %col))
                            query = "update suppliers set %s=%d where PhoneNo=%s"%(col,new_val,pno)
                            write_table(query)
                        elif(col == "Name"):
                            new_val = (input("Enter the updated value for %s: " %col)).split(' ')
                            query="update suppliers set Fname=\'%s\',Mname=\'%s\',Lname=\'%s\' where PhoneNo=%s"%(new_val[0],new_val[1],new_val[2],pno)
                            write_table(query)
                        elif(col == "Material_supplied"):
                            new_val = (input("Enter the updated value for %s: " %col)).split(',')
                            query="delete from Mat_supply where Phoneno=%s"%pno
                            write_table(query)
                            for i in new_val:
                                query="insert into Mat_supply values('%s','%s')"%(pno,i)
                                write_table(query)
                        elif(col == "PhoneNo" or col == "Area" or col == "City"):
                            new_val = input("Enter the updated value for %s: " %col)
                            query="update suppliers set %s=\'%s\' where PhoneNo=%s"%(col,new_val,pno)
                            write_table(query)
                        else:
                            print("Invalid Choice!")

                elif(in2 == "Delete Supplier"):
                    pno = input("Enter PhoneNo of supplier you want to delete: ")
                    query="delete from suppliers where PhoneNo=%s"%pno
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")
    
def raw_materials():
    while(1):
        
        print("Would you like to retreive, analyse or modify information in Raw Material table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"analyse\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show raw materials\": Gives a complete list of all the details of all the raw materials.")
                print("\"search raw material quantity\": search for raw materials with quantity greater than x")
                print("\"most quantity\": Shows the details of the raw material(s) which has the most quantity.")
                print("\"least quantity\": Shows the details of the raw material(s) which has the least quantity.")
                print("\"search raw material\": Runs a partial text match and shows the details of all the raw materials whose names partial match with input string")
                in2=input("Enter the Function Name as mentioned above ar enter \"back\" to go back: ")
                
                if(in2 == "show raw materials"):
                    supp = read_table(" select * from Raw_materials_supply")
                    print(supp)
                elif(in2 == "search raw material quantity"): 
                    x = input("Enter the reference x: ")
                    avg = read_table("select * from Raw_materials_supply where Quantities > %s"%x)
                    print(avg)
                elif(in2 == "most quantity"):
                    max = read_table("select * from Raw_materials_supply where Quantities=(select max(Quantities) from Raw_materials_supply)")
                    print(max)
                elif(in2 == "least quantity"):
                    min = read_table("select * from Raw_materials_supply where Quantities=(select min(Quantities) from Raw_materials_supply)")
                    print(min)
                elif(in2 == "search raw material"):
                    inp = input("Type the name of the raw material: ")
                    res = read_table("select * from Raw_materials_supply where Name like"+"\"%"+inp+"%\"")
                    print(res)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1 == "analyse"):
            print("Gives a list of suppliers and the raw materials they supply")
            supp = read_table("select * from suppliers")
            for i in supp:
                supp1= read_table("select Materials_supplied from Mat_supply where PhoneNo=%s"%i[0])
                print(supp1,i)
            
        elif(in1 == "modify"):
            while(1):
                print("Add Raw materials: adds a new entry in raw materials table")
                print("Update Raw materials: updates an entry in raw material table")
                print("Delete Raw materials: deletes an entry in raw material table")
                print("Supplier_PhoneNo, Dept.ID and Name needed for update and delete function. If you don't have it, please go back and use retreive function to get it.")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back: ")

                if(in2  == "Add Raw materials"):
                    row={}
                    print("Enter new Raw Material's details: ")
                    row["Sup_PhNo"] = input("Supplier PhoneNo: ")
                    row["Dep_ID"] = int(input("Department ID: "))
                    row["Name"] = input("Name: ")
                    row["Quantities"] = int(input("Quantity of Raw Material: "))
                    query="insert into Raw_materials_supply values ('%s',%d,'%s',%d)"%(row["Sup_PhNo"],row["Dep_ID"],row["Name"],row["Quantities"])
                    write_table(query)

                elif(in2 == "Update Raw materials"):
                    while(1):
                        print("Columns that can be modified are Dep_ID, Quantities, Sup_PhNo, Name")
                        col = input("Enter coloumn to be modified or enter \"back\" to go back: ")
                        if(col == "back"):
                            break
                        print("Enter old raw material's details")
                        pno = input("Supplier PhoneNo: ")
                        did = int(input("Department ID: "))
                        name = input("Name: ")
                        if( col == "Dep_ID" or col=="Quantities"):
                            new_val = int(input("Enter the updated value for %s:" %col))
                            query = "update Raw_materials_supply set %s=%d where Sup_PhNo=%s and Dep_ID=%d and Name=\'%s\'"%(col,new_val,pno,did,name)
                            write_table(query)
                        elif(col == "Sup_PhNo" or col == "Name"):
                            new_val = input("Enter the updated value for %s:" %col)
                            query="update Raw_materials_supply set %s=%s where Sup_PhNo=%s and Dep_ID=%d and Name=\'%s\'"%(col,new_val,pno,did,name)
                            write_table(query)
                        else:
                            print("Invalid Column Name !")

                elif(in2 == "Delete Raw materials"):
                    print("Enter the details of the raw material you would like to delete:")
                    pno = input("Supplier PhoneNo: ")
                    did = int(input("Department ID: "))
                    name = input("Name: ")
                    query="delete from Raw_materials_supply where Sup_PhNo=%s and Dep_ID=%d and Name=\'%s\'"%(pno,did,name)
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")
    

def departments():
    while(1):
        
        print("Would you like to retreive, analyse or modify information in Department table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"analyse\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show departments\": Gives a complete list of all the details of all the departments.")
                print("\"search department employee\": search for departments with number of employees greater than x")
                print("\"most employees\": Shows the details of the department(s) which has the most number of employees.")
                print("\"least employees\": Shows the details of the department(s) which has the least number of employees.")
                print("\"average employees\": Shows the average number of employees in all departments.")
                print("\"search department\": Runs a partial text match and shows the details of all the departments whose names partial match with input string")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back: ")
                
                if(in2 == "show departments"):
                    supp = read_table(" select * from Departments")
                    print(supp)
                elif(in2 == "search department employee"): 
                    x = input("Enter the reference x: ")
                    avg = read_table("select * from Departments where Employee_count > %s"%x)
                    print(avg)
                elif(in2 == "most employees"):
                    max = read_table("select * from Departments where Employee_count=(select max(Employee_count) from Departments)")
                    print(max)
                elif(in2 == "least employees"):
                    min = read_table("select * from Departments where Employee_count=(select min(Employee_count) from Departments)")
                    print(min)
                elif(in2 == "average employees"):
                    avg = read_table("select avg(Employee_count) from Departments")
                    print(avg[0])
                elif(in2 == "search department"):
                    inp = input("Type the name of the department: ")
                    res = read_table("select * from Departments where Dname like"+"\"%"+inp+"%\"")
                    print(res)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1 == "analyse"):
            print("Gives a list of sales made by each department")
            print(read_table("select distinct D.Dname,D.ID,S.name from Departments D, Sell_Products S where D.ID=S.Dept_ID"))
            
        elif(in1 == "modify"):
            while(1):
                print("Add Department: adds a new entry in Departments table")
                print("Update Department: updates an entry in Departments table")
                print("Delete Department: deletes an entry in Departments table")
                print("Dept.ID needed for update and delete function. If you don't have it, please go back and use retreive function to get it.")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back: ")

                if(in2  == "Add Department"):
                    row={}
                    print("Enter new Department's details: ")
                    row["ID"] = int(input("Department ID: "))
                    row["Dname"] = input("Name of new Department: ")
                    row["Employee_count"] = int(input("Employee Count: "))
                    row["Manager_ID"] = int(input("Manager ID: "))
                    query="insert into Departments values (%d,'%s',%d,%d)"%(row["ID"],row["Dname"],row["Employee_count"],row["Manager_ID"])
                    print(query)
                    write_table(query)

                elif(in2 == "Update Department"):
                    while(1):
                        print("Columns that can be modified are ID, Employee_count, Manager_ID, Dname")
                        col = input("Enter column to be modified or enter \"back\" to go back: ")
                        if(col == "back"):
                            break
                        did = int(input("Enter current Department ID: "))
                        if( col == "ID" or col=="Employee_count" or col == "Manager_ID"):
                            new_val = int(input("Enter the updated value for %s:" %col))
                            query = "update Departments set %s=%d where ID=%d "%(col,new_val,did)
                            write_table(query)
                        elif(col == "Dname"):
                            new_val = input("Enter the updated value for %s:" %col)
                            query="update Departments set %s=\'%s\' where ID=%d"%(col,new_val,did)
                            write_table(query)
                        else:
                            print("Invalid Column Name !")

                elif(in2 == "Delete Department"):
                    did = int(input("Enter Department ID of Department you want to delete: "))
                    query="delete from Departments where ID=%d"%did
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")

def employee():
    while(1):
        
        print("Would you like to retreive or modify information in Employee table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show employees\": Gives a complete list of the details of all the employees.")
                print("\"search employee name\": Runs a partial text match and shows the details of all the employees whose names partial match with input string")
                print("\"show number employees\": Shows the number of employees in each department")
                print("\"show employee dep\": Shows the details of employees working in a department whose ID is x")
                in2=input("Enter the Function Name as mentioned above ar enter \"back\" to go back to Supplier table: ")
                
                if(in2 == "show employees"):
                    emp = read_table("select * from Employee")
                    print(emp)
                elif(in2 == "search employee name"): 
                    inp = input("Enter the name of the employee: ")
                    res = read_table("select * from Employee where concat(Fname,Mname,Lname) like"+"\"%"+inp+"%\";")
                    print(res)
                elif(in2 == "show number employees"):
                    emp = read_table("select Dno,count(Employee_ID) from Employee group by Dno")
                    print(emp)
                elif(in2 == "show employee dep"):
                    inp = input("Enter the department ID: ")
                    res = read_table("select Fname,Mname,Lname,Employee_ID from Employee where Dno=%s"%inp)
                    print(res)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="modify"):
            while(1):
                print("Add Employee: adds a new entry in employee table")
                print("Update Employee: updates an entry in employee table")
                print("Delete Employee: deletes an entry in employee table")
                print("Employee Id and Department Id of Employee needed for update and delete function. If you don't have it, please go back and use retreive function to get it.")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back to Supplier table: ")

                if(in2  == "Add Employee"):
                    row={}
                    print("Enter new employee's details: ")
                    row["PhoneNo"] = input("PhoneNo: ")
                    name = (input("Name (Fname Mname Lname): ")).split(' ')
                    row["Fname"] = name[0]
                    row["Mname"] = name[1]
                    row["Lname"] = name[2]
                    row["Employee_ID"] = int(input("Employee ID: "))
                    row["Dno"] = int(input("Department ID: "))
                    row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
                    row["House_no"] = int(input("House_no: "))
                    row["Area"] = input("Area: ")
                    row["City"] = input("City: ")
                    query="insert into Employee values ('%s','%s','%s','%s',%d,%d,'%s',%d,'%s','%s')"%(row["PhoneNo"],row["Fname"],row["Mname"],row["Lname"],row["Employee_ID"],row["Dno"],row["DOB"],row["House_no"],row["Area"],row["City"])
                    write_table(query)
                    t = input("Enter if Employee is \"part-time\" or \"full-time\"")
                    if(t == "part-time"):
                        wage = float(input("Enter Hourly wage:"))
                        dur = input("Enter duration:")
                        query = "insert into Part_time_Emp values (%d,%f,'%s',%d)"%(row["Employee_ID"],wage,dur,row["Dno"])
                        write_table(query)
                    elif t == "full-time":
                        sal = float(input("Enter Salary:"))
                        query = "insert into Full_time_Emp values (%d,%f,%d)"%(row["Employee_ID"],sal,row["Dno"])
                        write_table(query)
                    else:
                        print("Invalid choice!")

                elif(in2 == "Update Employee"):
                    while(1):
                        print("Columns that can be updated are Name, PhoneNo, Employee_ID, Department_ID, HouseNo, Area, City, Employment type queries")
                        col = input("Enter name of column you would like to update or enter \"back\" to go back:")
                        if(col == "back"):
                            break
                        eid = int(input("Enter current Employee ID of Employee you want to modify: "))
                        did = int(input("Enter current Department ID of Employee you want to modify: "))
                        if(col == "HouseNo" or col=="Employee_ID" or col=="Department_ID"):
                            new_val = int(input("Enter the updated value for %s: " %col))
                            query = "update Employee set %s=%d where Employee_ID=%d and Dno=%d"%(col,new_val,eid,did)
                            write_table(query)
                        elif(col == "Name"):
                            new_val = (input("Enter the updated value for %s in First Middle Last format: " %col)).split(' ')
                            query="update Employee set Fname=\'%s\',Mname=\'%s\',Lname=\'%s\' where Employee_ID=%d and Dno=%d"%(new_val[0],new_val[1],new_val[2],eid,did)
                            write_table(query)
                        elif(col == "PhoneNo" or col == "Area" or col == "City"):
                            new_val = input("Enter the updated value for %s: " %col)
                            query="update Employee set %s=\'%s\' where Employee_ID=%d and Dno=%d"%(col,new_val,eid,did)
                            write_table(query)
                        elif(col == "Employment type queries"):
                            t = input("Enter current Employee type(part-time/full-time): ")
                            if(t == "part-time"):
                                query = "delete from Part_time_Emp where Emp_Id=%d and Dno=%d"%(eid,did)
                                write_table(query)
                            elif t == "full-time":
                                query = "delete from Full_time_Emp where Emp_Id=%d and Dno=%d"%(eid,did)
                                write_table(query)
                            else:
                                print("Invalid choice!")
                            t = input("Enter New Employee type(part-time/full-time):")
                            if(t == "part-time"):
                                wage = float(input("Enter Hourly wage:"))
                                dur = input("Enter duration:")
                                query = "insert into Part_time_Emp values (%d,%f,'%s',%d)"%(eid,wage,dur,did)
                                write_table(query)
                            elif t == "full-time":
                                sal = float(input("Enter Salary:"))
                                query = "insert into Full_time_Emp values (%d,%f,%d)"%(eid,sal,did)
                                write_table(query)
                            else:
                                print("Invalid choice!")
                        else:
                            print("Invalid Choice!")

                elif(in2 == "Delete Employee"):
                    eid = input("Enter Employee ID of Employee you want to delete:")
                    did = input("Enter Department ID of Employee you want to delete:")
                    query="delete from Employee where Employee_Id=%d and Dno=%d"%(eid,did)
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")

def dealers():
    while(1):
        
        print("Would you like to retreive or modify information in Dealers table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show dealers\": Gives a complete list of all the details of all the dealers.")
                print("\"search dealer name\": Runs a partial text match and shows the details of all the dealers whose names partial match with input string")
                print("\"show dealer com_x\": Shows dealer names whose commission is greater than x")
                print("\"average commission\": Calculates the average commission of all dealers.")
                print("\"most commission\": Shows the names of the dealer(s) who has/have the most commission.")
                print("\"least commission\": Shows the names of the dealer(s) who has/have the least commission.")
                in2=input("Enter the Function Name as mentioned above ar enter \"back\" to go back to Supplier table: ")
                
                if(in2 == "show dealers"):
                    deal = read_table(" select * from Prod_Supply,Dealers where phone_number = PhoneNo")
                    print(deal)
                elif(in2 == "search dealer name"): 
                    inp = input("Enter the name of the dealer: ")
                    res = read_table("select * from Dealers where concat(Fname,Mname,Lname) like"+"\"%"+inp+"%\"")
                    print(res)
                elif(in2 == "show dealer com_x"):
                    inp = input("Enter reference x: ")
                    res = read_table("select Fname,Mname,Lname from Dealers where Commission > %s"%inp)
                    print(res)
                elif(in2 == "average commission"):
                    deal = read_table("select avg(Commission) from Dealers")
                    print(deal[0])
                elif(in2 == "most commission"):
                    deal = read_table("select Fname,Mname,Lname from Dealers where Commission=(select max(Commission) from Dealers)")
                    print(deal)
                elif(in2 == "least commission"):
                    deal = read_table("select Fname,Mname,Lname from Dealers where Commission=(select min(Commission) from Dealers)")
                    print(deal)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="modify"):
            while(1):
                print("Add Dealer: adds a new entry in dealer table")
                print("Update Dealer: updates an entry in dealer table")
                print("Delete Dealer: deletes an entry in dealer table")
                print("PhoneNo of dealer needed for update and delete function. If you don't have it, please go back and use retreive function to get it.")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back to Dealers table: ")

                if(in2  == "Add Dealer"):
                    row={}
                    print("Enter new supplier's details: ")
                    name = (input("Name (Fname Mname Lname): ")).split(' ')
                    row["Fname"] = name[0]
                    row["Mname"] = name[1]
                    row["Lname"] = name[2]
                    row["Commision"] = float(input("Commision: "))
                    row["PhoneNo"] = input("PhoneNo: ")
                    row["House_no"] = int(input("House_no: "))
                    row["Area"] = input("Area: ")
                    row["City"] = input("City: ")
                    row["Products_supplied"] = (input("Products supplied: (should be comma(,) seperated)")).split(',')
                    query="insert into Dealers values ('%s','%s','%s',%f,'%s',%d,'%s','%s')"%(row["Fname"],row["Mname"],row["Lname"],row["Commision"],row["PhoneNo"],row["House_no"],row["Area"],row["City"])
                    write_table(query)
                    for i in row["Products_supplied"]:
                        query="insert into Prod_Supply values('%s','%s')"%(row["PhoneNo"],i)
                        write_table(query)

                elif(in2 == "Update Dealer"):
                    while(1):
                        print("Columns that can be modified are HouseNo, Name, Product_supplied, PhoneNo, Area, City, Commision")
                        col = input("Enter name of column you would like to update or enter \"back\" to go back:")
                        if(col == "back"):
                            break
                        pno = input("Enter current Phone Number of Dealer you want to modify:")
                        
                        if( col == "HouseNo"):
                            new_val = int(input("Enter the updated value for %s:" %col))
                            query = "update Dealers set %s=%d where PhoneNo=%s"%(col,new_val,pno)
                            write_table(query)
                        elif(col == "Name"):
                            new_val = (input("Enter the updated value for %s: in First Middle Last format: " %col)).split(' ')
                            query="update Dealers set Fname=\'%s\',Mname=\'%s\',Lname=\'%s\' where PhoneNo=%s"%(new_val[0],new_val[1],new_val[2],pno)
                            write_table(query)
                        elif(col == "Product_supplied"):
                            new_val = (input("Enter the updated value for %s: " %col)).split(',')
                            query="delete from Prod_Supply where phone_number=%s"%pno
                            write_table(query)
                            for i in new_val:
                                query="insert into Prod_Supply values('%s','%s')"%(pno,i)
                                write_table(query)
                        elif(col == "PhoneNo" or col == "Area" or col == "City"):
                            new_val = input("Enter the updated value for %s: " %col)
                            query="update Dealers set %s=\'%s\' where PhoneNo=%s"%(col,new_val,pno)
                            write_table(query)
                        elif(col == "Commision"):
                            new_val = input("Enter the updated value for %s: " %col)
                            query="update Dealers set %s=%f where PhoneNo=%s"%(col,new_val,pno)
                            write_table(query)
                        else:
                            print("Invalid Choice!")

                elif(in2 == "Delete Dealer"):
                    pno = input("Enter PhoneNo of Dealer you want to delete:")
                    query="delete from Dealers where PhoneNo=%s"%pno
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")
    

def products():
    while(1):
        
        print("Would you like to retreive or modify information in Products table or go back to Main Menu")
        in1=input("Enter either \"retreive\" or \"modify\" or \"back\": ")
        
        if(in1 == "retreive"):
            while(1):
                print("\"show products\": Gives a complete list of all the details of all the products.")
                print("\"search product quantity\": search for products with quantity greater than x")
                print("\"most quantity\": Shows the details of the product(s) which has/have the most quantity.")
                print("\"least quantity\": Shows the details of the products(s) which has/have the least quantity.")
                print("\"average quantity\": Shows the average quantity of the products")
                print("\"search product\": Runs a partial text match and shows the details of all the products whose names partial match with input string")
                in2=input("Enter the Function Name as mentioned above are enter \"back\" to go back: ")
                
                if(in2 == "show products"):
                    supp = read_table(" select * from Products")
                    print(supp)
                elif(in2 == "search product quantity"): 
                    x = input("Enter the reference x: ")
                    avg = read_table("select * from Products where Quantities > %s"%x)
                    print(avg)
                elif(in2 == "most quantity"):
                    max = read_table("select * from Products where Quantities=(select max(Quantities) from Products)")
                    print(max)
                elif(in2 == "least quantity"):
                    min = read_table("select * from Products where Quantities=(select min(Quantities) from Products)")
                    print(min)
                elif(in2 == "average quantity"):
                    avg = read_table("select avg(Quantities) from Products")
                    print(avg[0])
                elif(in2 == "search product"):
                    inp = input("Type the name of the product: ")
                    res = read_table("select * from Products where Name like"+"\"%"+inp+"%\"")
                    print(res)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1 == "modify"):
            while(1):
                print("Add Product: adds a new entry in products table")
                print("Add Make_Product: adds a new entry in make_products table")
                print("Add Sell_Product: adds a new entry in sell_product table")
                print("Update Product: updates an entry in product table")
                print("Delete Product: deletes an entry in product table")
                print("Dept.ID and Name needed for update and delete function. If you don't have it, please go back and use retreive function to get it.")
                in2=input("Enter the Function Name as mentioned above or enter \"back\" to go back: ")

                if(in2  == "Add Product"):
                    row={}
                    print("Enter new Products's details: ")
                    row["Quantities"] = int(input("Quantity of Products: "))
                    row["Name"] = input("Name: ")
                    row["Dept_ID"] = int(input("Department ID: "))
                    row["price"] = int(input("Price: "))
                    query="insert into Products values (%d,'%s',%d,%d)"%(row["Quantities"],row["Name"],row["Dept_ID"],row["price"])
                    write_table(query)
                elif (in2 == "Add Make_Product"):
                    print("Enter details")
                    name= input("Name: ")
                    did = int(input("Department ID: "))
                    eid = int(input("Employee ID: "))
                    query = "insert into Make_Products values ('%s',%d,%d)"%(name,eid,did)
                    write_table(query)
                elif (in2 == "Add Sell_Product"):
                    print("Enter details")
                    name= input("Name: ")
                    did = int(input("Department ID: "))
                    pno = input("Dealer Phone_No: ")
                    query = "insert into Sell_Products values ('%s','%s',%d)"%(name,pno,did)
                    write_table(query)
                elif(in2 == "Update Product"):
                    while(1):
                        print("Columns that can be modified are Dept_Id, Quantities, price, Name")
                        col = input("Enter column to be modified or enter \"back\" to go back: ")
                        if(col == "back"):
                            break
                        print("Enter current product's details")
                        did = int(input("Department ID: "))
                        name = input("Name: ")
                        if( col == "Dept_ID" or col=="Quantities" or col == "price"):
                            new_val = int(input("Enter the updated value for %s:" %col))
                            query = "update Products set %s=%d where Dept_ID=%d and Name=\'%s\'"%(col,new_val,did,name)
                            write_table(query)
                        elif(col == "Name"):
                            new_val = input("Enter the updated value for %s:" %col)
                            query="update Products set %s=\'%s\' where Dept_ID=%d and Name=\'%s\'"%(col,new_val,did,name)
                            write_table(query)
                        else:
                            print("Invalid Column Name !")
                elif(in2 == "Delete Product"):
                    print("Enter the details of the product you would like to delete:")
                    did = int(input("Department ID: "))
                    name = input("Name: ")
                    query="delete from Products where Dept_ID=%d and Name=\'%s\'"%(did,name)
                    write_table(query)
                elif(in2 == "back"):
                    break
                else:
                    print("Invalid choice!")

        elif(in1=="back"):
            break
        else:
            print("Invalid choice !!")
    


def dispatch(x):
    if x==1:
        supplier()
    elif x==2:
        raw_materials()
    elif x==3:
        departments()
    elif x==4:
        employee()
    elif x==5:
        dealers()
    elif x==6:
        products()
    else:
        print("Enter a valid number!!")
while(login_token == 1):

    tmp = sp.call('clear',shell=True)
    username = input("Type username:")
    password = getpass.getpass()
    database = input("Type database name:")
    
    con = pymysql.Connection(host='localhost',user=username,password=password,db=database)
    cur=con.cursor()
    try:
        tmp = sp.call('clear',shell=True) 
        if (con.open):
            print("CONNECTION ESTABLISHED!!! \n")
        else:
            print("CONNECTION FAILED.... \n")
        tmp = input("Press any key to continue \n")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear',shell=True)
                print("Enter 1 to handle supplier related data \n")
                print("Enter 2 to handle raw materials related data \n")
                print("Enter 3 to handle department related data \n")
                print("Enter 4 to handle employee related data \n")
                print("Enter 5 to handle dealer related data \n")
                print("Enter 6 to handle products related data \n")
                print("Enter 0 to log out \n")
                print("Enter 7 to close this program \n")
                ch = int(input("Enter your choice: "))
                tmp = sp.call('clear',shell=True)
                if(ch==0):
                    break
                elif(ch==7):
                    login_token = 0
                    break
                else:
                    dispatch(ch)
                    tmp = input("Press any key to continue \n")
    
    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database \n")
        tmp = input("Enter any key to continue \n")
