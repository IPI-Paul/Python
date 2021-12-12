/*
* Example 20-29
* Uses Py_CompileString that takes a mode flag  that is normally passed to 
* PyRun_String, as well as a second string argument that is used only in error 
* messages. Also uses PyEval_EvalCode which takes two namspace dictionaries
* Author: Mark Lutz, Paul I Ighofose
* Last modified: 2019-04-27
*/

/* precompile code strings to bytecode objects */

#include <Python.h>
#include <compile.h>
#include <eval.h>

main() {
    int i;
    char *cval;
    PyObject *pcode1, *pcode2, *pcode3, *presult, *pdict;
    char *codestr1, *codestr2, *codestr3;
    printf("ch20_embed-bytecode\n");
    
    Py_Initialize();
    
    /* set Python search path */
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('../../chapter20')");     
    
    codestr1 = "import usermod\nprint(usermod.message)";    /* statements */
    codestr2 = "usermod.transform(usermod.message)";        /* expression */
    codestr3 = "print('%d:%d' % (X, X ** 2), end=' ')";     /* use input X */
    
    /* make new namespace dictionary */
    pdict = PyDict_New();
    if (pdict == NULL) return -1;
    PyDict_SetItemString(pdict, "__builtins__", PyEval_GetBuiltins());
    
    /* precompile strings of code to bytecode objects */
    pcode1 = Py_CompileString(codestr1, "<embed>", Py_file_input);
    pcode2 = Py_CompileString(codestr2, "<embed>", Py_eval_input);
    pcode3 = Py_CompileString(codestr3, "<embed>", Py_file_input);
    
    /* run compiled bytecode in namespace dict */
    if (pcode1 && pcode2 && pcode3) {
        (void) PyEval_EvalCode((PyCodeObject *)pcode1, pdict, pdict);
        presult = PyEval_EvalCode((PyCodeObject *)pcode2, pdict, pdict);
        PyArg_Parse(presult, "s", &cval);
        printf("%s\n", cval);
        Py_DECREF(presult);
        
        /* return code object repeatedly */
        for (i = 0; i <= 10; i++) {
            PyDict_SetItemString(pdict, "X", PyLong_FromLong(i));
            (void) PyEval_EvalCode((PyCodeObject *)pcode3, pdict, pdict);
        }
        printf("\n");
    }
    /* free referenced objects */
    Py_XDECREF(pdict);
    Py_XDECREF(pcode1);
    Py_XDECREF(pcode2);
    Py_XDECREF(pcode3);
    Py_Finalize();
}