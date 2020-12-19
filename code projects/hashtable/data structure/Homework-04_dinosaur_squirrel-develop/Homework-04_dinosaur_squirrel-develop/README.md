# Overview
Last week, you generated ASCII movies with scrolling, fixed-width sprites. 
In this assignment, you'll get a chance to make your movies more sophisticated. 
You'll make your movie work with any size sprite, and make it possible to have more than one sprite on the screen at a time. 
Along the way, you will learn a new tool ( `valgrind`), work with pointers and dynamic memory allocation, and gain a bit more understanding of constructors and destructors.


# Reading
Before you begin, get started with the following reading:
* The [Constructors, Destructors, and Assignment](https://github.com/hmc-cs70-fall2018/Materials/blob/master/assets/ConstructorsDestructors.pdf) handout.
* The wiki page on [`valgrind`](https://cs.hmc.edu/cs70/wiki/ValgrindHowTo)

We also recommend these resources on pointers, pointers to pointers (`int**`), and references to pointers (`int*&`), along with successful memory management: 
* This nice overview from `cplusplus.com`: [Pointers in C++](http://www.cplusplus.com/doc/tutorial/pointers/). You can skip the sections on string literals and pointers to functions.
* Section 2.3.3 of the *C++ Primer* textbook about compound types 
* Section 3.5 of the *C++ Primer* textbook for a review of arrays (Review from HW3)
* Section 12.1.2 of the *C++ Primer* about managing memory with `new` and `delete`
* Section 12.2.1 of the *C++ Primer* through the subsection "Freeing Dynamic arrays" about dynamically allocated arrays

# Grading
Your submission will be graded on its correctness, completeness, style, elegance, and clarity. See the [Grading Guidelines](https://cs.hmc.edu/cs70/wiki/Grading-Guidelines) wiki page for more information about what we're looking for in each of those categories. 
