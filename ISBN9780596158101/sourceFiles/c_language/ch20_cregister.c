/*
* Example 20-30
* Uses both embedding and extending interfaces to register and invoke Python 
* event handler code
* Author: Mark Lutz
* Last modified: 
*/

#include <Python.h>
#include <stdlib.h>

/************************************************/
/* 1) code to route events to Python object     */
/* note that we could run strings here instead  */
/************************************************/

static PyObject *Handler = NULL;        /* keep Python object in C */

void Route_Event(char *label, int count)
{
    char *cres;
    PyObject *args, *pres;
    
    /* call Python handler */
    args = Py_BuildValue("(si)", label, count); /* make arg-list */
    pres = PyEval_CallObject(Handler, args);    /* apply: run a call */
    Py_DECREF(args);                            /* add error checks */
    
    if (pres != NULL) {
        /* use and decref handler result */
        PyArg_Parse(pres, "s", &cres);
        printf("%s\n", cres);
        Py_DECREF(pres);
    }
}

/*****************************************************/
/* 2) python extension module to register handlers   */
/* python imports this module to set handler objects */
/*****************************************************/

static PyObject *
Register_Handler(PyObject *self, PyObject *args)
{
    /* save Python callable object */
    Py_XDECREF(Handler);                /* called before? */
    PyArg_Parse(args, "(O)", &Handler); /* one argument */
    Py_XINCREF(Handler);                /* add a reference */
    Py_INCREF(Py_None);                 /* return 'None': success */
    return Py_None;
}

static PyObject *
Trigger_Event(PyObject *self, PyObject *args)
{
    /* let Python simulate event caught by C */
    static count = 0;
    Route_Event("spam", count++);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef ch20_cregister_methods[] = {
    {"setHandler", Register_Handler, METH_VARARGS, ""}, /* name, &func,... */
    {"triggerEvent", Trigger_Event, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}                               /* end of table */
};

static struct PyModuleDef ch20_cregistermodule = {
    PyModuleDef_HEAD_INIT,
    "ch20_cregister",        /* name of module */
    "ch20_cregister mod",    /* module documentation, may be NULL */
    -1,                 /* size of per-interpreter module state, -1=in global vars */
    ch20_cregister_methods   /* link to methods table */
};

PyMODINIT_FUNC
PyInit_ch20_cregister()                  /* called on first import */
{
    return PyModule_Create(&ch20_cregistermodule);
}