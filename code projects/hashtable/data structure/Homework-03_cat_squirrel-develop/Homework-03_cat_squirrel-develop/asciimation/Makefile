sprite.o: sprite.cpp sprite.hpp
	clang++ -c -o sprite.o -g -std=c++11 -pedantic -Wall -Wextra sprite.cpp

asciimation.o: asciimation.cpp asciimation.hpp
	clang++ -c -o asciimation.o -g -std=c++11 -pedantic -Wall -Wextra asciimation.cpp
movie-helper.o: movie-helper.cpp movie-helper.hpp
	clang++ -c -o movie-helper.o -g -std=c++11 -pedantic -Wall -Wextra movie-helper.cpp

our-movie.o: our-movie.cpp
	clang++ -c -o our-movie.o -g -std=c++11 -pedantic -Wall -Wextra our-movie.cpp

our-movie: sprite.o asciimation.o movie-helper.o our-movie.o
	clang++ -o our-movie -g -std=c++1z -pedantic -Wall -Wextra sprite.o movie-helper.o asciimation.o our-movie.o -lstdc++fs

clean:
	rm -rf *.o movie-helper

