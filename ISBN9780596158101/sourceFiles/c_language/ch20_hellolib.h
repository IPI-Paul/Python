/*
* Example 20-5
* The header file that declares the function externally
* Author: Mark Lutz
* Last modified: 
*/

/*******************************************************************************
* Define ch20_hellolib.c exports to the C namespace, not to Python programs--the
* latter is defined by a method registration table in a Python extension module's
* code, not by this .h
*******************************************************************************/

extern char *message(char *label);