'''
This file parses through the OHSU EHR data and stores the information into a list.
The functions have the same name as the relevant OHSU table. The input to all the
functions is the name of the file in which the OHSU EHR data is stored. All functions
return a single list named collected_data. collected_data is composed of lists containing
the information from a DATA_RECORD. collected_data is not sorted so the lists are in the
same order in which the DATA_RECORD appears in the file (so the first list is the first
DATA_RECORD, second list is the second DATA_RECORD, and so on and so forth). Only the
data that has equivalent fields in the OMOP CDM are retained. Any data that does not map
to the CDM is lost at this stage.
'''

import os
import xml.etree.ElementTree as et

def convert_lists_to_dictionary(collected_data):
	'''Stores DATA_RECORDS as a dictionary. Key is
	a numerical value designating in what order the
	info appeared on the XML file and the value is
	a list of  the data. I ended up not needing this
	function but it's here for any later modifications.'''
	collected_data = {idx + 1: entry for idx, entry in enumerate(collected_data)}
	return collected_data

def administered_medications(data_set):
	'''parses the xml file for the administered_medications tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'RX_NAME',
			'RX_ORDER_START_DATE',
			'RX_ORDER_END_DATE',
			'ADMINISTRATION_ROUTE',
			'DOSE',
			'FREQUENCY']])

	return collected_data

def ambulatory_encounters(data_set):
	'''parses the xml file for the ambulatory_encounters tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'ENCOUNTER_DATE',
			'ENCOUNTER_TYPE',
			'DEPARTMENT_NAME',
			'ENCOUNTER_PROVIDER']])

	return collected_data

def current_medications(data_set):
	'''parses the xml file for the current_medications tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'LAST_CURRENT_MEDICATIONS_DATE',
			'MEDICATION_NAME',
			'ADMINISTRATION_ROUTE']])

	return collected_data

def demographics(data_set):
	'''parses the xml file for the demographics tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()
	# print(root.tag) # root is MAIN

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'BIRTH_DATE',
			'GENDER',
			'ETHNICITY',
			'RACE',
			'DEATH_DATE',
			'LAST_NAME',
			'FIRST_NAME',
			'CITY',
			'ADDRESS_LINE1',
			'ADDRESS_LINE2',
			'STATE',
			'ZIP',
			'COUNTY',
			'PRIMARY_CARE_PHYSICIAN']])

	return collected_data

def encounter_attributes(data_set):
	'''parses the xml file for the encounter_attributes tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'ENCOUNTER_FROM_DT',
			'ENCOUNTER_THRU_DT',
			'INPUT_OUTPUT_FLAG',
			'VISIT_CATEGORY',
			'ENCOUNTER_TYPE',
			'VISIT_TYPE']])

	return collected_data

def encounter_diagnosis(data_set):
	'''parses the xml file for the encounter_diagnosis tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()
	# print(root.tag) # root is MAIN

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'DX_DATE',
			'ENCOUNTER_DIAGNOSIS_FLAG',
			'FOLLOWUP_DIAGNOSIS_FLAG',
			'HOSPITAL_ADMIT_FLAG',
			'ORDER_MEDICATION_DX_FLAG',
			'DIAGNOSIS_ICD10_CODE',
			'DIAGNOSIS_ICD10_NAME',]])

	return collected_data

def hospital_encounters(data_set):
	'''parses the xml file for the hospital_encounters tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'HOSPITAL_ACCOUNT_DATE',
			'HOSPITAL_ADMIT_TIME',
			'HOSPITAL_DISCHARGE_TIME',
			'ADMITTING_DIAGNOSIS_ICD_CODE',
			'ADMITTING_DIAGNOSIS_NAME',
			'BILL_DISCHARGE_DIAGNOSIS_ICD_CODE',
			'BILL_DISCHARGE_DIAGNOSIS_NAME',
			'BILL_DIAGNOSIS_2_ICD_CODE',
			'BILL_DIAGNOSIS_2_NAME',
			'BILL_DIAGNOSIS_3_ICD_CODE',
			'BILL_DIAGNOSIS_3_NAME',
			'BILL_DIAGNOSIS_4_ICD_CODE',
			'BILL_DIAGNOSIS_4_NAME',
			'ENCOUNTER_DIAGNOSIS',
			'ENCOUNTER_PROCEDURES',
			'ADMITTED_FROM_ED',
			'ADMISSION_SOURCE',
			'DISCHARGE_LOCATION',
			'DISCHARGE_DESTINATION',
			'DISCHARGE_DISPOSITION',
			'ADMITTING_ICD10_DIAGNOSIS_CODE',
			'ADMITTING_ICD10_DIAGNOSIS_NAME',
			'ENCOUNTER_DIAGNOSIS_ICD10',
			'ENCOUNTER_PROCEDURES_ICD10']])

	return collected_data

def lab_results(data_set):
	'''parses the xml file for the lab_results tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'SPECIMEN__TIME',
			'COMPONENT_NAME',
			'TEXT']])

	return collected_data

