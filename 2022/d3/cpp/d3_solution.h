#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class d3
{
private:
    char findSharedLetter(string &input);
    char findSharedLetter(string &input1, string &input2, string &input3);
    vector<string> getFileInput();
    int charToNum(char &letter);

public:
    int problem1();
    int problem2();
};