'''
This file contains the xml structure for the OMOP CDM xml files. The functions have
the same name as the relevant OMOP table. The input to all the functions is the root
element and collected_data, a list that has been dequeued. This file is only utilized
for print_OMOP_xml.py in order to allow for repeated calls to print an xml file and clean
up print_OMOP_xml.py.
'''

import xml.etree.ElementTree as et
import mapping as mapp

def administered_medications_DRUG_EXPOSURE_elements(root, collected_data):
	'''indexes the administered_medications list and maps the OHSU data fields to
	the OMOP structure for the DRUG_EXPOSURE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "drug_exposure_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "drug_concept_id").text = None
	et.SubElement(record, "drug_exposure_start_date").text = collected_data[3]
	et.SubElement(record, "drug_exposure_start_datetime").text = collected_data[3]
	et.SubElement(record, "drug_expsoure_end_date").text = collected_data[4]
	et.SubElement(record, "drug_expsoure_end_datetime").text = collected_data[4]
	et.SubElement(record, "verbatim_end_date").text = None
	et.SubElement(record, "drug_type_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "refills").text = None
	et.SubElement(record, "quantity").text = None
	et.SubElement(record, "days_supply").text = None
	et.SubElement(record, "sig").text = collected_data[7]
	et.SubElement(record, "route_concept_id").text = None
	et.SubElement(record, "lot_number").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "drug_source_value").text = collected_data[2]
	et.SubElement(record, "drug_source_concept_id").text = None
	et.SubElement(record, "route_source_value").text = collected_data[5]
	et.SubElement(record, "dose_unit_source_value").text = collected_data[6]

def ambulatory_encounters_VISIT_OCCURRENCE_elements(root, collected_data):
	'''indexes the ambulatory_encounters list and maps the OHSU data fields to
	the OMOP structure for the VISIT_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "visit_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "visit_concept_id").text = None
	et.SubElement(record, "visit_start_date").text = collected_data[2]
	et.SubElement(record, "visit_start_datetime").text = collected_data[2]
	et.SubElement(record, "visit_end_date").text = collected_data[2]
	et.SubElement(record, "visit_end_datetime").text = collected_data[2]
	et.SubElement(record, "visit_type_concept_id").text = None #mapp.visit_type_concept_id(collected_data[3]) # need to write a function to map
	et.SubElement(record, "provider_id").text = collected_data[5]
	et.SubElement(record, "care_site_id").text = None
	et.SubElement(record, "visit_source_value").text = collected_data[4]
	et.SubElement(record, "visit_source_concept_id").text = collected_data[1]
	et.SubElement(record, "admitted_from_concept_id").text = None
	et.SubElement(record, "admitted_from_source_value").text = None
	et.SubElement(record, "discharge_to_concept_id").text = None
	et.SubElement(record, "discharge_to_source_value").text = None
	et.SubElement(record, "preceding_visit_occurrence_id").text = None

