#include "d6_solution.h"

// Reads input file and stores it into a string
string d6::getFileInput()
{
    string line;

    fstream file("../input/input.txt");

    if (!file)
    {
        cout << "Error opening file!";
    }
    else
    {
        getline(file, line);
    }

    return line;
}

int d6::signalLockOn(string &input, const int numToLockOn)
{
    set<char> s;
    int i = 0, startIndex = 0;

    while (s.size() != numToLockOn && startIndex + i < input.size())
    {
        if (s.find(input[startIndex + i]) != s.end())
        {
            s.clear();
            startIndex++;
            i = 0;
        }
        else
        {
            s.insert(input[startIndex + i]);
            i++;
        }
    }

    return startIndex + i;
}

int d6::problem1()
{
    string input = getFileInput();

    return signalLockOn(input, 4);
}

int d6::problem2()
{
    string input = getFileInput();

    return signalLockOn(input, 14);
}

int main()
{
    d6 day6;

    // Part 1
    cout << "== Part 1 ==" << endl
         << day6.problem1() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << day6.problem2() << endl;

    return 0;
}