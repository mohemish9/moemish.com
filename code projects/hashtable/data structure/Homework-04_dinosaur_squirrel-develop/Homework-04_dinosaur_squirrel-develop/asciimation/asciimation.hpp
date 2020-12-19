/* asciimation.hpp
   =========

   Interface definition for the Asciimation class, which handles the creation
   of a sprite-based asciimation movie.

 */

#ifndef ASCIIMATION_HPP_INCLUDED
#define ASCIIMATION_HPP_INCLUDED

#include <string>
#include "sprite.hpp"


/**
 * \class Asciimation
 * \brief Holds the contents of an ASCIImation movie
 *
 * \details
 * Stores an array of characters that will be displayed to the screen, and
 * a Sprite that will be added to the screen.
 *
 */

using std::string;

class Asciimation {
public:
    

    Asciimation(size_t width, size_t height) ;

    /**
     * \brief Creates the current display showing the sprite
     * \post The current display contents are up to date and
     * ready to display to the screen.
     */
    void updateContents();

    /**
     * \brief generates an animated GIF of the requested duration
     * \post
     */
    void generateAnimation(string framesDirectory,
                           int totalFrames,
                           int animationFramerate);

    /**
     * \brief Exports the current display contents to a text file
     * \post file [fileName] contains an ASCII art rendering
     * of the current display buffer.
     */
    void exportSingleFrame(string fileName);
    void checkResize();
    void addSprite(const string&filename, int xPos, int yPos, bool scrolling);
    ~Asciimation();
    
    Asciimation (const Asciimation &asciimation) = delete;
    


private:
    Sprite** sprites_;
    size_t width_;
    size_t height_;
    size_t totalSprites_;
    size_t spriteCapacity_;
    char* movie_;
    void clearContents();
};

#endif // ifndef ASCIIMATION_HPP_INCLUDED
