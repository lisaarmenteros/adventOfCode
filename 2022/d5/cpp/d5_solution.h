#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>

using namespace std;

class d5
{
private:
    vector<string> getFileInput();
    int getNumStacks(string &line);
    int getStackIndex(vector<string> &fileInput);
    int ctoi(char &c);
    void initializeStacks(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS, const int &STACK_INDEX);
    void crateMover9000(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS);
    void crateMover9001(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS);
    vector<int> getInstuctions(string s);

public:
    string problem1();
    string problem2();
};