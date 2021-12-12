/*
* Example 20-28
* Creates a brand-new namespace for running code strings that is independent of 
* any existing module files. The new namespace is created as a dictionary object,
* an a handful of new API calls are employed in the process
* Author: Mark Lutz
* Last modified: 
*/

/* make a new dictionary for code string namespace */

#include <Python.h>

main() {
    int cval;
    PyObject *pdict, *pval;
    printf("ch20_embed-dict\n");
    Py_Initialize();
    
    /* make a new namespace */
    pdict = PyDict_New();
    PyDict_SetItemString(pdict, "__builtins__", PyEval_GetBuiltins());
    
    PyDict_SetItemString(pdict, "Y", PyLong_FromLong(2));   /* dict['Y'] = 2 */
    PyRun_String("X = 99", Py_file_input, pdict, pdict);    /* run statements */
    PyRun_String("X = X+Y", Py_file_input, pdict, pdict);   /* same X and Y */
    pval = PyDict_GetItemString(pdict, "X");                /* fetch dict['X'] */
    
    PyArg_Parse(pval, "i", &cval);                          /* convert to C */
    printf("%d\n", cval);                                   /* result=101 */
    Py_DECREF(pdict);
    Py_Finalize();
}