def medications_ordered(data_set):
	'''parses the xml file for the medications_ordered tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'PRESCRIPTION_ORDER_PLACED_TIME',
			'PRESCRIPTION_ORDER_START_TIME',
			'PRESCRIPTION_ORDER_END_TIME',
			'PRESCRIPTION_ORDER_TO_START_DATE',
			'PRESCRIPTION_ORDER_TO_END_DATE',
			'PRESCRIPTION_ORDER_DISCONTINUE_TIME',
			'MEDICATION_NAME',
			'GENERIC_NAME_1',
			'GENERIC_NAME_2',
			'ADMINISTRATION_ROUTE',
			'DOSE',
			'FREQUENCY',
			'UNIT']])

	return collected_data

def microbiology_results(data_set):
	'''parses the xml file for the microbiology_results tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'SPECIMEN_TAKEN_TIME',
			'RESULT_DATE_TIME',
			'MASTER_PANEL_NAME',
			'SAMPLE_SOURCE',
			'ISOLATE_NUMBER',
			'TOTAL_ISOLATES',
			'QUANTITY',
			'RESULT_NUMBER',
			'ORGANISM',
			'SUSCEPTIBILITY',
			'SUSCEPTIBILITY_TEST_METHOD',
			'MIC',
			'KIRBY_BAUER',
			'HOSPITAL_ADMIT_TIME',
			'HOSPITAL_DISCHARGE_TIME']])

	return collected_data

def notes(data_set):
	'''parses the xml file for the notes tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'NOTE_ID',
			'NOTE_TYPE',
			'NOTE_DATE',
			'AUTHOR_NAME',
			'AUTHOR_SPECIALTY',
			'NOTE_TEXT']])

	return collected_data

def problem_list(data_set):
	'''parses the xml file for the problem_list tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'DIAGNOSIS_ICD',
			'DIAGNOSIS_NAME',
			'DIAGNOSIS_START_DATE',
			'DIAGNOSIS_END_DATE',
			'PROBLEM_LIST_DIAGNOSIS_STATUS',
			'DIAGNOSIS_ICD10',
			'DIAGNOSIS_ICD10_NAME']])

	return collected_data

def procedures_ordered(data_set):
	'''parses the xml file for the procedures_ordered tables of patients
	and stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'ENCOUNTER_DATE',
			'PROCEDURE_NAME',
			'PROCEDURE_CPT_CODE']])

	return collected_data

def result_comments(data_set):
	'''parses the xml file for the result_comments tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'SPECIMEN_DATE',
			'PROCEDURE_NAME',
			'TEXT']])

	return collected_data

def surgeries(data_set):
	'''parses the xml file for the surgeries tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'HOSPITAL_ACCOUNT_ID',
			'HOSPITAL_ADMIT_TIME',
			'HOSPITAL_DISCHARGE_TIME',
			'SURGERY_DATE',
			'CASE_ID',
			'INPATIENT_OUTPATIENT',
			'PRIMARY_CPT_CODE',
			'PRIMARY_CPT_DESCRIPTION',
			'PRIMARY_DIAGNOSIS_ICD_CODE',
			'PRIMARY_DIAGNOSIS_ICD_NAME',
			'PRIMARY_PROGNOSIS_ICD_CODE',
			'PRIMARY_PROGNOSIS_ICD_NAME',
			'SECONDARY_CPT_CODES',
			'SECONDARY_CPT_DESCRIPTION',
			'SECONDARY_DIAGNOSIS_ICD_CODES',
			'SECONDARY_PROGNOSIS_ICD_CODES',
			'SURGERY_PROCEDURE_DESCRIPTION',
			'PRIMARY_DIAGNOSIS_ICD10_CODE',
			'PRIMARY_DIAGNOSIS_ICD10_NAME',
			'PRIMARY_PROGNOSIS_ICD10_CODE',
			'PRIMARY_PROGNOSIS_ICD10_NAME',
			'SECONDARY_DIAGNOSIS_ICD10_CODES',
			'SECONDARY_PROGNOSIS_ICD10_CODES']])

	return collected_data

def vitals(data_set):
	'''parses the xml file for the vitals tables of patients and
	stores only the information that maps to the OMOP CDM in a list'''
	base_path = os.path.dirname(os.path.realpath(__file__)) # path to this file
	xml_file = os.path.join(base_path, "C:\\Users\\huque\\Desktop\\{}".format(data_set)) # joins path to this file and data set
	tree = et.parse(xml_file) # parses xml file
	root = tree.getroot()

	# creates a list for each DATA_RECORD
	collected_data = []
	for d in root.findall('DATA_RECORD'):
		collected_data.append([d.find(x).text for x in ['OHSU_PAT_ID',
			'OHSU_ENCOUNTER_ID',
			'RECORDED_TIME',
			'BMI',
			'BP_DIASTOLIC',
			'BP_SYSTOLIC',
			'BSA',
			'HEIGHT_CM',
			'WEIGHT_KG',
			'PAIN_SCORE_NUMBER',
			'PAIN_LOCATION_NUMBER',
			'SP02',
			'PULSE',
			'RESPIRATION_RATE',
			'TEMPERATURE_C']])

	return collected_data

'''
if __name__ == "__main__":
    print(administered_medications('test_administered_medications.xml'))
    print(ambulatory_encounters('test_ambulatory_encounters.xml'))
    print(current_medications('test_current_medications.xml'))
    print(demographics('test_demographics.xml'))
    print(encounter_attributes('test_encounter_attributes.xml'))
    print(encounter_diagnosis('test_encounter_diagnosis.xml'))
    print(hospital_encounters('test_hospital_encounters.xml'))
    print(lab_results('test_lab_results.xml'))
    print(medications_ordered('test_medications_ordered.xml'))
    print(microbiology_results('test_microbiology_results.xml'))
    print(notes('test_notes.xml'))
    print(problem_list('test_problem_list.xml'))
    print(procedures_ordered('test_procedures_ordered.xml'))
    print(result_comments('test_result_comments.xml'))
    print(surgeries('test_surgeries.xml'))
    print(vitals('test_vitals.xml'))
'''