def current_medications_DRUG_EXPOSURE_elements(root, collected_data):
	'''indexes the current_medications list and maps the OHSU data fields to
	the OMOP structure for the DRUG_EXPOSURE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "drug_exposure_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "drug_concept_id").text = None
	et.SubElement(record, "drug_exposure_start_date").text = None
	et.SubElement(record, "drug_exposure_start_datetime").text = None
	et.SubElement(record, "drug_expsoure_end_date").text = collected_data[1]
	et.SubElement(record, "drug_expsoure_end_datetime").text = collected_data[1]
	et.SubElement(record, "verbatim_end_date").text = None
	et.SubElement(record, "drug_type_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "refills").text = None
	et.SubElement(record, "quantity").text = None
	et.SubElement(record, "days_supply").text = None
	et.SubElement(record, "sig").text = None
	et.SubElement(record, "route_concept_id").text = None
	et.SubElement(record, "lot_number").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = None
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "drug_source_value").text = collected_data[2]
	et.SubElement(record, "drug_source_concept_id").text = None
	et.SubElement(record, "route_source_value").text = collected_data[3]
	et.SubElement(record, "dose_unit_source_value").text = None

def demographics_PERSON_elements(root, collected_data):
	'''indexes the demographics list and maps the OHSU data fields to
	the OMOP structure for the PERSON table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "gender_concept_id").text = None # Athena
	et.SubElement(record, "year_of_birth").text = collected_data[1][6:10]
	et.SubElement(record, "month_of_birth").text = collected_data[1][0:2]
	et.SubElement(record, "day_of_birth").text = collected_data[1][3:5]
	et.SubElement(record, "birth_datetime").text = collected_data[1]
	et.SubElement(record, "death_datetime").text = collected_data[5]
	et.SubElement(record, "race_concept_id").text = None # Athena
	et.SubElement(record, "ethnicity_concept_id").text = None # Athena
	et.SubElement(record, "location_id").text = str(count()) # unique ID from location table
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "care_site_id").text = None
	et.SubElement(record, "person_source_value").text = collected_data[7] + ' ' + collected_data[6]
	et.SubElement(record, "gender_source_value").text = collected_data[2]
	et.SubElement(record, "gender_source_concept_id").text = None
	et.SubElement(record, "race_source_value").text = collected_data[4]
	et.SubElement(record, "race_source_concept_id").text = None
	et.SubElement(record, "ethnicity_source_value").text = collected_data[3]
	et.SubElement(record, "ethnicity_source_concept_id").text = None

def demographics_LOCATION_elements(root, collected_data):
	'''indexes the demographics list and maps the OHSU data fields to
	the OMOP structure for the LOCATION table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "location_id").text = str(count())
	et.SubElement(record, "address_1").text = collected_data[9]
	et.SubElement(record, "address_2").text = collected_data[10]
	et.SubElement(record, "city").text = collected_data[8]
	et.SubElement(record, "state").text = collected_data[11]
	et.SubElement(record, "zip").text = collected_data[12]
	et.SubElement(record, "county").text = collected_data[13]
	et.SubElement(record, "country").text = None
	et.SubElement(record, "location_source_value").text = None
	et.SubElement(record, "latitude").text = None
	et.SubElement(record, "longitude").text = None

def encounter_attributes_VISIT_OCCURRENCE_elements(root, collected_data):
	'''indexes the encounter_attributes list and maps the OHSU data fields to
	the OMOP structure for the VISIT_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "visit_occurrence_id").text = collected_data[0]
	et.SubElement(record, "person_id").text = collected_data[1]
	et.SubElement(record, "visit_concept_id").text = None
	et.SubElement(record, "visit_start_date").text = collected_data[2]
	et.SubElement(record, "visit_start_datetime").text = collected_data[2]
	et.SubElement(record, "visit_end_date").text = collected_data[3]
	et.SubElement(record, "visit_end_datetime").text = collected_data[3]
	et.SubElement(record, "visit_type_concept_id").text = collected_data[5] # + " or " + collected_data[6] + " or " + collected_data[7] # mapp.visit_type_concept_id(collected_data[])
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "care_site_id").text = None
	et.SubElement(record, "visit_source_value").text = collected_data[4] # mapp.visit_source_value(collected_data[4])
	et.SubElement(record, "visit_source_concept_id").text = None
	et.SubElement(record, "admitted_from_concept_id").text = None
	et.SubElement(record, "admitted_from_source_value").text = None
	et.SubElement(record, "discharge_to_concept_id").text = None
	et.SubElement(record, "discharge_to_source_value").text = None
	et.SubElement(record, "preceding_visit_occurrence_id").text = None

