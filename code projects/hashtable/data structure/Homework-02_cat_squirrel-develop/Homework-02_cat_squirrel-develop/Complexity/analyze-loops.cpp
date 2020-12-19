#include "loops.hpp"
#include <iostream>
#include <fstream>
#include <iomanip>  
using namespace std;

void loopATester();
void loopBTester();
void loopCTester();
void loopDTester();
void loopETester();

int main(){

    loopETester();
}
void loopATester(){
    ofstream myfile;
    myfile.open ("loopA.dat");
    myfile << "#  x        y\n";
    for(int x=1; x<=100; x++){
        unsigned int storeValue = loopA(x);
        myfile << "   ";
        myfile << x;
        myfile << setw(10);
        myfile << storeValue;
        myfile << "\n";
        
}
    myfile.close();}


void loopBTester(){
    ofstream myfile;
    myfile.open ("loopB.dat");
    myfile << "#  x        y\n";
    for(int x=1; x<=100; x++){
        unsigned int storeValue = loopB(x);
        myfile << "   ";
        myfile << x;
        myfile << setw(10);
        myfile << storeValue;
        myfile << "\n";
        
}
    myfile.close();}

void loopCTester(){
    ofstream myfile;
    myfile.open ("loopC.dat");
    myfile << "#  x             y \n";
    for(int x=1; x<=100; x++){
        unsigned int storeValue = loopC(x);
        myfile << setw(4);
        myfile << x;
        myfile << setw(14);
        myfile << storeValue;
        myfile << "\n";
        
}
    myfile.close();}



void loopDTester(){
    ofstream myfile;
    myfile.open ("loopD.dat");
    myfile << "#  x         y \n";
    for(int x=1; x<=100; x++){
        unsigned int storeValue = loopD(x);
        myfile << "   ";
        myfile << x;
        myfile << setw(10);
        myfile << storeValue;
        myfile << "\n";
        
}
    myfile.close();}

void loopETester(){
    ofstream myfile;
    myfile.open ("loopE.dat");
    myfile << "#  x         y \n";
    for(int x=1; x<=100; x++){
        unsigned int storeValue = loopE(x);
        myfile << "   ";
        myfile << x;
        myfile << setw(10);
        myfile << storeValue;
        myfile << "\n";
        
}
    myfile.close();}

