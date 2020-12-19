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
    
    

    /**
     * \brief Reads a text file containing the characters for a sprite.
     * \post Should populate the sprite's character array, but doesn't yet.
     */
    Sprite(string fname, int topLeftRow, int topLeftColumn, bool shouldScroll);
    ~Sprite();
    Sprite (const Sprite &sprite) = delete;
    
    Sprite() = delete; 
    int getTopLeftColumn();
    int getTopLeftRow();
    char getCharAt(int row, int col);
    void setLocation(int x, int y);
    
    // Sprite(int topLeftRow, int topLeftColumn, string fname) = delete;


    void setScrolling(bool flag);
    bool getScrolling();
    void moveRight(int screenWidth);
    size_t getWidth();
    size_t getHeight();


private:
    int topLeftRow_;
    int topLeftColumn_;
    string fname_;
    char* contents_;
    bool shouldScroll_;
    size_t width_;
    size_t height_;



};

#endif // ifndef SPRITE_HPP_INCLUDED
