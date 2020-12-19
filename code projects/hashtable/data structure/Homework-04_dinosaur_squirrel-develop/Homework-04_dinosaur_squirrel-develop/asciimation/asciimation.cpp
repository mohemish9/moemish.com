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

#include <fstream>
#include <iostream>
#include <stdexcept>

#include "movie-helper.hpp"
#include "asciimation.hpp"
#include "sprite.hpp"

using std::string;
using std::cerr;
using std::endl;
using std::ifstream;
using std:: ofstream;

Asciimation::Asciimation(size_t width, size_t height) 
: width_ (width), height_ (height), totalSprites_ (0), spriteCapacity_ (5)
{
    movie_ = new char [width_ * height_];
    sprites_ = new Sprite*[spriteCapacity_];
}
void Asciimation::clearContents(){
     for(size_t i =0; i < width_*height_; ++i){
            movie_[i] = ' ';
        }
}

Asciimation::~Asciimation(){
    delete [] movie_;
    for (size_t index =0; index<totalSprites_; index++ ){
        delete sprites_[index];
    }
    delete [] sprites_;
}
void Asciimation::updateContents()
{
    // Clear contents by writing a space everywhere, so that we don't keep
    // old contents around when the display updates.

    // TODO: Call clearContents() to overwrite all of the old content
    // with spaces
    clearContents();

    // TODO: Call moveRight() (once it exists).
    for (size_t index = 0; index < totalSprites_; index++){
        if (sprites_[index]->Sprite::getScrolling()){
        sprites_[index]->Sprite::moveRight(width_);
        }
        // Loop through all of the characters in the sprite and copy them to
        // the right spot in the movie's character array.
        if (sprites_[index]->Sprite::getScrolling()){
           sprites_[index]->Sprite::moveRight(width_);
        }

        size_t movieRow = 0;
        size_t movieCol = 0;
        
        
        for (size_t spriteRow = 0; spriteRow < sprites_[index]->Sprite::getHeight(); 
            ++spriteRow) {
            for(size_t spriteCol = 0; spriteCol < sprites_[index]->Sprite::getWidth(); 
                ++spriteCol) {
                    if (sprites_[index]->Sprite::getTopLeftColumn() > 0 || ((sprites_[index]->Sprite::getTopLeftColumn() < 0) && (abs(sprites_[index]->Sprite::getTopLeftColumn()) < int(spriteCol)))) {  
                      movieCol = spriteCol + sprites_[index]->getTopLeftColumn();
                      movieRow =  spriteRow + sprites_[index]->getTopLeftRow();
                      if (movieCol < width_){
                         movie_[width_*movieRow+movieCol] = sprites_[index]->getCharAt(spriteRow, spriteCol);
                      }
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

    ofstream myfile (fileName);
    if (myfile.good()){
      for(size_t row =0; row<Asciimation::height_; ++row){
          for (size_t col = 0; col < Asciimation::width_; ++col){
              myfile << Asciimation::movie_[(row*Asciimation::width_)+col];
          }
          myfile<<endl;
      }
        myfile.close();
    }

}


void Asciimation::checkResize(){
    if ( totalSprites_ == spriteCapacity_ ){
       spriteCapacity_ = spriteCapacity_*2;
       Sprite** newSprites = new Sprite*[spriteCapacity_];
       for (size_t index =0; index < (spriteCapacity_/2) ; index++){
           newSprites[index] = sprites_[index];
       }
       delete[] sprites_;
       sprites_ = newSprites;

    }
}


void Asciimation::addSprite(const string&filename, int xPos, int yPos, bool scrolling){
  checkResize();
  Sprite* s = new Sprite( filename,  xPos,  yPos, scrolling);
  sprites_[totalSprites_] = s;
  ++totalSprites_;
}