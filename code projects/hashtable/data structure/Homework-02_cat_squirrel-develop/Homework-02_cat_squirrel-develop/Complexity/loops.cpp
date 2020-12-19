#include <time.h>
#include <cmath>

unsigned int loopA(unsigned int N){
    unsigned int total = 0;
    for(unsigned int i = 0; i < N; ++i) {
        total++;
    }
    return total;
}

unsigned int loopB(unsigned int N){
    unsigned int total = 0;

    for(unsigned int i = 0; i < N; ++i) {
        for(unsigned int j = i; j < N; ++j) {
              total++;
        }
    }
    return total;
}

unsigned int loopC(unsigned int N){
    unsigned int total = 0;

    for(unsigned int i = 0; i < pow(N,2); i += 2) {
        for(unsigned int j = 1; j <= N; j *= 2) {
              for (unsigned int k = 0; k < N*i; ++k) {
                  total++;
            }
        }
    }
    return total;
}

unsigned int loopD(unsigned int N){
    unsigned int total = 0;

    for (unsigned int i = 0; i < N; ++i) {
        if (time(NULL) % 2 == 0) {
            total += loopA(i);
        }
        else {
              total += loopB(i);
        }
    }
    return total;
}

unsigned int loopE(unsigned int N){
    unsigned int total = 0;

    for (unsigned int i = 1; i <= N; i+=3){
        for (unsigned int j = 0; j < N; j++){
            total++;
        }
    }

    return total;
}
