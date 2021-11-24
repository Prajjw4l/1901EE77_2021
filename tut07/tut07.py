import pandas as pd

reg_feed_dict = {} 
feedback_dict = {}
courses_dict = {} 
stud_dict = {}

#columns for the output file 
OUTPUT_HEADERS = [ 
	"Rollno",
	"Register_Sem",
	"Schedule_Sem",
	"Subno",
	"Name",
	"Email",
	"Aemail",
	"Contact",
]

"""
i have created the mask for the LTP 
EX-> L-T-P => 3-2-0 the binery mask will be => 1-1-0
instead of bit count 
"""
def populate_dicts(): #functiion to initialise all the dictioneries 
	global courses_dict 
	global stud_dict 
	global reg_feed_dict
	course_master_file = pd.read_csv("course_master_dont_open_in_excel.csv")
	for j, row in course_master_file.iterrows():
		LTP = str(row["ltp"]).split("-") #list to store the L-T-P seperately 
		LTP_MASK = 0  #initialing mask
		for i, b in enumerate(LTP):
			LTP_MASK |= (int(float(b)) and 1) << (2 - i) #updating mask bits on the basis of b is non- zero or zero 
		courses_dict[row["subno"]] = LTP_MASK #mapping the subject code to its binery mask 
		
   
	students_file = pd.read_csv("studentinfo.csv")
	"""
	initialising the student dictionary 
	"""
	for j, row in students_file.iterrows():
		stud_dict[row["Roll No"]] = { 
			"Name": row["Name"],
			"Email": row["email"],
			"Aemail": row["aemail"],
			"Contact": row["contact"],
		}


	reg_feedback_file = pd.read_csv("course_registered_by_all_students.csv")
	"""
	creating the unic key for the particular student with concatenation of student roll_no and
	subject number along with - in the middle and then it is mapped to register_sem and scheduled
	sem 
	"""
	for j, row in reg_feedback_file.iterrows():
		reg_feed_dict[str(row['rollno']) + '-' + str(row['subno'])] = {
				"register_sem": row['register_sem'],
				"schedule_sem": row['schedule_sem'],
				}


def given_feedback():
	global feedback_dict
	given_feedback_file = pd.read_csv("course_feedback_submitted_by_students.csv")
	for j, row in given_feedback_file.iterrows(): #if key doesnot exist the key is initialse to 0
		feedback_dict.setdefault(str(row['stud_roll']) + '-' + str(row['course_code']), 0)
		"""given feebback value by students we make a given_mask from it and use it for future comparison
		   the feedback_dictionary is mapped with  key to given mask(feedback type provided by the students)  
		 """
		feedback_dict[str(row['stud_roll']) + '-' + str(row['course_code'])] |= 1 << (3 - int(row['feedback_type'])) 


def remaining_feedback_update():
	global OUTPUT_HEADERS
	remaining_feedback = pd.DataFrame(columns=OUTPUT_HEADERS) #remaining dataframe is the required output we want to get in dataframe
	for key, feedback_val in feedback_dict.items():
		roll, course = key.split('-')
		"""if L-T_P are all 0 and L-T-P mask does not macth with required L-T-P mask then it is appended in 
		the remaning feedback dictionary and later it is converted to excel file 
		"""
		if courses_dict[course] !=0 and courses_dict[course]!=feedback_val:
			remaining_feedback = remaining_feedback.append({
				"Rollno": roll,
				"Register_Sem": reg_feed_dict[key]['register_sem'],
				"Schedule_Sem": reg_feed_dict[key]['schedule_sem'],
				"Subno": course,
				"Name": stud_dict[roll]["Name"],
				"Email": stud_dict[roll]["Email"],
				"Aemail": stud_dict[roll]["Aemail"],
				"Contact": stud_dict[roll]["Contact"],
				}, ignore_index=True)
	remaining_feedback.to_excel("course_feedback_remaining.xlsx", index=False)


def feedback_not_submitted():
	populate_dicts()
	given_feedback()
	remaining_feedback_update()




feedback_not_submitted()