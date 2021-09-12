import csv
import os
from openpyxl import Workbook,load_workbook

def output_by_subject(item, heading):
    path = os.path.join("output_by_subject", item[2]+".xlsx")            
    if os.path.exists(path) == False:     #create new file if it does not exist
        wb = Workbook()                   
        sheet = wb.active                 
        sheet.append(heading)  #add headings (column names)          
        wb.save(path)   #save excel file                  

    wb = load_workbook(path)  #load excel file             
    sheet = wb.active                     
    sheet.append(item)            
    wb.save(path)                         
    return

def output_individual_roll(item, heading):
    path = os.path.join("output_individual_roll", item[0]+".xlsx")             
    if os.path.exists(path) == False:      
        wb = Workbook()                   
        sheet = wb.active                 
        sheet.append(heading)             
        wb.save(path)                     

    wb = load_workbook(path)              
    sheet = wb.active                     
    sheet.append(item)            
    wb.save(path)                         
    return

subject = "output_by_subject"    
os.mkdir(subject)    #create output folder 

roll_no = "output_individual_roll"    
os.mkdir(roll_no)    


with open('regtable_old.csv', 'r') as read_obj:      
    reader = csv.reader(read_obj)
    row_count = 0
    heading=[]
    for line in reader:       
        if  row_count == 0:   
            heading=[line[0],line[1],line[3],line[8]]     
            row_count += 1
        else:
            item=[line[0],line[1],line[3],line[8]] 
            output_individual_roll(item, heading)    
            output_by_subject(item, heading)        