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

Sprite::Sprite(string fname, int topLeftRow, int topLeftColumn, bool shouldScroll) 
: topLeftRow_ (topLeftRow), topLeftColumn_ (topLeftColumn), fname_ (fname),  shouldScroll_(shouldScroll) {
    
    
   // TODO: Initialize the simplest data members using constructor parameters
    ifstream inputFile(fname);
    
    if (!inputFile.good()) {
        cerr << "Error: Unable to open input file: " << fname;
        return;
    }
    inputFile >> width_;
    inputFile >>  height_;
    contents_ = new char [width_ * height_];



    inputFile.get(); // Read past the newline character after the height.

    

    // Read in characters from the text file,
    // copying them into the character array.

    for(size_t i =0; i < height_*width_; ++i){
            contents_[i] = inputFile.get();
        }

    // TODO: Fill in this part so that it puts values into the contents_ of
    // this Sprite object. You can use inputFile.get() to get one character
    // at a time from the file.

    inputFile.close();
}
Sprite::~Sprite(){
  delete [] contents_;
}

int Sprite::getTopLeftColumn() {
    return topLeftColumn_;
}

int Sprite::getTopLeftRow() {
    return topLeftRow_;
}

char Sprite::getCharAt(int row, int col) {
    return contents_[(row*width_)+col];
}

void Sprite::setLocation(int x, int y) {
    topLeftRow_ = x;
    topLeftColumn_ = y;
}

void Sprite::setScrolling(bool flag) {
    shouldScroll_ = flag;
}

void Sprite::moveRight(int screenWidth) {
    ++topLeftColumn_;
    if (getTopLeftColumn() == screenWidth) {
        topLeftColumn_ = (int) -width_;
    }
}

bool Sprite::getScrolling(){
    return shouldScroll_;
}

size_t Sprite::getWidth(){
    return width_;
}
size_t Sprite::getHeight(){
    return height_;
}