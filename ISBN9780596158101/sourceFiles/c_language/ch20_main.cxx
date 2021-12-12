/*
* Example 20-16
* The C++ file defines a Number class with four methods (add, sub, square, and 
* display), a data member (data), and a constructor and destructor. This is how
* this class is USED IN A C++ program (C++ distinguishes between "members" and 
* "methods", while they're usually both called "attributes" in Python)
* Author: Mark Lutz
* Last modified: 
*/

#include <iostream>
#include "ch20_number.h"

main()
{
    Number *num;
    int res, val;
    
    num = new Number(1);                // make a C++ class instance
    num->add(4);                        // call its methods
    num->display();
    num->sub(2);
    num->display();
    
    res = num->square();                // method return value
    std::cout << "square: " << res << std::endl;
    
    num->data = 99;                     // set C++ data member
    val = num->data;                    // fetch C++ data member
    std::cout << "data:   " << val << std::endl;
    std::cout << "data+1: " << val + 1 << std::endl;
    
    num->display();
    std::cout << num << std::endl;                // print raw instance ptr
    delete num;                         // run destructor
}