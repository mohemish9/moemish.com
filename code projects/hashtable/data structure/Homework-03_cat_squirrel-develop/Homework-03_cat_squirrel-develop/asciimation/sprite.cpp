/**
 * \file sprite.cpp
 * \author CS 70 Provided Code
 *
 * \brief Implements the Sprite class
 *
 * \details
 *
 * \remarks
 *
 */

#include <cstddef>
#include <iostream>
#include "sprite.hpp"

Sprite::Sprite(string fname, int topLeftRow, int topLeftColumn)
{    topLeftColumn_=topLeftColumn;
     topLeftRow_=topLeftRow;
     
    ifstream inputFile(fname);

    if (!inputFile.good()) {
        cerr << "Error: Unable to open input file: " << fname;
        return;
    }

    int widthFromFile = 0;
    inputFile >> widthFromFile;

    int heightFromFile = 0;
    inputFile >> heightFromFile;

    inputFile.get(); // Read past the newline character after the height.

    if (widthFromFile != SPRITE_WIDTH) {
        cerr << "Warning: Trying to read a Sprite with the wrong width: "
             << widthFromFile << endl;
    }

    if (heightFromFile != SPRITE_HEIGHT) {
        cerr << "Warning: Trying to read a Sprite with the wrong height: "
             << heightFromFile << endl;
    }

    // Read in characters from the text file,
    // copying them into the character array.
    int index = 0;
    while(!(inputFile.eof())){
      contents_[index] = inputFile.get();
      index++;
    }
    // TODO: Fill in this part so that it puts values into the contents_ of
    // this Sprite object. You can use inputFile.get() to get one character
    // at a time from the file.

    inputFile.close();
}

int Sprite::getTopLeftColumn(){
    return topLeftColumn_;
}

int Sprite::getTopLeftRow(){
    return topLeftRow_;
}

char Sprite::getCharAt(int row, int col){
    int index = row* SPRITE_WIDTH + col;
    return contents_[index];
}

void Sprite::setLocation(int x, int y){
    topLeftRow_ = x;
    topLeftColumn_ = y;

}

void Sprite::setScrolling(bool flag){
    shouldScroll_ = flag;
}

bool Sprite::getScrolling(){
   return shouldScroll_;
}

void Sprite::moveRight(int screenWidth){
    if(getTopLeftColumn() >= screenWidth){
        topLeftColumn_ = 0 - SPRITE_WIDTH ;
    }
    else
    {
       topLeftColumn_++;
    }
}