def encounter_diagnosis_CONDITION_OCCURRENCE_elements(root, collected_data):
	'''indexes the encounter_diagnosis list and maps the OHSU data fields to
	the OMOP structure for the CONDITION_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "condition_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "condition_concept_id").text = None
	et.SubElement(record, "condition_start_date").text = collected_data[2]
	et.SubElement(record, "condition_start_datetime").text = collected_data[2]
	et.SubElement(record, "condition_end_date").text = collected_data[2]
	et.SubElement(record, "condition_end_datetime").text = collected_data[2]
	et.SubElement(record, "condition_type_concept_id").text = None
	et.SubElement(record, "condition_status_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "condition_source_value").text = collected_data[10]
	et.SubElement(record, "condition_source_concept_id").text = collected_data[9]
	et.SubElement(record, "condition_status_source_value").text = None

def hospital_encounters_CONDITION_OCCURRENCE_elements(root, collected_data):
	'''indexes the hospital_encounters list and maps the OHSU data fields to
	the OMOP structure for the CONDITION_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "condition_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "condition_concept_id").text = None
	et.SubElement(record, "condition_start_date").text = collected_data[3]
	et.SubElement(record, "condition_start_datetime").text = collected_data[3]
	et.SubElement(record, "condition_end_date").text = collected_data[4]
	et.SubElement(record, "condition_end_datetime").text = collected_data[4]
	et.SubElement(record, "condition_type_concept_id").text = None
	et.SubElement(record, "condition_status_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "condition_source_value").text = collected_data[6]
	et.SubElement(record, "condition_source_concept_id").text = collected_data[5]
	et.SubElement(record, "condition_status_source_value").text = None

def lab_results_MEASUREMENT_elements(root, collected_data):
	'''indexes the lab_results list and maps the OHSU data fields to
	the OMOP structure for the MEASUREMENT table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "measurement_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "measurement_concept_id").text = None
	et.SubElement(record, "measurement_date").text = collected_data[2] # [0]
	et.SubElement(record, "measurement_datetime").text = collected_data[2]
	et.SubElement(record, "measurement_time").text = collected_data[2] # [1]
	et.SubElement(record, "measurement_type_concept_id").text = None
	et.SubElement(record, "operator_concept_id").text = None
	et.SubElement(record, "value_as_number").text = None
	et.SubElement(record, "value_as_concept_id").text = None
	et.SubElement(record, "unit_concept_id").text = None
	et.SubElement(record, "quantity").text = None
	et.SubElement(record, "range_low").text = None
	et.SubElement(record, "range_high").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "measurement_source_value").text = collected_data[3]
	et.SubElement(record, "measurement_source_concept_id").text = None
	et.SubElement(record, "unit_source_value").text = None
	et.SubElement(record, "value_source_value").text = collected_data[4]

def medications_ordered_DRUG_EXPOSURE_elements(root, collected_data):
	'''indexes the medications_ordered list and maps the OHSU data fields to
	the OMOP structure for the DRUG_EXPOSURE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "drug_exposure_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "drug_concept_id").text = None
	et.SubElement(record, "drug_exposure_start_date").text = collected_data[2]
	et.SubElement(record, "drug_exposure_start_datetime").text = collected_data[2]
	et.SubElement(record, "drug_expsoure_end_date").text = collected_data[3]
	et.SubElement(record, "drug_expsoure_end_datetime").text = collected_data[3]
	et.SubElement(record, "verbatim_end_date").text = None
	et.SubElement(record, "drug_type_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "refills").text = None
	et.SubElement(record, "quantity").text = collected_data[6]
	et.SubElement(record, "days_supply").text = None
	et.SubElement(record, "sig").text = collected_data[7]
	et.SubElement(record, "route_concept_id").text = None
	et.SubElement(record, "lot_number").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "drug_source_value").text = collected_data[4]
	et.SubElement(record, "drug_source_concept_id").text = None
	et.SubElement(record, "route_source_value").text = collected_data[5]
	et.SubElement(record, "dose_unit_source_value").text = collected_data[8]

def microbiology_results_MEASUREMENT_elements(root, collected_data):
	'''indexes the microbiology_results list and maps the OHSU data fields to
	the OMOP structure for the MEASUREMENT table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "measurement_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "measurement_concept_id").text = None
	et.SubElement(record, "measurement_date").text = collected_data[3][0:9]
	et.SubElement(record, "measurement_datetime").text = collected_data[3]
	et.SubElement(record, "measurement_time").text = collected_data[3][11:15]
	et.SubElement(record, "measurement_type_concept_id").text = None
	et.SubElement(record, "operator_concept_id").text = None
	et.SubElement(record, "value_as_number").text = collected_data[7]
	et.SubElement(record, "value_as_concept_id").text = None
	et.SubElement(record, "unit_concept_id").text = None
	et.SubElement(record, "quantity").text = collected_data[8]
	et.SubElement(record, "range_low").text = None
	et.SubElement(record, "range_high").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "measurement_source_value").text = collected_data[11]
	et.SubElement(record, "measurement_source_concept_id").text = collected_data[4] + ' OR ' + collected_data[12]
	et.SubElement(record, "unit_source_value").text = None
	et.SubElement(record, "value_source_value").text = None

def microbiology_results_SPECIMEN_elements(root, collected_data):
	'''indexes the microbiology_results list and maps the OHSU data fields to
	the OMOP structure for the SPECIMEN table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "specimen_id").text = None
	et.SubElement(record, "person_id").text = None
	et.SubElement(record, "specimen_concept_id").text = None
	et.SubElement(record, "specimen_type_concept_id") = collected_data[4]
	et.SubElement(record, "specimen_date").text = collected_data[2][0:9]
	et.SubElement(record, "specimen_datetime").text = collected_data[2]
	et.SubElement(record, "quantity").text = collected_data[8]
	et.SubElement(record, "unit_concept_id").text = None
	et.SubElement(record, "anatomic_site_concept_id").text = collected_data[5]
	et.SubElement(record, "disease_status_concept_id").text = None
	et.SubElement(record, "specimen_source_id").text = None
	et.SubElement(record, "specimen_source_value").text = collected_data[10]
	et.SubElement(record, "unit_source_value").text = None
	et.SubElement(record, "anatomic_site_source_value").text = None
	et.SubElement(record, "disease_status_source_value").text = None

