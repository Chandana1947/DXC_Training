# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:35:39 2021

@author: Gaddam Srinivas
"""

# This is simplest Student data management program in python
# Create class "Student"
class Student:
    # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
         
    # Function to create and append new student   
    def accept(self, Name, Rollno, marks1, marks2 ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2 )
        ls.append(ob)
  
    # Function to display student details     
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("Marks1 : ", ob.m1)
            print("Marks2 : ", ob.m2)
            print("\n")    
         
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i      
            else:
                return -1
            
    def search_name(self, sn):
        for i in range(ls.__len__()):
            if(ls[i].name == sn):
                return i      
            else:
                return -1
    
    # Delete Function                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    # Update Function   
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;
         
# Create a list to add Students
ls =[]
# an object of Student class
obj = Student('', 0, 0, 0)

print("==============================================")
print("\t\tMain Menu\n\t\t_ _ _ _ _")
print("\n\t\t1.Add record\n\t\t2.Display all records\n\t\t3.Search by rollno\n\t\t4.Search by Search by name\n\t\t5.Modify by rollno\n\t\t6.Delete by rollno\n\t\t6.Exit")
 
ch = 0
while(ch!=6):
    ch = int(input("Enter choice:"))
    if(ch == 1):
        n = input("Enter student name")
        r = int(input("Enter student RollNo"))
        s1 = int(input("Enter marks of subject 1:"))
        s2 = int(input("Enter marks of subject 2:"))
        obj.accept(n,r,s1,s2)
             
    elif(ch == 2):
        print("\n")
        print("\nList of Students\n")
        for i in range(ls.__len__()):    
            obj.display(ls[i])
                 
    elif(ch == 3):
        s = obj.search(int(input("Enter roll no:")))
        if(s !=-1):
            print("\n Student Found, ")
            obj.display(ls[s])
        else:
            print("\n Student not found")
            
    elif(ch == 4):
        s = obj.search_name(input("Enter name:"))
        if(s !=-1):
            print("\n Student Found, ")
            obj.display(ls[s])
        else:
            print("\n Student not found")
    
    elif(ch == 5):
        m_rn = int(input("Enter roll no to be modified:"))
        m_nrn = int(input("Enter new roll no:"))
        obj.update(m_rn, m_nrn)
        print(ls.__len__())
        print("List after updation")
        for i in range(ls.__len__()):    
            obj.display(ls[i])
     
    elif(ch == 6):
        d_rn = int(input("Enter roll no to delete record:"))
        obj.delete(d_rn)
        print(ls.__len__())
        print("List after deletion")
        for i in range(ls.__len__()):    
            obj.display(ls[i])
                 
    else:
        print("Thank You !")
        break