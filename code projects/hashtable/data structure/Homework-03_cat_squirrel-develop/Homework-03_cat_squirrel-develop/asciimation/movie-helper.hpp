/**
 * \file movie-helper.hpp
 * \author CS 70 Provided Code
 *
 * \brief Friendly helper code to create ASCII art animations in animated
 * GIF format.
 *
 * \details Uses imagemagick to convert ASCII art text files into PNG frames.
 * Then converts these frames into an animated GIF using FFMPEG.
 *
 * \remarks
 *
 */

#include <string>

using std::string;

void convertFramesToAnimation(string framesDirectory,
                              int totalFrames, int animationFramerate,
                              string framesBaseFilename,
                              string movieFilename);