def notes_NOTE_elements(root, collected_data):
	'''indexes the notes list and maps the OHSU data fields to
	the OMOP structure for the NOTE table'''
	root = et.Element('NOTE')
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "note_id").text = collected_data[2]
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "note_event_id").text = None
	et.SubElement(record, "note_event_field_concept_id").text = None
	et.SubElement(record, "note_date").text = collected_data[4]
	et.SubElement(record, "note_datetime").text = collected_data[4]
	et.SubElement(record, "note_type_concept_id").text = collected_data[3]
	et.SubElement(record, "note_class_concept_id").text = None
	et.SubElement(record, "note_title").text = None
	et.SubElement(record, "note_text").text = collected_data[7]
	et.SubElement(record, "encoding_concept_id").text = None
	et.SubElement(record, "language_concept_id").text = None
	et.SubElement(record, "provider_id").text = collected_data[5]
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "note_source_value").text = None

def problem_list_CONDITION_OCCURRENCE_elements(root, collected_data):
	'''indexes the problem_list list and maps the OHSU data fields to
	the OMOP structure for the CONDITION_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "condition_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "condition_concept_id").text = None
	et.SubElement(record, "condition_start_date").text = collected_data[3]
	et.SubElement(record, "condition_start_datetime").text = collected_data[3]
	et.SubElement(record, "condition_end_date").text = collected_data[4]
	et.SubElement(record, "condition_end_datetime").text = collected_data[4]
	et.SubElement(record, "condition_type_concept_id").text = None
	et.SubElement(record, "condition_status_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = None
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "condition_source_value").text = collected_data[7]
	et.SubElement(record, "condition_source_concept_id").text = collected_data[6]
	et.SubElement(record, "condition_status_source_value").text = collected_data[5]

def procedures_ordered_PROCEDURE_OCCURRENCE_elements(root, collected_data):
	'''indexes the procedures_ordered list and maps the OHSU data fields to
	the OMOP structure for the PROCEDURE_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "procedure_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "procedure_concept_id").text = None
	et.SubElement(record, "procedure_date").text = collected_data[2]
	et.SubElement(record, "procedure_datetime").text = collected_data[2]
	et.SubElement(record, "procedure_type_concept_id").text = None
	et.SubElement(record, "modifier_concept_id").text = None
	et.SubElement(record, "quantity").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "procedure_source_value").text = collected_data[3]
	et.SubElement(record, "procedure_source_concept_id").text = collected_data[4]
	et.SubElement(record, "modifier_source_value").text = None

