import statistics, random, csv, os

def split_rank(s):
        head = s.rstrip('0123456789')
        tail = s[len(head):]
        return head, tail

def linear_estimation():
	overall = 0
	ranks = {"VHA": 4, "HA": 3, "SA": 2, "LA": 1, "VLA": 0}
	
	for _ in range(5):
			sub_score = split_rank(input("Subject score: "))
			overall += ( ranks[sub_score[0]] * 10 ) + int(sub_score[1])
	return("OP:",26-(overall/10))

def generate_qcs(students):
	cohort = sum(students)
	mean = sum([students[i] * (-4.28571429*(i^2)+57.14285714*i+100) for i in range(5)])/cohort
	scores = [random.gauss(mean, 25) for _ in range(cohort)]
	
	return scores
	
def generate_sais(cohort):
	if (cohort == 1):
		return [300]
	elif (cohort == 0):
		return []
	SAIs = [i*(200/(cohort-1))+200 for i in range(cohort)]
	return SAIs

def scaled_sais(SAIs, QCS):
	if (len(SAIs) > 2):
		SAI_sd = statistics.stdev(SAIs)	
	else:
		SAI_sd = 75
	
	if (len(QCS) > 2):
		QCS_sd = statistics.stdev(QCS)
	else:
		QCS_sd = 25
	
	SAI_mean = statistics.mean(SAIs)
	QCS_mean = statistics.mean(QCS)
		
	#scaled = [(SAI,((SAI - SAI_mean) / SAI_sd) * QCS_sd + QCS_mean) for SAI in SAIs]
	scaled = [(((SAI - SAI_mean) / SAI_sd) * QCS_sd + QCS_mean) for SAI in SAIs]
	return scaled

def school_enrolements():
	with open('qcaa_stats_subj_part.csv', 'r') as f:
		reader = csv.reader(f)
		attendence = list(reader)
	
	#{ "Cleveland High School": {"English": 50, "Math B": 40}, "Victoria Point High": {"Sport": 41, "Science": 39} }
	last_school = None
	school_index = {}
	queensland_index = {}
	
	for school_subject_students in attendence:		
		if (last_school != school_subject_students[0]): #New school			
			if (last_school != None): #If its NOT the very first row				
				queensland_index[last_school] = school_index
			school_index = {}	
		school_index[school_subject_students[1]] = int(school_subject_students[2])
		last_school = school_subject_students[0]	
	return queensland_index

def get_2015_qcs_results():
	qcs_results = {}
	with open('qcaa_stats_yr12_outcomes_15_all_schools.csv', 'r') as f:
		reader = csv.reader(f)
		qcs_fileinfo = list(reader)
	
	for line in qcs_fileinfo:
		qcs_results[line[0]] = []
		
		for element in line:
			try:
				qcs_results[line[0]].append(int(element))
			except ValueError:
				pass
	
	return qcs_results		
	
def average_to_op(average):
	boundries = [224.5009,214.5619,206.9835,200.8959,195.9845,191.1634,186.1559,181.1579,176.5899,172.5,168.5559,164.8159,161.3169,157.5299,153.7819,149.9219,145.9689,141.8439,138.1579,134.1509,128.5528,123.375,115.0194,105.893,0]
	op = 1	
	
	for i in range(len(boundries)):
		if average > boundries[i]:
			return op
		else:
			op += 1
	
	return "?"	

def main():
	attendence = school_enrolements()
	qcs_results_2015 = get_2015_qcs_results()
	qcs_results_2016 = {}
	
	#STUDENT_SUBJECTS = {"English": 290, "Mathematics B": 315, "Physics": 315, "Technology Studies": 400, "Information Processing & Technology": 325}
	#STUDENT_SUBJECTS = {"English": 200, "Mathematics B": 200, "Physics": 200, "Technology Studies": 200, "Information Processing & Technology": 200}
	#STUDENT_SUBJECTS = {"English": 400, "Mathematics B": 400, "Physics": 400, "Technology Studies": 400, "Information Processing & Technology": 400}
	#STUDENT_SUBJECTS = {"English": 320, "Mathematics A": 320, "Graphics": 320, "Technology Studies": 320, "Information Processing & Technology": 320}
	STUDENT_SUBJECTS = {"English": 400, "Mathematics B": 382, "Mathematics C": 400, "Physics": 365, "Chemistry": 397}
	
	STUDENT_SCHOOL = "Aspley State High School"
	#STUDENT_SCHOOL = "Cleveland District State High School"

	for school in attendence: #Each school where `school` is index
		try:
			qcs_results_2016[school] = generate_qcs(qcs_results_2015[school])
			for subject in attendence[school]:
				sais = generate_sais(attendence[school][subject])
				if school == STUDENT_SCHOOL and subject in STUDENT_SUBJECTS.keys():
					sais.append(STUDENT_SUBJECTS[subject])
				attendence[school][subject] = scaled_sais(sais,qcs_results_2016[school])
		except KeyError:
			pass
	
	
	
	STUDENT_AVERAGE = 0
	for subject in attendence[STUDENT_SCHOOL]:
		if subject in STUDENT_SUBJECTS.keys():
			STUDENT_AVERAGE += attendence[STUDENT_SCHOOL][subject][-1]
			print(attendence[STUDENT_SCHOOL][subject][-1])
	
	average = STUDENT_AVERAGE/5
	print("average",average)
	print("OP",average_to_op(average),"±1")
	
if __name__ == "__main__":
	print("Started",os.path.basename(__file__))
	
	main()
	
	
	
			
			
