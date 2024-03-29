#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class d2
{
private:
    static const int
        WIN = 6,
        DRAW = 3,
        OPPONENT_INDEX = 0,
        YOUR_INDEX = 2;
    const map<char, int> rps = {
        {'A', 1},
        {'B', 2},
        {'C', 3},
        {'X', 1},
        {'Y', 2},
        {'Z', 3}};

    vector<string> getFileInput();
    int gameOutcome(char opponent, char you);

public:
    int problem1();
    int problem2();
};
