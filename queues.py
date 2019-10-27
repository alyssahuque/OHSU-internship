'''
Creates a queue, adds the list containing data record information
(which are called fro parse_OHSU.py), and then iterates through the
queue, removing a list and printing an XML file that follows the OMOP
standards (which calls on print_OMOP_xml.py). Each functions takes an
input of a list and prints out the XML documents. These are the
functions that are called in main.py.
'''

import parse_OHSU as pohsu
import print_OMOP_xml as pxml
import debugging as debug


class Queue: # apparently Python has a library for Queues which I did not know of
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		if self.items == []:
			return None
			sys.exit(1)
		return self.items.pop()

	def size(self):
		return len(self.items)


def q_administered_medications(data_set):
	'''adds the list containing data records of administered_medications
	to a queue and continuously removes a list and prints an OMOP DRUG_EXPOSURE
	XML document until the queue is empty'''
	administered_medications_queue = Queue()
	for i in range(len(pohsu.administered_medications(data_set))):
		administered_medications_queue.enqueue(pohsu.administered_medications(data_set)[i])
	while administered_medications_queue.isEmpty() != True:
		data_record = administered_medications_queue.dequeue()
		pxml.print_administered_medications_DRUG_EXPOSURE(data_record)

def q_ambulatory_encounters(data_set):
	'''adds the list containing data records of ambulatory_encounters
	to a queue and continuously removes a list and prints an OMOP VISIT_OCCURRENCE
	XML document until the queue is empty'''
	ambulatory_encounters_queue = Queue()
	for i in range(len(pohsu.ambulatory_encounters(data_set))):
		ambulatory_encounters_queue.enqueue(pohsu.ambulatory_encounters(data_set)[i])
	while ambulatory_encounters_queue.isEmpty() != True:
		data_record = ambulatory_encounters_queue.dequeue()
		pxml.print_ambulatory_encounters_VISIT_OCCURRENCE(data_record)

def q_current_medications(data_set):
	'''adds the list containing data records of current_medications
	to a queue and continuously removes a list and prints an OMOP DRUG_EXPOSURE
	XML document until the queue is empty'''
	current_medication_queue = Queue()
	for i in range(len(pohsu.current_medications(data_set))):
		current_medication_queue.enqueue(pohsu.current_medications(data_set)[i])
	while current_medication_queue.isEmpty() != True:
		data_record = current_medication_queue.dequeue()
		pxml.print_current_medications_DRUG_EXPOSURE(data_record)

def q_demographics(data_set):
	'''adds the list containing data records of demographics
	to a queue and continuously removes a list and prints an OMOP PERSON
	and LOCATION XML document until the queue is empty'''
	demographics_queue = Queue()
	for i in range(len(pohsu.demographics(data_set))):
		demographics_queue.enqueue(pohsu.demographics(data_set)[i])
	while demographics_queue.isEmpty() != True:
		data_record = demographics_queue.dequeue()
		pxml.print_demographics_PERSON_LOCATION(data_record)

def q_encounter_attributes(data_set):
	'''adds the list containing data records of encounter_attributes
	to a queue and continuously removes a list and prints an OMOP VISIT_OCCURRENCE
	XML document until the queue is empty'''
	encounter_attributes_queue = Queue()
	for i in range(len(pohsu.encounter_attributes(data_set))):
		encounter_attributes_queue.enqueue(pohsu.encounter_attributes(data_set)[i])
	while encounter_attributes_queue.isEmpty() != True:
		data_record = encounter_attributes_queue.dequeue()
		pxml.print_encounter_attributes_VISIT_OCCURRENCE(data_record)

def q_encounter_diagnosis(data_set):
	'''adds the list containing data records of encounter_diagnosis
	to a queue and continuously removes a list and prints an OMOP CONDITION_OCCURRENCE
	XML document until the queue is empty'''
	encounter_diagnosis_queue = Queue()
	for i in range(len(pohsu.encounter_diagnosis(data_set))):
		encounter_diagnosis_queue.enqueue(pohsu.encounter_diagnosis(data_set)[i])
	while encounter_diagnosis_queue.isEmpty() != True:
		data_record = encounter_diagnosis_queue.dequeue()
		pxml.print_encounter_diagnosis_CONDITION_OCCURRENCE_elements(data_record)

def q_hospital_encounters(data_set):
	'''adds the list containing data records of hospital_encounters
	to a queue and continuously removes a list and prints an OMOP CONDITION_OCCURRENCE
	XML document until the queue is empty'''
	hospital_encounters_queue = Queue()
	for i in range(len(pohsu.hospital_encounters(data_set))):
		hospital_encounters_queue.enqueue(pohsu.hospital_encounters(data_set)[i])
	while hospital_encounters_queue.isEmpty() != True:
		data_record = hospital_encounters_queue.dequeue()
		pxml.print_hospital_encounters_CONDITION_OCCURRENCE_elements(data_record)

def q_lab_results(data_set):
	'''adds the list containing data records of lab_results
	to a queue and continuously removes a list and prints an OMOP MEASUREMENT
	XML document until the queue is empty'''
	lab_results_queue = Queue()
	for i in range(len(pohsu.lab_results(data_set))):
		lab_results_queue.enqueue(pohsu.lab_results(data_set)[i])
	while lab_results_queue.isEmpty() != True:
		data_record = lab_results_queue.dequeue()
		pxml.print_lab_results_MEASUREMENT(data_record)
		
