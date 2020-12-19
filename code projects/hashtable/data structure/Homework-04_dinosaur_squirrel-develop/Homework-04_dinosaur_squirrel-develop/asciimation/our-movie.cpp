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


void makeOurMovie()  {
    Asciimation ourMovie(80,80);
    ourMovie.addSprite("spriteImages/background.txt", 5,  5, false);
    ourMovie.addSprite("spriteImages/discoball.txt", 10,  20, false);
    ourMovie.addSprite("spriteImages/smiley.txt", 5,  5, true);
    ourMovie.addSprite("spriteImages/ymca_m.txt",    20, 20, true);
    ourMovie.generateAnimation("frames/", 100, 30);
    
}

int main()
{
    makeOurMovie();
    return 0;
}
