/**
 * \file movie.cpp
 * \author CS 70 Provided Code
 *
 * \brief Implements the Movie class
 *
 * \details
 *
 * \remarks
 *
 */

#include <iostream>
#include <stdexcept>

#include "movie-helper.hpp"
#include "asciimation.hpp"
#include "sprite.hpp"

using std::string;
using std::cerr;
using std::endl;
 
Asciimation::Asciimation(string fname, int topLeftColumn, int topLeftRow) 
      : sprite_(fname, topLeftRow, topLeftColumn)
{   
    sprite_.Sprite::setScrolling(true);
    updateContents();
}
void Asciimation::updateContents()
{
    // Clear contents by writing a space everywhere, so that we don't keep
    // old contents around when the display updates.

    // TODO: Call clearContents() to overwrite all of the old content
    // with spaces
    clearContents();
    // TODO: Call moveRight() (once it exists).
    if (sprite_.Sprite::getScrolling()){
        sprite_.Sprite::moveRight(MOVIE_WIDTH);
        }
    // Loop through all of the characters in the sprite and copy them to
    // the right spot in the movie's character array.
     
    size_t movieRow = 0;
    size_t movieCol = 0;
    
    for (size_t spriteRow = 0; spriteRow < Sprite::SPRITE_HEIGHT; 
        ++spriteRow) {

        for(size_t spriteCol = 0; spriteCol < Sprite::SPRITE_WIDTH; 
            ++spriteCol) {

            // if (topLeftColumn is positive OR spriteCol + topLeftColumn is not negative), add stuff()
            if (sprite_.Sprite::getTopLeftColumn() > 0 || ((sprite_.Sprite::getTopLeftColumn() < 0) && (abs(sprite_.Sprite::getTopLeftColumn()) < spriteCol))) {  
                movieCol= sprite_.Sprite::getTopLeftColumn() + spriteCol; 
                movieRow = sprite_.Sprite::getTopLeftRow() + spriteRow;
                if (movieCol < MOVIE_WIDTH){
                    
                    int index = MOVIE_WIDTH * movieRow + movieCol;
                    characterArray_[index] = sprite_.Sprite::getCharAt(spriteRow, spriteCol);
                }
            }
        }
    }
    

}



/**
 * \brief Generates a sequence of frames and converts them into an animation.
 * \param totalFrames is the number of frames of animation to generate
 * \param animationFramerate is given in frames per second
 */
void Asciimation::generateAnimation(string framesDirectory,
                                    int totalFrames,
                                    int animationFramerate)
{


    // specify a base name for each frame's ASCII text file
    const string FRAME_NAME = "frame-";

    // specify the file name for our generated animated GIF
    const string OUTPUT_FILENAME = "./our-movie.gif";

    for (int f = 0; f < totalFrames; ++f) {
        // Copy contents to the screen
        updateContents();
       
        // copy the movie's characters to an ASCII art text file
        string frameNumberStr = std::to_string(f);
        string outputFileName = framesDirectory
                                + FRAME_NAME + frameNumberStr + ".txt";

        exportSingleFrame(outputFileName);
    }

    // use helper function to generate the animated gif!
    convertFramesToAnimation(framesDirectory,
                             totalFrames, animationFramerate,
                             FRAME_NAME, OUTPUT_FILENAME);
}

void Asciimation::exportSingleFrame(string fileName)
{
    // Loop through all of the characters in the current character array and
    // copy them to an ASCII text file; then, export (save) that file.
    // TODO: Fill in the implementation of exportSingleFrame
    
    std::ofstream outputFile;
    outputFile.open(fileName);
    for (size_t row = 0; row<MOVIE_HEIGHT; row++) {
        for(size_t column = 0; column < MOVIE_WIDTH; column++) {
          int index = row*MOVIE_WIDTH+column;
         outputFile << characterArray_[index];
        }
        outputFile<<'\n';
    }
    outputFile.close();
}

void Asciimation::clearContents(){
    for(size_t row = 0; row<MOVIE_HEIGHT; row++){
        for (size_t column = 0; column<MOVIE_WIDTH; column++){
           int index = row * MOVIE_WIDTH + column;
           characterArray_[index] = ' ';
        }
    } 
}