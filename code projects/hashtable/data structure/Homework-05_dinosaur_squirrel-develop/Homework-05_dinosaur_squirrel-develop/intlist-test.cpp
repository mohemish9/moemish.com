/**
 * \file intlist-test.cpp
 * \authors CS 70 Starter Code
 * \brief The program unit tests the IntList class.
 *
 * \details Part of the CS 70 IntList assignment.
 */

/* Note: In testing, it's always a good idea to #include the header you're
 *       testing without including anything else beforehand.  That way, you
 *       won't accidentally depend on something being included for your
 *       header to compile.
 */
#include "intlist.hpp"
#include "testing-logger.hpp"

#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <list>

#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;


///////////////////////////////////////////////////////////
//  TESTING
///////////////////////////////////////////////////////////

// ISSUE 2 TESTS

/** \brief Test default constructor for IntLists
 */
bool defaultConstructorTest()
{
    // Set up the TestingLogger object
    TestingLogger log("default constructor");

    // Set up for your test
    IntList myList;

    // Add checks for things that should be true. 
    affirm(myList.size() == 0);

    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}




// ISSUE 3 TESTS -------------------------------------------------
// Add tests here for empty, push_front, and pop_front

/** \brief Test empty
 *  \detail Tests that empty is true for a default intlist, and that
 *          it is false for a non-empty intlist.  
 */
bool emptyTest()
{
    // Set up the TestingLogger object
    TestingLogger log("empty");

    // Set up for your test
    IntList myList;

    affirm(myList.empty());

    // Fill in the test content here...
    myList.push_front(0);

    affirm(!(myList.empty()));
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

// Following the above model, add tests for push/pop front here:

// ...
bool push_frontTest()
{
    TestingLogger log("push_front");

    // Set up for your test
    IntList myList;

    affirm(myList.empty());

 
    myList.push_front(0);

    affirm(!(myList.empty()));

    affirm(myList.size() == 1);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}


// ... 

bool pop_frontTest()
{
    TestingLogger log("pop_front");

    // Set up for your test
    IntList myList;


    myList.push_front(0);

    affirm(!(myList.empty()));

    affirm (myList.pop_front() == 0);

    affirm(myList.empty());
    affirm(myList.size() == 0);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

// ISSUE 4 TESTS -------------------------------------------------
// Do not write tests that call the IntList destructor! 
// Instead, be sure to run valgrind




// ISSUE 5 TESTS -------------------------------------------------
// Add tests here for begin, end; and for Iterator *, ++ and ==
bool beginTest()
{
    TestingLogger log("begin");

    // Set up for your test
    IntList myList;
    myList.push_front(0);
    affirm(*myList.begin() ==0);
    
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

bool endTest()
{
    TestingLogger log("end");

    // Set up for your test
    IntList myList;
    affirm(myList.end() == myList.begin());
    myList.push_front(0);
    myList.push_front(1);
    IntList::iterator myIter = myList.begin();
    ++myIter;
    ++myIter;
    affirm(myList.end()== myIter);
    
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

bool dereference_operatorTest()
{
    TestingLogger log("dereference operator");

    // Set up for your test
    IntList myList;
    myList.push_front(0);
    IntList::iterator myIter = myList.begin();
    affirm(*myIter==0);
    //changes the vlaue of the element through the iterator and checks that the real element is chnaged
    *myIter = 1;
    affirm(*(myList.begin()) == 1);

    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}
bool increment_operatorTest()
{
    TestingLogger log("increment operator");

    // Set up for your test
    IntList myList;
    myList.push_front(0);
    myList.push_front(1);
    myList.push_front(2);
    IntList::iterator myIter = myList.begin();
    ++myIter;
    affirm(*myIter == 1);
    ++myIter;
    affirm(*myIter == 0);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}
bool equalto_operatorTest()
{
    TestingLogger log("equal-to operator");

    // Set up for your test
    IntList myList1;
    
    myList1.push_front(0);
    
    IntList::iterator myIter1 = myList1.begin();
    IntList::iterator myIter2 = myList1.begin();
    affirm(myIter1 == myIter2);
    myList1.push_front(1);
    ++myIter1;
    affirm(myIter1 != myIter2);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}
// ISSUE 6 TESTS -------------------------------------------------
// Add tests here for IntList ==
bool intList_equalto_operatorTest()
{
    TestingLogger log("intList equal-to operator");

    // Set up for your test
    IntList myList1;
    myList1.push_front(0);
    myList1.push_front(1);
    myList1.push_front(2);
    myList1.push_front(3);
    IntList myList2;
    myList2.push_front(0);
    myList2.push_front(1);
    myList2.push_front(2);
    myList2.push_front(3);
    IntList myList3;
    myList3.push_front(69);
    myList3.push_front(4);
    myList3.push_front(20);
    
    
    affirm(myList1 == myList2);
    affirm(myList1 != myList3);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}


// ISSUE 7 TESTS -------------------------------------------------
// Add tests here for push_back and insert_after

bool push_backTest()
{
    TestingLogger log("push_back");

    // Set up for your test
    IntList myList1;
    myList1.push_front(0);
    myList1.push_front(1);
    IntList myList2;
    myList2.push_front(1);
    myList2.push_back(0);

    affirm(myList2.size() == 2);
    affirm(myList1 == myList2);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

bool insert_afterTest()
{
    TestingLogger log("insert_after");

    // Set up for your test
    IntList myList1;
    myList1.push_front(1);

    IntList myList2;
    myList2.push_front(0);
    myList2.push_front(1);


    IntList::iterator myIter = myList1.begin();

    myList1.insert_after(myIter,0);
    
    affirm(myList1 == myList2);
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}
// ISSUE 8 TESTS -------------------------------------------------
// Add tests here for the IntList copy constructor 
bool copy_constructorTest()
{
    TestingLogger log("The copy constructor");

    // Set up for your test
    IntList myList1;
    myList1.push_front(0);
    myList1.push_front(1);
    myList1.push_front(2);
    myList1.push_front(3);

    IntList myList2 = IntList(myList1);

    IntList::iterator myIter = myList2.begin();

    affirm(*myIter == 3);
    ++myIter;
    affirm(*myIter == 2);
    ++myIter;
    affirm(*myIter == 1);
    ++myIter;
    affirm(*myIter == 0);
    
    // Print a summary of the all the affirmations and return true
    // if they were all successful.
    return log.summarize();
}

/*
 * Test the IntList!
 */
int main(int, char**)
{
    TestingLogger alltests("All tests");
    
    affirm(defaultConstructorTest());

    // To do: add your new tests as new affirms here...
    
    affirm(emptyTest());
    affirm(push_frontTest());
    affirm(pop_frontTest());
    affirm(beginTest());
    affirm(endTest());
    affirm(dereference_operatorTest());
    affirm(increment_operatorTest());
    affirm(equalto_operatorTest());
    affirm(intList_equalto_operatorTest());
    affirm(push_backTest());
    affirm(insert_afterTest());
    affirm(copy_constructorTest());
    // Print a summary of the all the affirmations and exit the program.

    if (alltests.summarize(true)) {
        return 0;       // Error code of 0 == Success!
    } else {
        return 2;       // Arbitrarily chosen exit code of 2 means tests failed.
    }
}
