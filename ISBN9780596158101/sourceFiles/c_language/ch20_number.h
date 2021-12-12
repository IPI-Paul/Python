/*
* Example 20-14
* The C++ file defines a Number class with four methods (add, sub, square, and 
* display), a data member (data), and a constructor and destructor. This is the
* header file for the C++ file
* Author: Mark Lutz
* Last modified: 
*/

class Number
{
public:
    Number(int start);                      // constructor
    ~Number();                              // destructor
    void add(int value);                    // update data member
    void sub(int value);
    int square();                           // return a value
    void display();                         //print data member
    int data;
};