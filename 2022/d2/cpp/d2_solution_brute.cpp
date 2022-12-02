#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int getScore()
{
    string line;
    int score = 0;

    fstream file("../input/input.txt");

    if (!file)
    {
        cout << "Error opening file!";
    }
    else
    {
        while (getline(file, line))
        {
            switch (line[2])
            {
            case 'X':
                if (line[0] == 'B') // Loss
                {
                    score += 1; // Point for playing rock
                }
                else if (line[0] == 'C') // Win
                {
                    score += 1 + 6; // Point for playing rock (1) + points for win (6)
                }
                else // Draw
                {
                    score += 1 + 3; // Point for playing rock (1) + points for draw (3)
                }
                break;
            case 'Y':
                if (line[0] == 'C') // Loss
                {
                    score += 2; // Points for playing paper
                }
                else if (line[0] == 'A') // Win
                {
                    score += 2 + 6;
                }
                else // Draw
                {
                    score += 2 + 3;
                }
                break;
            case 'Z':
                if (line[0] == 'A') // Loss
                {
                    score += 3;
                }
                else if (line[0] == 'B') // Win
                {
                    score += 3 + 6;
                }
                else
                {
                    score += 3 + 3;
                }
                break;
            default:
                break;
            }
        }
    }

    return score;
}

int getScore2()
{
    string line;
    int score = 0;

    fstream file("../input/input.txt");

    if (!file)
    {
        cout << "Error opening file!";
    }
    else
    {
        while (getline(file, line))
        {
            switch (line[2])
            {
            case 'X': // Must Lose
                if (line[0] == 'A')
                {
                    score += 3;
                }
                else if (line[0] == 'B')
                {
                    score += 1;
                }
                else
                {
                    score += 2;
                }
                break;
            case 'Y': // Must end in draw
                if (line[0] == 'A')
                {
                    score += 3 + 1;
                }
                else if (line[0] == 'B')
                {
                    score += 3 + 2;
                }
                else // Draw
                {
                    score += 3 + 3;
                }
                break;
            case 'Z': // Must Win
                if (line[0] == 'A')
                {
                    score += 6 + 2;
                }
                else if (line[0] == 'B')
                {
                    score += 6 + 3;
                }
                else
                {
                    score += 6 + 1;
                }
                break;
            default:
                break;
            }
        }
    }

    return score;
}

int main()
{
    // Part 1
    cout << "== Part 1 ==" << endl
         << getScore() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << getScore2() << endl;

    return 0;
}