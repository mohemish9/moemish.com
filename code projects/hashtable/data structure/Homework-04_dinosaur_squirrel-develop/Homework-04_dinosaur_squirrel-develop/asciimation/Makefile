
# Updates the executable file 
all: our-movie

# The rule below is creating our executable named our-movie


our-movie: sprite.o asciimation.o movie-helper.o our-movie.o
	clang++  -o our-movie -g -std=c++1z -pedantic -Wall -Wextra sprite.o asciimation.o movie-helper.o our-movie.o  -lstdc++fs

# The four rules directly below are creating machine language files
# These files are asciimation.o, movie-helper.o, sprite.o, and our-movie.o

sprite.o: sprite.cpp sprite.hpp
	clang++ -c -o sprite.o -g -std=c++1z -pedantic -Wall -Wextra sprite.cpp
	
asciimation.o: asciimation.cpp asciimation.hpp sprite.cpp sprite.hpp
	clang++ -c -o asciimation.o -g -std=c++1z -pedantic -Wall -Wextra asciimation.cpp

movie-helper.o: movie-helper.cpp movie-helper.hpp
	clang++ -c -o movie-helper.o -g -std=c++1z -pedantic -Wall -Wextra movie-helper.cpp 

our-movie.o: our-movie.cpp 
	clang++ -c -o our-movie.o -g -std=c++1z -pedantic -Wall -Wextra our-movie.cpp

# Removes all object files and the executable
clean:
	rm -rf *.o our-movie

	