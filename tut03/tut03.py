import os

def output_by_subject():
    if not os.path.exists("output_by_subject"): 
        os.makedirs("output_by_subject") #used to make new output File 
    file = open("regtable_old.csv", "r") #used to open given CSV file 
    csv_data = file.read().split('\n')  
    final_data = []
    for i in csv_data:
        if i:
            final_data.append(i.split(',')) 
    file.close()
    del final_data[0]
    for i in final_data:
        file_name = os.path.join("output_by_subject", i[3] + ".csv")
        existing_data = ""
        if os.path.exists(file_name):
            file2 = open(file_name, "r")
            existing_data = file2.read()
            file2.close()
        file3 = open(file_name, "a")
        if len(existing_data)==0:
            file3.write('rollno,register_sem,subno,sub_type\n')
        file3.write(i[0] + "," + i[1] + "," + i[3] + "," + i[8] + "\n")
        file3.close()
    file.close()

def output_individual_roll():
    if not os.path.exists("output_individual_roll"):
        os.makedirs("output_individual_roll")
    file = open("regtable_old.csv", "r")
    csv_data = file.read().split('\n')
    final_data = []
    for i in csv_data:
        if i:
            final_data.append(i.split(','))
    file.close()
    del final_data[0]
    for i in final_data:
        file_name = os.path.join("output_individual_roll", i[0] + ".csv")
        existing_data = ""
        if os.path.exists(file_name):
            file3 = open(file_name, "r")
            existing_data = file3.read()
            file3.close()
        file2 = open(file_name, "a") #please note here we have used append here if we run code multiple times then output will be replecated in the same CSv file  
        if len(existing_data) == 0:
            file2.write('rollno,register_sem,subno,sub_type\n')
        file2.write(i[0] + "," + i[1] + "," + i[3] + "," + i[8] + "\n")
        file2.close()
    file.close()

output_individual_roll()
output_by_subject()