def q_medications_ordered(data_set):
	'''adds the list containing data records of medications_ordered
	to a queue and continuously removes a list and prints an OMOP DRUG_EXPOSURE
	XML document until the queue is empty'''
	medications_ordered_queue = Queue()
	for i in range(len(pohsu.medications_ordered(data_set))):
		medications_ordered_queue.enqueue(pohsu.medications_ordered(data_set)[i])
	while medications_ordered_queue.isEmpty() != True:
		data_record = medications_ordered_queue.dequeue()
		pxml.print_medications_ordered_DRUG_EXPOSURE(data_record)

def q_microbiology_results(data_set):
	'''adds the list containing data records of microbiology_results
	to a queue and continuously removes a list and prints an OMOP MEASUREMENT
	XML document until the queue is empty'''
	microbiology_results_queue = Queue()
	for i in range(len(pohsu.microbiology_results(data_set))):
		microbiology_results_queue.enqueue(pohsu.microbiology_results(data_set)[i])
	while microbiology_results_queue.isEmpty() != True:
		data_record = microbiology_results_queue.dequeue()
		pxml.print_microbiology_results_MEASUREMENT(data_record)
		pxml.print_microbiology_results_SPECIMEN(data_record)

def q_notes(data_set):
	'''adds the list containing data records of notes
	to a queue and continuously removes a list and prints an OMOP NOTE
	XML document until the queue is empty'''
	notes_queue = Queue()
	for i in range(len(pohsu.notes(data_set))):
		notes_queue.enqueue(pohsu.notes(data_set)[i])
	while notes_queue.isEmpty() != True:
		data_record = notes_queue.dequeue()
		pxml.print_notes_NOTE(data_record)

def q_problem_list(data_set):
	'''adds the list containing data records of problem_list
	to a queue and continuously removes a list and prints an OMOP CONDITION_OCCURRENCE
	XML document until the queue is empty'''
	problem_list_queue = Queue()
	for i in range(len(pohsu.problem_list(data_set))):
		problem_list_queue.enqueue(pohsu.problem_list(data_set)[i])
	while problem_list_queue.isEmpty() != True:
		data_record = problem_list_queue.dequeue()
		pxml.print_problem_list_CONDITION_OCCURRENCE(data_record)

def q_procedures_ordered(data_set):
	'''adds the list containing data records of procedures_ordered
	to a queue and continuously removes a list and prints an OMOP PROCEDURE_OCCURRENCE
	XML document until the queue is empty'''
	procedures_ordered_queue = Queue()
	for i in range(len(pohsu.procedures_ordered(data_set))):
		procedures_ordered_queue.enqueue(pohsu.procedures_ordered(data_set)[i])
	while procedures_ordered_queue.isEmpty() != True:
		data_record = procedures_ordered_queue.dequeue()
		pxml.print_surgeries_CONDITION_OCCURRENCE(data_record)

def q_result_comments(data_set):
	'''adds the list containing data records of result_comments
	to a queue and continuously removes a list and prints an OMOP NOTE
	XML document until the queue is empty'''
	result_comments_queue = Queue()
	for i in range(len(pohsu.result_comments(data_set))):
		result_comments_queue.enqueue(pohsu.result_comments(data_set)[i])
	while result_comments_queue.isEmpty() != True:
		data_record = result_comments_queue.dequeue()
		pxml.print_result_comments_NOTE(data_record)

def q_surgeries(data_set):
	'''adds the list containing data records of surgeries
	to a queue and continuously removes a list and prints an OMOP PROCEDURE_OCCURRENCE
	XML document until the queue is empty'''
	surgeries_queue = Queue()
	for i in range(len(pohsu.surgeries(data_set))):
		surgeries_queue.enqueue(pohsu.surgeries(data_set)[i])
	while surgeries_queue.isEmpty() != True:
		data_record = surgeries_queue.dequeue()
		pxml.print_surgeries_PROCEDURE_OCCURRENCE(data_record)

def q_vitals(data_set):
	'''adds the list containing data records of vitals
	to a queue and continuously removes a list and prints an OMOP MEASUREMENT
	XML document until the queue is empty'''
	vitals_queue = Queue()
	for i in range(len(pohsu.vitals(data_set))):
		vitals_queue.enqueue(pohsu.vitals(data_set)[i])
	while vitals_queue.isEmpty() != True:
		data_record = vitals_queue.dequeue()
		pxml.print_vitals_MEASUREMENT(data_record)

'''
if __name__ == "__main__":
    q_administered_medications('test_administered_medications.xml')
    q_ambulatory_encounters('test_ambulatory_encounters.xml')
    q_current_medications('test_current_medications.xml')
    q_demographics('test_demographics.xml')
    q_encounter_attributes('test_encounter_attributes.xml')
    q_encounter_diagnosis('test_encounter_diagnosis.xml')
    q_hospital_encounters('test_hospital_encounters.xml')
    q_lab_results('test_lab_results.xml')
    q_medications_ordered('test_medications_ordered.xml')
    q_microbiology_results('test_microbiology_results.xml')
    q_notes('test_notes.xml')
    q_problem_list('test_problem_list.xml')
    q_procedures_ordered('test_procedures_ordered.xml')
    q_result_comments('test_result_comments.xml')
    q_surgeries('test_surgeries.xml')
    q_vitals('test_vitals.xml'
 '''