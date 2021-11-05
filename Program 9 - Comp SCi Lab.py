''' Rye Ledford - Comp science lab - Program 9'''

import csv


def months_(c):
    cal = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    return cal[str(c)]

def read_file(file_name):
    data = []
    try:
        f = open(file_name,'r',encoding='UTF-8')
    except:
        return -1
    read = csv.reader(f)
    for row in read:
        data.append(row)
    f.close()
    return data

def dict_column(data,name):
    dict_ex = {}
    c = data[0].index(name)
    for sub in data[1:]:
        if sub[c]in dict_ex:
            dict_ex[sub[c]]+=1
        else:
            dict_ex[sub[c]]=1
    return dict_ex

def date_dict(data):
    return dict_column(data,'Reported_Date')

def offense_dict(data):
    return dict_column(data,"Offense")

def reported_dict(data):
    dict_ex = {}
    for sub in data[1:]:
        temp = sub[1][0:2]
        if temp in dict_ex:
            dict_ex[temp]+=1
        else:
            dict_ex[temp]=1
    return dict_ex

def off_zip(data):
    dict_ex={}
    for sub in data[1:]:
        temp = sub[7]
        if temp in dict_ex:
            temp_dict = dict_ex[temp]
            if sub[13] in temp_dict:
                temp_dict[sub[13]]+=1
            else:
                temp_dict[sub[13]] = 1
        else:
            dict_ex[temp] = {sub[13]:1}
    return dict_ex

    
def search():
    print()
    again = input('Would you like to complete another search? Enter Y/n ==> ')
    print()
    if again == 'Y' or again == 'y':
        return main()
    elif again == 'N' or again == 'n':
        print()
        return goodbye()
    else:
        print('Please enter a valid option')
        print()
        return search()

def goodbye():
    print('Thank you for using the KCPD Crime Database, have a great day.')
    exit(main)
            

def main():
    while(True):
        file_name = input("Enter the name of the crime data file ==> ")
        data = read_file(file_name)
        if(data==-1):
            print("Could not find the file. ", file_name, " was not found")
        else:
            break
    month = reported_dict(data)
    print(month)
    mx = max(month,key=month.get)
    print()
    print("The month with the highest # of crimes is ", months_(mx), " with ", str(month[mx]), " offenses")
    offense = offense_dict(data)
    mx = max(offense,key=offense.get)
    print()
    print("The offense with the highest # of crimes is ", mx, " with ",str(offense[mx]), " offenses")
    offense = off_zip(data)
    print()
    while(True):
        offense1 = input("Enter an offense; ")
        if offense1 not in offense:
            print("Not a valid offense, please try again")
            print()
        else:
            break
    print(offense1, " offense by Zip Code")
    print("Zip Code\t\t\t# Offenses")
    print("==========================================")
    for k,v in offense[offense1].items():
        print(k,"\t\t\t\t\t", str(v))
    return search()

if __name__ == "__main__":
    main()

main()
