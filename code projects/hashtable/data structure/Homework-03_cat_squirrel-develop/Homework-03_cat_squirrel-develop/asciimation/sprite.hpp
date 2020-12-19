/* sprite.hpp
   =========

   interface definition for the Sprite class. Defines the behavior
   of a single asciimation 'character'

 */

#ifndef SPRITE_HPP_INCLUDED
#define SPRITE_HPP_INCLUDED

#include <iostream>
#include <fstream>
#include <string>

using std::string;
using std::cout;
using std::cerr;
using std::endl;
using std::ifstream;

/**
 * \class Sprite
 * \brief Holds the contents of a single ASCIImation sprite
 *
 * \details
 * Stores an array of characters that will be displayed to the screen, along
 * with the sprite's current location.
 *
 * \remarks
 *    The implemented code only works for a fixed size sprite.
 *
 */
class Sprite {
public:
    // Size of the sprite, in characters
    // Declaring these to be static constants
    // tells the compiler that they're the same for all Sprites, and that
    // they won't change. 
    static const size_t SPRITE_WIDTH = 40;
    static const size_t SPRITE_HEIGHT = 10;

    /**
     * \brief Reads a text file containing the characters for a sprite.
     * \post Should populate the sprite's character array, but doesn't yet.
     */
    Sprite(string fname, int row, int col);
    Sprite() = delete; 
    int getTopLeftRow ();
    int getTopLeftColumn();
    char getCharAt ( int row, int col);
    void setLocation(int x, int y);
    void setScrolling(bool flag);
    bool getScrolling();
    void moveRight(int screenWidth);
private:
    int topLeftColumn_;
    int topLeftRow_;
    char contents_[SPRITE_HEIGHT*SPRITE_WIDTH];
    bool shouldScroll_;
};

#endif // ifndef SPRITE_HPP_INCLUDED
