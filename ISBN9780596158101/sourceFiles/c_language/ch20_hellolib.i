/*
* Example 20-6
* SWIG type declarations input file
* Author: Mark Lutz
* Last modified: 
*/

/*******************************************************************************
* Swig module description file, for a C lib file. 
* Generate by saying "swig - python ch20_hellolib.i"
*******************************************************************************/

%module hellowrap

%{
#include <../c_language/ch20_hellolib.h>
%}

extern char *message(char*);        /* or; %include "../HelloLib/hellolib.h" */
                                    /* or; %include hellolib.h, and use -I arg */