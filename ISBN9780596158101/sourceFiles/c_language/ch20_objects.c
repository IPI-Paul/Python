/*
* Example 20-34
* Uses both embedding and extending interfaces to register and invoke Python 
* event handler code
* Author: Mark Lutz
* Last modified: 
*/

#include <Python.h>
#include <stdio.h>

main() {
    /* run objects with low-level calls */
    char *arg1="sir", *arg2="robin",  *cstr;
    PyObject *pmod, *pclass, *pargs, *pinst, *pmeth, *pres;
    
    /* instance = module.klass */
    Py_Initialize();

    /* set Python search path */
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../../chapter20')"); 

    pmod = PyImport_ImportModule("module");         /* fetch module */
    pclass = PyObject_GetAttrString(pmod, "klass"); /* fetch module.class */
    Py_DECREF(pmod);
    
    pargs = Py_BuildValue("()");
    pinst = PyEval_CallObject(pclass, pargs);       /* call class() */
    Py_DECREF(pclass);
    Py_DECREF(pargs);
    
    /* result = instance.method(x, y) */
    pmeth = PyObject_GetAttrString(pinst, "method");/* fetch bound method */
    Py_DECREF(pinst);
    pargs = Py_BuildValue("(ss)", arg1, arg2);      /* convert to Python */
    pres = PyEval_CallObject(pmeth, pargs);         /* call mehtod(x, y) */
    Py_DECREF(pmeth);
    Py_DECREF(pargs);
    
    PyArg_Parse(pres, "s", &cstr);                  /* convert to C */
    printf("%s\n", cstr);
    Py_DECREF(pres);
}