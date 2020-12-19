#include <iostream>

using namespace std;

int main(){
    
    const int NUM_VALUES = 2;
    int* values = new int[NUM_VALUES];
    int* otherValues = values;

    for (size_t i = 0; i < NUM_VALUES; ++i) {
        values[i] = 70;
    }

    delete [] values;
    
    for (size_t i = 0; i <= NUM_VALUES; ++i) {
        cout << otherValues[i] << endl;
    }

    return 0;
}
