In order to run this program type in the file names to main.py and run in terminal.

PROGRAM WORKS IN THESE STEPS:
  1) Parse the OHSU XML source files (parse_OHSU.py)
  2) Store the EHR patient data into a list (parse_OHSU.py)
  3) Add all lists to a queue (queues.py)
  4) Remove one list at a time from the queue (queues.py)
  5) Index the list and assign the information to the OMOP field (xml_content.py)
  6) Print a new XML file that follows the standards and organizational pattern of the OMOP CDM (print_OMOP_xml.py)

FILES (SEE SPECIFIC FILE FOR MORE INFORMATION):
  parse_OHSU.py: parses the OHSU tables, stores information in a list of lists.
  queues.py: makes a queue for each of the OHSU tables, enqueues the list, dequeues one list at a time
  print_OMOP_xml.py: prints xml files
  xml_content.py: contains the file structure for the OMOP CDM xml files
  main.py: runs the whole program, need to type in file names in order to run

OTHER:
  - function naming:
    [OHSU/OMOP table]: parses relevant table
    q_[OHSU table]: creates queue object, enqueues, dequeues for relevant table
    print_[OMOP table]: prints xml file for relevant table
    [OMOP table]_elements: creates xml structure for relevant table
  - file paths:
    within print_OMOP_xml.py it specifies a path in order to print the XML documents. When printing this path needs to be modified.
    If this program is not being run on a windows os, it does not need the "//" within the file paths as this will cause an error.