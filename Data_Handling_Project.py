import pandas as pd 
import numpy as np
from datetime import date
from time import sleep
from dateutil.parser import parse
import matplotlib.pyplot as pl

csvlist = pd.read_csv('Listofpatients.csv')

def main_menu():
    print('\t\t\n Welcome to Covid-19 Testing Program')
    print('-------------------------------------------------------------------------------------------------')
    print('''\nChoose a Login Option:
    \n         1. ADMIN
         2. USER 
         3. EXIT PROGRAM''')
    LogOpt = int(input('\nENTER YOUR CHOICE: '))
    if LogOpt == 1:
        password = input('\nEnter the passcode: ')
        if password == '123': #set password
            Admin()
        else:
            print("You've entered the wrong password")
            exit
    elif LogOpt == 2:
        User()
    elif LogOpt == 3:
        exit
    else:
        print("Invalid choice pls try again....")
        main_menu()

def ModifyDetails(): #edit patient details
    
    csvlist = pd.read_csv('Listofpatients.csv')

    modind = int(input('Enter the index of row to be modified: '))

    print(csvlist.iloc[modind])

    modcol = str(input('Enter the column name: '))

    if modcol not in ['Name','Date of test','Age','Gender','Result']:
        print('\n Entered column name is wrong...')
        ModifyDetails()


    modval = input('Enter the value: ')
    
    if modcol == 'Date of test': #convert inputted date to correct format
        parse(modval)
    elif modval.isdigit():
        modval = int(modval)

    csvlist.loc[modind, modcol] = modval #edit the record
    csvlist.to_csv('Listofpatients.csv', index = False)
    
    print(csvlist.loc[modind])

    modagain = input('\nDo you want to modify another record(Y/N): ')
    modagain = modagain.lower()
    if modagain == 'y':
        ModifyDetails()
    else:
        Admin()

    

def SearchFunc(): #to search for specific data
    try:
        searchlist = pd.read_csv('Listofpatients.csv')
        scol = str(input('Enter the coloumn name to be searched: '))

        srow = input('Enter the value to be searched: ')

        if scol == 'Date of test':
            parse(srow)

        if srow.isdigit():
            srow = int(srow)

        print(searchlist[searchlist[scol] == srow ])

    except FileNotFoundError:
        print('File does not exist...')
        
    input('\nPress Enter to continue.... ')
    Admin()


def Add():  #Adding data 
    run = True #run variable so it keeps running
    while run == True:
        csvlist = pd.read_csv('Listofpatients.csv') #reading the csv file

        a = str(input('Enter the name: '))
        b = date.today()
        c = int(input('Enter the age of Patient: '))
        d = str(input('Enter the Gender (M/F): '))
        e = str(input('Enter the result of test(Positive/Negative): '))

        x = [a,b,c,d,e]

        df = pd.DataFrame([x])
        df.to_csv('Listofpatients.csv', mode='a', header= False, index= False) 

        csvlist = pd.read_csv('Listofpatients.csv')
        q = input('Do you want to run the program again (Y/N): ')
        q = q.lower()
        if q == 'y':
            run = True
        else:
            run = False
            Admin()

def Delete():
    csvlist = pd.read_csv('Listofpatients.csv')
    droplist = input('Enter the index of patients to be deleted: ')
    droplist = droplist.split(',')
    
    dropp = []

    for i in droplist: #to make the list integers from strings
        dropp.append(int(i)-1)

    csvlist.drop(dropp, inplace = True)
    csvlist.to_csv('Listofpatients.csv',index = False)
    print(csvlist)
    input('\nPress Enter to continue...')
    Admin()

def traverse_patients(): #display all data
    trav_txt = 'Reading all the record of CSV file'
    
    for i in trav_txt: #typing effect
        sleep(0.1)
        print(i, end = '', flush = True)
    print('\n                       ')

    try:
        csvlist = pd.read_csv('Listofpatients.csv')
        print(csvlist)

        
    except FileNotFoundError:
        print('No such file was found....')
    input('\n Press enter key to continue....')
    main_menu()

def Graphs(): #to show graph
    print('\n Available graph options:')
    print('\n1.BASED ON GENDER')
    print('2.BASED ON AGE')
    graphopt = int(input('\n Enter your choice :'))
    if graphopt == 1:
        m = csvlist[csvlist['Gender'] == 'M']
        mn = m[m['Result'] == 'Negative']
        mp = m[m['Result'] == 'Positive']

        f = csvlist[csvlist['Gender'] == 'F']
        fn = f[f['Result'] == 'Negative']
        fp = f[f['Result'] == 'Positive']


        countmn = len(mn.index)
        countmp = len(mp.index)
        countfn = len(fn.index)
        countfp = len(fp.index)

        w = 0.4
        gen = ['Male','Female']
        pos = [countmp,countfp]
        nev = [countmn,countfn]

        bar1 = np.arange(len(gen))
        bar2 = [i+w for i in bar1]

        pl.bar(bar1, pos, w, label= 'Positive')
        pl.bar(bar2, nev, w, label= 'Negative')
        pl.xlabel('Genders')
        pl.ylabel('No. of patients')
        pl.title('Covid-19 Cases based of Gender')
        pl.xticks(bar1+w/2,gen)
        pl.legend()
        pl.show()
    
    
    elif graphopt == 2:
        
        p1_12 = 0
        p13_17 = 0
        p18_25 = 0
        p26_40 = 0
        p40_60 = 0
        p60 = 0

        for i in range(1,13):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p1_12 += len(n.index)

        for i in range(13,18):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p13_17 += len(n.index)

        for i in range(18,26):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p18_25 += len(n.index)

        for i in range(26,41):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p26_40 += len(n.index)

        for i in range(40,61):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p40_60 += len(n.index)

        for i in range(60,300):
            m = csvlist[csvlist['Age'] == i]
            n = m[m['Result'] == 'Positive']
            p60 += len(n.index)
        
        ages = ['1-12','13-17','18-25','25-40','40-60','60+']
        numofp = [p1_12,p13_17,p18_25,p26_40,p40_60,p60]
        barcolor = ['r','orange','y','g','b','m']
        pl.bar(ages,numofp, width = 0.4, color = barcolor)
        pl.xlabel('Age of Patients')
        pl.ylabel('No. of patients')
        pl.title('Covid-19 cases based on Age')
        pl.show()
            
    else:
        print('Invalid choice...')
        exit


def Admin():
    print('\n Welcome to Admin')
    print('\n Covid-19 Test Record Program')
    print('''
    1. Add a new patient
    2. Modify a patient details
    3. Delete patients records
    4. Display all patient details
    5. Search for patient records
    6. Data Visualization of all patient details
    7. Return to Main Menu
    8. Exit''')
    option = int(input('\n Enter your choice: '))
    if option == 1 :
        Add()
    elif option == 2:
        ModifyDetails()
    elif option == 3:
        Delete()
    elif option == 4:
        traverse_patients()
    elif option == 5:
        SearchFunc()
    elif option == 6 : 
        Graphs()
        main_menu()
    elif option == 7: 
        main_menu()
    elif option == 8:
        exit
    else: 
        print("Invalid option please choose the correct option...")
        Admin()

def User():
    print('\n Choose from the following options: ')
    print('\n    1.Data Visualization of all patient details')
    print('    2.Display All Patient Data')
    UserOpt = int(input('\nEnter your option: '))
    if UserOpt == 1:
        Graphs()
    elif UserOpt == 2:
        traverse_patients()
    else:
        print('\nInvalid Choice...')
        main_menu()

main_menu()