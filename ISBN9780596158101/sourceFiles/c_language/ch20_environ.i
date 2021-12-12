/*
* Example 20-12
* Can replace the entire ch20_cenviron.c C code file for wrapping with SWIG
* Author: Mark Lutz
* Last modified: 
*/

/*******************************************************************************
* SWIG module description file, to generate all Python wrapper code for C lib 
* getenv/putenv calls: "swig -python ch20_environ.i".
*******************************************************************************/

%module environ

extern char *getenv(const char *varname);
extern int putenv(char *assignment);