'''
Prints new OMOP XML file. Calls xml_content.py which contains the
list indices that are printed. Each file that is printed is named
[OMOP table name]_[patient_id].xml. For each function the input is
a list of parsed data from the OHSU data records and the fucntion
prints the new OMOP XML document.
Need to figure out how to print multiple files from same patient
into one file. (i.e. if a patient is taking multiple medications
there will be multiple DRUG_EXPOSURE tables. All DRUG_EXPOSURE 
tables for a patient should be in the same XML file.
'''

import sys
import xml.etree.ElementTree as et
import os
import xml_content as xmlc

def print_administered_medications_DRUG_EXPOSURE(collected_data):
	'''takes a list of administered_medications from OHSU data records and
	reformats to a DRUG_EXPOSURE table that meets OMOP standards'''
	root = et.Element('DRUG_EXPOSURE')
	xmlc.administered_medications_DRUG_EXPOSURE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\DRUG_EXPOSURE_{collected_data[0]}.xml")

def print_ambulatory_encounters_VISIT_OCCURRENCE(collected_data):
	'''takes a list of ambulatory_encounters from OHSU data records and
	reformats to a VISIT_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('VISIT_OCCURRENCE')
	xmlc.ambulatory_encounters_VISIT_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\VISIT_OCCURRENCE_{collected_data[0]}.xml")

def print_current_medications_DRUG_EXPOSURE(collected_data):
	'''takes a list of current_medications from OHSU data records and
	reformats to a DRUG_EXPOSURE table that meets OMOP standards'''
	root = et.Element('DRUG_EXPOSURE')
	xmlc.current_medications_DRUG_EXPOSURE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\DRUG_EXPOSURE_{collected_data[0]}.xml")

def print_demographics_PERSON_LOCATION(collected_data):
	'''takes a list of demographics from OHSU data records and
	reformats to a PERSON and LOCATION table that meets OMOP standards'''
	root = et.Element('PERSON')
	xmlc.demographics_PERSON_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\PERSON_{collected_data[0]}.xml")
	
	root = et.Element('LOCATION')
	xmlc.demographics_LOCATION_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\LOCATION_{collected_data[0]}.xml")

def print_encounter_attributes_VISIT_OCCURRENCE(collected_data):
	'''takes a list of encounter_attributes from OHSU data records and
	reformats to a VISIT_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('VISIT_OCCURRENCE')
	xmlc.encounter_attributes_VISIT_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\VISIT_OCCURRENCE_{collected_data[0]}.xml")

def print_encounter_diagnosis_CONDITION_OCCURRENCE_elements(collected_data):
	'''takes a list of encounter_diagnosis from OHSU data records and
	reformats to a CONDITION_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('CONDITION_OCCURRENCE')
	xmlc.encounter_diagnosis_CONDITION_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\CONDITION_OCCURRENCE_{collected_data[0]}.xml")

def print_hospital_encounters_CONDITION_OCCURRENCE_elements(collected_data):
	'''takes a list of hospital_encounters from OHSU data records and
	reformats to a CONDITION_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('CONDITION_OCCURRENCE')
	xmlc.hospital_encounters_CONDITION_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\CONDITION_OCCURRENCE_{collected_data[0]}.xml")

def print_lab_results_MEASUREMENT(collected_data):
	'''takes a list of lab_results from OHSU data records and
	reformats to a MEASUREMENT table that meets OMOP standards'''
	root = et.Element('MEASUREMENT')
	xmlc.lab_results_MEASUREMENT_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\MEASUREMENT_{collected_data[0]}.xml")

def print_medications_ordered_DRUG_EXPOSURE(collected_data):
	'''takes a list of medications_ordered from OHSU data records and
	reformats to a DRUG_EXPOSURE table that meets OMOP standards'''
	root = et.Element('DRUG_EXPOSURE')
	xmlc.medications_ordered_DRUG_EXPOSURE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C:\\Users\\huque\\Desktop\\data\\DRUG_EXPOSURE_{collected_data[0]}.xml")

def print_microbiology_results_MEASUREMENT(collected_data):
	'''takes a list of microbiology_results from OHSU data records and
	reformats to a MEASUREMENT table that meets OMOP standards'''
	root = et.Element('MEASUREMENT')
	xmlc.microbiology_results_MEASUREMENT_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\DRUG_EXPOSURE_{collected_data[0]}.xml")

def print_microbiology_results_SPECIMEN(collected_data):
	'''takes a list of microbiology_results from OHSU data records and
	reformats to a SPECIMEN table that meets OMOP standards'''
	root = et.Element('SPECIMEN')
	xmlc.microbiology_results_SPECIMEN_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\SPECIMEN_{collected_data[0]}.xml")

def print_notes_NOTE(collected_data):
	'''takes a list of notes from OHSU data records and
	reformats to a NOTE table that meets OMOP standards'''
	root = et.Element('NOTE')
	xmlc.notes_NOTE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\NOTE_{collected_data[0]}.xml")

def print_problem_list_CONDITION_OCCURRENCE(collected_data):
	'''takes a list of problem_list from OHSU data records and
	reformats to a CONDITION_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('CONDITION_OCCURRENCE')
	xmlc.problem_list_CONDITION_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\CONDITION_OCCURRENCE_{collected_data[0]}.xml")

def print_procedures_ordered_PROCEDURE_OCCURRENCE(collected_data):
	'''takes a list of procedures_ordered from OHSU data records and
	reformats to a PROCEDURE_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('PROCEDURE_OCCURRENCE')
	xmlc.procedures_ordered_PROCEDURE_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\PROCEDURE_OCCURRENCE_{collected_data[0]}.xml")
'''
def print_result_comments_NOTE(collected_data):
	# takes a list of result_comments from OHSU data records and
	# reformats to a NOTE table that meets OMOP standards
	root = et.Element('NOTE')
	xmlc.result_comments_NOTE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\NOTE_{collected_data[0]}.xml")
'''
def print_surgeries_PROCEDURE_OCCURRENCE(collected_data):
	'''takes a list of surgeries from OHSU data records and
	reformats to a PROCEDURE_OCCURRENCE table that meets OMOP standards'''
	root = et.Element('PROCEDURE_OCCURRENCE')
	xmlc.surgeries_PROCEDURE_OCCURRENCE_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\PROCEDURE_OCCURRENCE_{collected_data[0]}.xml")

def print_vitals_MEASUREMENT(collected_data):
	'''takes a list of vitals from OHSU data records and
	reformats to a MEASUREMENT_OCCURRENCE table that meets OMOP standards'''
	root = et.ElementTree('MEASUREMENT')
	xmlc.vitals_MEASUREMENT_elements(root, collected_data)

	tree = et.ElementTree(root)

	tree.write(f"C\\Users\\huque\\Desktop\\data\\MEASUREMENT_{collected_data[0]}.xml")

'''
if __name__ == "__main__":
 	print_notes_NOTE(['Z0000000', '00000000', '0123456789', 'CONSULTS', '01/01/2009 00:00', 'SHELL, ALYSSA', 'DOCTOR', 'According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees dont care what humans think is impossible.'])
 '''