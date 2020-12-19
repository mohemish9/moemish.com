/**
 * \file our-movie.cpp
 * \author CS 70 Provided Code
 *
 * \brief Provides the main() function for creating and running
 * a specific asciimation movie.
 *
 * \details
 *
 * \remarks
 *
 */
#include <iostream>
#include "asciimation.hpp"
#include "sprite.hpp"

void makeOurMovie()
{
       Asciimation movieMaker = Asciimation("spriteImages/ourimage.txt", 15, 10);
 
       movieMaker.Asciimation::generateAnimation("./frames/",100,15);

}


int main()
{
    makeOurMovie();
    return 0;
}
