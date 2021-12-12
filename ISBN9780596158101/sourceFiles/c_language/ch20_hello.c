/*
* Example 20-1
* Implements a simple C extension module named hello for use in Python scripts, 
* with a function named message that simply returns its input string argument 
* with extra text prepended
* Author: Mark Lutz
* Last modified: 
*/

/*******************************************************************************
* A simple C extension module for Python, called "hello"; compile this into a 
* ".so" on python path, import and call hello.message
*******************************************************************************/

#include <Python.h>
#include <string.h>

/* module functions */
static PyObject *                                   /* returns object */
message(PyObject *self, PyObject *args)             /* self unused in modules */
{
    char *fromPython, result[1024];
    if(! PyArg_Parse(args, "(s)", &fromPython))     /* convert Python -> C */
        return NULL;                                /* null=raise exception */
    else {
        strcpy(result, "Hello, ");                  /* build up C string */
        strcat(result, fromPython);                 /* add passed Python string */
        return Py_BuildValue("s", result);          /* convert C -> Python */
    }
}

/* registration table */
static PyMethodDef ch20_hello_methods[] = {
    {"message", message, METH_VARARGS, "func doc"}, /* name, &func, fmt, doc */
    {NULL, NULL, 0, NULL}                           /* end of table marker */
};

/* module definition structure */
static struct PyModuleDef ch20_hellomodule = {
    PyModuleDef_HEAD_INIT,
    "ch20_hello",        /*name of module */
    "mod doc",      /* module documentation, may be NULL */
    -1,             /* size of per-interpreter module state, -1=in global vars */
    ch20_hello_methods   /* link to methods table */
};

/* module initializer */
PyMODINIT_FUNC
PyInit_ch20_hello()                      /* called on first import */
{                                   /* name matters if loaded dynamically */
    return PyModule_Create(&ch20_hellomodule);
}