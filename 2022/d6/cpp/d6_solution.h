#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <set>

using namespace std;

class d6
{
private:
    string getFileInput();
    int signalLockOn(string &input, int numToLockOn);

public:
    int problem1();
    int problem2();
};