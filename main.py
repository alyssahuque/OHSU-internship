'''
Run this file to run entire software program.
'''

import queues as Q

Q.q_administered_medications('test_administered_medications.xml')
Q.q_ambulatory_encounters('test_ambulatory_encounters.xml')
Q.q_current_medications('test_current_medications.xml')
Q.q_demographics('test_demographics.xml')
Q.q_encounter_attributes('test_encounter_attributes.xml')
Q.q_encounter_diagnosis('test_encounter_diagnosis.xml')
Q.q_hospital_encounters('test_hopsital_encounters.xml')
Q.q_lab_results('test_lab_results.xml')
Q.q_medications_ordered('test_medications_ordered.xml')
Q.q_microbiology_results('test_microbiology_results.xml')
Q.q_notes('test_notes.xml')
Q.q_problem_list('test_problem_list.xml')
Q.q_procedures_ordered('test_procedures_ordered.xml')
Q.q_result_comments('test_result_comments.xml')
Q.q_surgeries('test_surgeries.xml')
Q.q_vitals('test_vitals.xml')