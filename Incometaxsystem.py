display="""
           Sunway College Account Department
                MaitiDevi, Kathmandu
           Welcome to Salary& Tax Calculate System (STCS)"""

# For display the name of the system.
def display_Static_Info():
    print(display)

Staff_No=[]
address=[]
panNo=[]
status=[]
fiscalYear=[]
incomePerMonth=[]

#For inputing the information
def Staff_Info():
    n=int(input("Please enter the number of staff you wanted to provide data"))
    for i in range(n):
        Staff_No.append(input(f"Enter Staff Name [{i+1}]"))
        address.append(input(f"Enter Address [{i+1}] "))
        panNo.append(input(f"Enter Pan No [{i+ 1}]"))
        status.append(input(f"Enter 'Y' for Married and 'N' for Unmarried Status[{i+1}]"))
        fiscalYear.append(input(f"Enter FY[{i + 1 }]"))
        incomePerMonth.append(int(input(f"Enter Staff per month income Rs [{ i + 1}]")))
        display_Static_Info()
        taxAmount,incomeAfterTax=Calculate_Tax_Of_Staff_Married(incomePerMonth[i])
        display_Staff_Info(Staff_No[i],address[i],panNo[i],status[i],fiscalYear[i],incomePerMonth[i],taxAmount,incomeAfterTax)

def Calculate_Tax_Of_Staff(status,income):
    flag
    if status=='Y':
        flag=1
    
    elif status=='N':
        flag=0
    taxAmount=0
    incomeAfterTax=0
    if(flag):
       taxAmount,incomeAfterTax=Calculate_Tax_Of_Staff_Married(income)
       return taxAmount,incomeAfterTax
    else:
        Calculate_Tax_Of_Staff_Unmarried(income)

    
    return taxAmount,incomeAfterTax


def Calculate_Tax_Of_Staff_Married(income):
  taxAmount=0
  incomeAfterTax=0
  if(income<=450000):
    taxAmount=1/ 100 *(income)
    incomeAfterTax= income - taxAmount
  
  elif(income> 450000 and income<=550000):
    extra=income - 450000
    taxAmount= 10 / 100 * (extra) + 1 / 100 * 450000
    incomeAfterTax= income - taxAmount

  elif(income>550000 and income <=750000):
    extra=income - 550000
    taxAmount=  (10/100 * (100000)) + (1/100 *(450000)) + (20/100 * (extra))
    incomeAfterTax=income - taxAmount
  
  elif(income>750000 and income<=2000000):
    extra= income - 750000
    taxAmount= (10/100 *(100000)) + (1/100 *(450000))+ (20/100 *(200000)) + (30/100 * (extra))
    incomeAfterTax=income - taxAmount

  elif(income>2000000):
    extra=income - 2000000
    taxAmount=(10/100 *(100000)) + (1/100 *(450000))+ (20/100 *(200000)) + (30/100 * (1250000)) + (36/100 * (extra))

  return taxAmount, incomeAfterTax

#Finishing later
def Calculate_Tax_Of_Staff_Unmarried():
   pass

def display_Staff_Info(name,address,panNo,status,fiscalyear,income,taxAmount,incomeAfterTax):
    print("Staff name:"+ name)
    print("Address:"+ address)
    print("panNo:"+panNo)
    print("Status:"+status)
    print("FiscalYear"+fiscalyear)
    print("Income"+str(income))
    print("Tax amount:"+str(taxAmount))
    print("IncomeAfterTax"+str(incomeAfterTax))

Staff_Info()
    