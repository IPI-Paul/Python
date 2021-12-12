/*
* Example 20-23
* Runs Python code to accomplish the same results as the Python interactive 
* session
* Author: Mark Lutz, Paul I Ighofose
* Last modified: 2019-04-26
*/

/*******************************************************************************
* simple code strings: C acts like the interactive prompt, code runs in _main__, 
* no output sent to C;
*******************************************************************************/

#include <Python.h>         /* standard API def */

main() {
    printf("ch20_embed-simple\n");
    Py_Initialize();

    /* set Python search path */
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../../chapter20')"); 

    PyRun_SimpleString("import usermod");           /* load .py file */
    PyRun_SimpleString("print(usermod.message)");   /* on Python path */
    PyRun_SimpleString("x = usermod.message");      /* compile and run */
    PyRun_SimpleString("print(usermod.transform(x))");
    Py_Finalize();
}