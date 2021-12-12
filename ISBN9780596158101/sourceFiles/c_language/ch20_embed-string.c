/*
* Example 20-26
* Uses the following API calls to run code strings that return expression results
* back to C
* Author: Mark Lutz, Paul I Ighofose
* Last modified: 2019-04-26
*/

/* code-strings with results and namespaces */

#include <Python.h>

main() {
    char *cstr;
    PyObject *pstr, *pmod, *pdict;
    printf("ch20_embed-string\n");
    Py_Initialize();

    /* set Python search path */
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../../chapter20')"); 
    
    /* get usermod.message */
    pmod = PyImport_ImportModule("usermod");
    pdict = PyModule_GetDict(pmod);
    pstr = PyRun_String("message", Py_eval_input, pdict, pdict);
    
    /* convert to C */
    PyArg_Parse(pstr, "s", &cstr);
    printf("%s\n", cstr);
    
    /* assign usermod.X */
    PyObject_SetAttrString(pmod, "X", pstr);
    
    /* print usermod.transform(X) */
    (void) PyRun_String("print(transform(X))", Py_file_input, pdict, pdict);
    Py_DECREF(pmod);
    Py_DECREF(pstr);
    Py_Finalize();
}