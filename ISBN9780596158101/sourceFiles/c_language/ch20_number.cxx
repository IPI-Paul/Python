/*
* Example 20-15
* The C++ file defines a Number class with four methods (add, sub, square, and 
* display), a data member (data), and a constructor and destructor. This is the
* class's implementation file
* Author: Mark Lutz
* Last modified: 
*/

////////////////////////////////////////////////////////////////////////////////
// implement c C++ calss, to be used from Python code or not; 
// caveat: cout and print usually both work, but I ran into a c++/py output 
// overlap issue on Cygwin that prompted printf
////////////////////////////////////////////////////////////////////////////////

#include "ch20_number.h"
#include "stdio.h"                      // versus #include "iostream.h"

Number::Number(int start) {
    data = start;                       // python print goes to stdout
    printf("Number: %d\n", data);       // or: cout << "Number: " << data << endl;
}

Number::~Number() {
    printf("~Number: %d\n", data);
}

void Number::add(int value) {
    data += value;
    printf("add %d\n", value);
}

void Number::sub(int value) {
    data -= value;
    printf("sub %d\n", value);
}

int Number::square() {
    return data * data;        // if print label, fflush(stdout) or cout << flush
}

void Number::display() {
    printf("Number=%d\n", data);
}