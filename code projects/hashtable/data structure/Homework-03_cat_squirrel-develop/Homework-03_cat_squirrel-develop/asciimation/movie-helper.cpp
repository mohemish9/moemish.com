/**
 * \file movie-helper.cpp
 * \author CS 70 Provided Code
 *
 * \brief Friendly helper code to create ASCII art animations as animated GIFs.
 *
 * \details Uses Imagemagick to convert ASCII art text files into PNG frames.
 * Then converts these frames into an animated GIF using FFMPEG.
 *
 * \remarks
 *
 */

#include <cstdlib>                 // used for system(...) calls
#include <experimental/filesystem> // used for directory manipulations
#include <iostream>
#include "movie-helper.hpp"

// for brevity, we can refer to the filesystem namespace with a shortcut ("fs"):
namespace fs = std::experimental::filesystem;

void runSystemCommand(string commandStr){

    // We'll need to convert the command from type "string"
    // to type "const char *" because the system requires it.
    // The .c_str() method converts to "C-Style String", aka "char *"
    const char *command = commandStr.c_str();

    // report to standard error the command you're about to execute:
    std::cerr << "\tExecuting command: \n\t\t" + commandStr << std::endl;
    system(command); // executes as if typed directly into the command line
}

/**
 * \brief Takes in text files of ASCII art; converts these to PNG frames,
 * uses these frames to generate an animated GIF.
 * \post movieFilename exists and contains an animation
 * of the input text files.
 */
void convertFramesToAnimation(string framesDirectory,
                              int totalFrames, int animationFramerate,
                              string framesBaseFilename, string movieFilename){

    // Step zero: ============================================================
    // make a temporary directory to store image files

    string tmpDir = framesDirectory + "tmp/";
    fs::create_directory(tmpDir);

    // Step one: ============================================================
    // convert all ASCII text files to PNG images, one per frame

    for (int i = 0; i < totalFrames; ++i){
        string imagemagickCommand = "";

        // pixel width, height of each frame
        imagemagickCommand += "convert -size 600x600";

        // draw in the specified font and font size on a white background
        string fontName = "\"Courier-New\""; // this is available on Knuth
        imagemagickCommand += " xc:white -font " + fontName + " -pointsize 12";

        // fill letters in with the color black
        imagemagickCommand += " -fill black ";

        // start drawing letters at the upper left corner
        imagemagickCommand += " -gravity NorthWest -annotate 0 ";

        // tell ImageMagick which ASCII text file we want to draw
        string textFileName = framesDirectory + framesBaseFilename
                + std::to_string(i) + ".txt ";
        imagemagickCommand += "@" + textFileName;

        // the image file (PNG format) to export to
        string imageFileName = tmpDir + framesBaseFilename
                + std::to_string(i) + ".png";
        imagemagickCommand += imageFileName;

        // Finally, run the full command to generate the image
        runSystemCommand(imagemagickCommand);
    }

    // Step two: ============================================================
    // combine all frame images into a single animation
    string ffmpegCommand = "";

    // set the number of frames to display per second of animation
    ffmpegCommand += "ffmpeg -framerate " + std::to_string(animationFramerate);

    // import all frames whose name is of the form /tmp/frame-X.png
    ffmpegCommand += " -i " + tmpDir + framesBaseFilename + "%d.png" ;

    // tell FFMPEG to save the result to the filename provided
    // the [-y] flag permits FFMPEG to overwrite this file if it already exists.
    // the [-v 0] flag tells FFMPEG we don't need terminal output
    ffmpegCommand += " " + movieFilename + " -y -v 0";

    // Generate the animated GIF!
    runSystemCommand(ffmpegCommand);

    // Step three: ============================================================
    // clean up by deleting all image frames
    fs::remove_all(tmpDir);
}


