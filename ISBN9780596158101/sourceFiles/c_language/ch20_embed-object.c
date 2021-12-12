/*
* Example 20-27
* Accomplishes the same task as Examples 20-23 and 20-26, but it uses other API
* tools to interact with objects in the Python module directly
* Author: Mark Lutz, Paul I Ighofose
* Last modified: 2019-04-27
*/

/* fetch and call objects in modules */

#include <Python.h>

main() {
    char *cstr;
    PyObject *pstr, *pmod, *pfunc, *pargs;
    printf("ch20_embed-object\n");
    Py_Initialize();
    
    /* set Python search path */
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../../chapter20')"); 

    /* get usermod.message */
    pmod = PyImport_ImportModule("usermod");
    pstr = PyObject_GetAttrString(pmod, "message");
    
    /* convert string to C */
    PyArg_Parse(pstr, "s", &cstr);
    printf("%s\n", cstr);
    Py_DECREF(pstr);
    
    /* call usermod.tranform(usermod.message) */
    pfunc = PyObject_GetAttrString(pmod, "transform");
    pargs = Py_BuildValue("(s)", cstr);
    pstr = PyEval_CallObject(pfunc, pargs);
    PyArg_Parse(pstr, "s", &cstr);
    printf("%s\n", cstr);
    
    /* free owned objects */
    Py_DECREF(pmod);
    Py_DECREF(pstr);
    Py_DECREF(pfunc);               /* not really neeeded in main() */
    Py_DECREF(pargs);               /* since all memory goes away */
    Py_Finalize();
}