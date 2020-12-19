/*
 * palindrome.cpp * This file contains `palindrome` program to identify palindromes.
 *
 * The palindrome test is handled by isPalindrome, while all
 * interaction is handled in main.
 */

#include <iostream>
#include <string>

using namespace std;

/*
 * isPalindrome()
 * returns true iff `text` is the same backwards and forwards.
 *
 * input:  (TODO - A string 
 * output: (TODO - True if the input is a palindrome, and false otherwise
dh
 *
 *   We currently require the ASCII characters in the string to
 *   be identical backwards and forwards, rather than only caring
 *   about the letters. Example: "tacocat" would return True, but
 *   "Tacocat" or "TacoCat" would return False.
 *
 * todo: (1) Ignore Spaces and punctuation
 *       (2) Ignore capitalization
 */
bool isPalindrome(string text /*<-- Candidate palindrome.*/){

    int left  = 0;                      // Indexes of the leftmost and
    int right = text.length() - 1;      // rightmost unchecked character.
    int LOWER_VALUE = 65;               // First char that will be checked "A"
    int HIGHER_VALUE = 122;             // Last char that will be checked, "z"
    // Check for a palindrome by moving left and right boundaries
    // closer until they finally meet or pass each other.
    // Bail early (return false) if we find a mismatch.
    while (left < right) {
      if (LOWER_VALUE <= text[left] && HIGHER_VALUE>= text[left]){
       if (LOWER_VALUE <=text[right] && HIGHER_VALUE >=text[right]){
           bool LequalsR=( text[left] == text[right]);
	   bool LequalsRMinus32 = (text[left]== text[right]-32);
	   bool LequalsRPlus32 = (text[left]== text[right] + 32);
        if (LequalsR || LequalsRMinus32 || LequalsRPlus32 ){
         ++left;
         --right;}
	 else{
	  return false;}
	 }
	else{
	 --right;}
        }
       else{
       ++left;
       }
}

   
    // All the character pairs matched. It's a palindrome!
    return true;
}


/*
 * Reads a potential palindrome from cin; checks if it is one (or not)
 *
 * input: Command line arguments are ignored.
 * output: If program exits with no errors, main will
 *         return 0 (just like any regular main function)
 *
 */
int main (int, const char*[])
{
    cout << "Enter possible palindrome: ";
    string line;

    getline(cin, line);

    if (isPalindrome(line))
        cout << "Yay, that's a palindrome!" << endl;
    else
        cout << "No, that's not a palindrome." << endl;

    return 0;
}
