**Catalog_Master.py, Editing_Master.py**

The following modules are necessary to successfully execute the catalog master codes. Below are the web sources
as well as installation instruction through command prompt. Python 3.0 or greater is required. Code was
written and executed on Python v. 3.9.7.

Editing_Master.py is the master editing file that contains examples of the code used to evaluate streamflow
catalog to check for misspellings, standardization issues, and empty fields. Many incorrect field edits were 
made manually on a case-by-case basis.

Catalog_Master.py is the python script to sort data and create graph visualizations using matplotlib.


(1) 	
NumPy
version 1.23.1
https://numpy.org/

a) installation through command prompt:
	$pip install numpy
b) double check module was installed correctly:
	$pip show numpy
<show> command will show module name, version number, and file location. <package not found> will indicate
the module didn't install correctly.

(2)
openpyxl 
version 3.0.10
https://openpyxl.readthedocs.io/en/stable/#

a) installation through command prompt:
	$pip install openpyxl
b) double check module was installed correctly:
	$pip show openpyxl
<show> command will show module name, version number, and file location. <package not found> will indicate
the module didn't install correctly.

(3)
matplotlib
version 3.5.2
https://matplotlib.org/

a) installation through command prompt:
	$pip install matplotlib
b) double check module was installed correctly:
	$pip show matplotlib
<show> command will show module name, version number, and file location. <package not found> will indicate
the module didn't install correctly.

	
**USGSquery_startend.py**

This code is designed to retrieve information about USGS gages, specifically their dates of operation. Gage ID numbers are provided to the NWIS server which 
then returns arrays of all recorded data. The first and last date of record are extracted from this data.


LIBRARIES

https://github.com/DOI-USGS/dataretrieval-python/blob/master/dataretrieval/nwis.py

https://openpyxl.readthedocs.io/en/stable/


