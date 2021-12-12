/*
* Example 20-17
* Generates the glue logic layer between C++ and Python
* Author: Mark Lutz
* Last modified: 
*/

/*******************************************************************************
* SWIG module description file, for wrapping a C++ class. 
* Generate by running "swig -c++ -python ch20_number.i".
* The C++ module is generated in file number_wrap.cxx; module 'number' refers to 
* the number.py shadow class.
*******************************************************************************/

%module number

%{
#include "ch20_number.h"
%}

%include ch20_number.h