def result_comments_NOTE_elements(root, collected_data):
	# indexes the result_comments list and maps the OHSU data fields to
	# the OMOP structure for the NOTE table
	root = et.Element('NOTE')
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "note_id").text = None
	et.SubElement(record, "person_id").text = None
	et.SubElement(record, "note_event_id").text = None
	et.SubElement(record, "note_event_field_concept_id").text = None
	et.SubElement(record, "note_date").text = None
	et.SubElement(record, "note_datetime").text = None
	et.SubElement(record, "note_type_concept_id").text = None
	et.SubElement(record, "note_class_concept_id").text = None
	et.SubElement(record, "note_title").text = None
	et.SubElement(record, "note_text").text = None
	et.SubElement(record, "encoding_concept_id").text = None
	et.SubElement(record, "language_concept_id").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = None
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "note_source_value").text = None


def surgeries_CONDITION_OCCURRENCE_elements(root, collected_data):
	'''indexes the surgeries list and maps the OHSU data fields to
	the OMOP structure for the CONDITION_OCCURRENCE table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "condition_occurrence_id").text = None
	et.SubElement(record, "person_id").text = collected_data[0]
	et.SubElement(record, "condition_concept_id").text = None
	et.SubElement(record, "condition_start_date").text = collected_data[3]
	et.SubElement(record, "condition_start_datetime").text = collected_data[3]
	et.SubElement(record, "condition_end_date").text = collected_data[4]
	et.SubElement(record, "condition_end_datetime").text = collected_data[4]
	et.SubElement(record, "condition_type_concept_id").text = None
	et.SubElement(record, "condition_status_concept_id").text = None
	et.SubElement(record, "stop_reason").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = collected_data[1]
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "condition_source_value").text = collected_data[11]
	et.SubElement(record, "condition_source_concept_id").text = collected_data[10]
	et.SubElement(record, "condition_status_source_value").text = collected_data[7]

def vitals_MEASUREMENT_elements(root, collected_data):
	'''indexes the vitals list and maps the OHSU data fields to
	the OMOP structure for the MEASUREMENT table'''
	record = et.SubElement(root, 'DATA_RECORD')
	et.SubElement(record, "measurement_id").text = None
	et.SubElement(record, "person_id").text = None
	et.SubElement(record, "measurement_concept_id").text = None
	et.SubElement(record, "measurement_date").text = None
	et.SubElement(record, "measurement_datetime").text = None
	et.SubElement(record, "measurement_time").text = None
	et.SubElement(record, "measurement_type_concept_id").text = None
	et.SubElement(record, "operator_concept_id").text = None
	et.SubElement(record, "value_as_number").text = None
	et.SubElement(record, "value_as_concept_id").text = None
	et.SubElement(record, "unit_concept_id").text = None
	et.SubElement(record, "quantity").text = None
	et.SubElement(record, "range_low").text = None
	et.SubElement(record, "range_high").text = None
	et.SubElement(record, "provider_id").text = None
	et.SubElement(record, "visit_occurrence_id").text = None
	et.SubElement(record, "visit_detail_id").text = None
	et.SubElement(record, "measurement_source_value").text = None
	et.SubElement(record, "measurement_source_concept_id").text = None
	et.SubElement(record, "unit_source_value").text = None
	et.SubElement(record, "value_source_value").text = None
