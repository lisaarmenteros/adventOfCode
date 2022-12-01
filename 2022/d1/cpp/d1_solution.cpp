#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Opens file and converts file input to vector of elves and their total calories consumed
vector<int> getElves()
{
    vector<int> elves;
    string line;
    int sum = 0;

    fstream file("../input/input.txt");

    if (!file)
    {
        cout << "Error opening file!";
    }
    else
    {
        while (getline(file, line))
        {
            if (line.empty())
            {
                elves.push_back(sum);
                sum = 0;
            }
            else
            {
                sum += stoi(line);
            }
        }
    }

    return elves;
}

int findMax(vector<int> &elves)
{
    return elves.at(elves.size() - 1);
}

int topThreeTotal(vector<int> &elves)
{
    return elves.at(elves.size() - 1) + elves.at(elves.size() - 2) + elves.at(elves.size() - 3);
}

int main()
{
    vector<int> elves = getElves();

    sort(elves.begin(), elves.end());

    // Part 1
    cout << "== Part 1 ==" << endl
         << findMax(elves) << endl
         << endl;

    // Part 2
    cout << "== Part 2 == " << endl
         << topThreeTotal(elves) << endl;

    return 0;
}