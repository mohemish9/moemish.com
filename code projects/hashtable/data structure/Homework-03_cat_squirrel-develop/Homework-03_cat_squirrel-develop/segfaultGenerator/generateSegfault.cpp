/**
 * \file generateSegfault.cpp
 *
 * \brief Reads past the end of an array, to induce a segfault.
 *
 */

#include "helloSayer.hpp"

#include <iostream>

using std::cout;
using std::endl;

int main() {

    HelloSayer helloSayer;
    helloSayer.sayHello();

    static const size_t ARRAY_SIZE = 10;
 
    int array[ARRAY_SIZE];

    size_t i = 0;
    int sum = 0;
    while (true) { // intentionally loop forever
        sum += array[i];
        cout << "Successfully read array[" << i
            << "] when the size is really " << ARRAY_SIZE
            << ", sum is " << sum << endl;
        ++i;
    }

    cout << "The sum is " << sum << ", though you'll never actually see "
        "this message" << endl;

    return 0;
}
