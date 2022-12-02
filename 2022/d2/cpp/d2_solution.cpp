#include "d2_solution.h"

// Reads input file and stores it into a vector
vector<string> d2::getFileInput()
{
    vector<string> fileInput;
    string line;

    fstream file("../input/input.txt");

    if (!file)
    {
        cout << "Error opening file!";
    }
    else
    {
        while (getline(file, line))
        {
            fileInput.push_back(line);
        }
    }

    return fileInput;
}

// Calculates the winning hand and returns the points for the results
int d2::gameOutcome(char opponent, char you)
{
    int result = (rps.at(you) - rps.at(opponent)) % 3;

    // Win if result is 1 or -2 (Modulus 3 of a negative number is not returning as 1 for some reason. EX: 1-3 % 3)
    // Loss will result in result of 0
    return (result == 1 || result == -2) ? WIN : result == 0 ? DRAW : 0;
}

int d2::problem1()
{
    vector<string> input = getFileInput();
    int totalScore = 0;
    char yourHand, opponentHand;

    for (int i = 0; i < input.size(); i++)
    {
        opponentHand = input.at(i)[OPPONENT_INDEX];
        yourHand = input.at(i)[YOUR_INDEX];

        // Add the points based on hand played
        totalScore += rps.at(yourHand);
        
        // Add winning result
        totalScore += gameOutcome(opponentHand, yourHand);
    }

    return totalScore;
}

int d2::problem2()
{
    vector<string> input = getFileInput();
    int totalScore = 0;
    char outcome, opponent;

    for (int i = 0; i < input.size(); i++)
    {
        outcome = input.at(i)[YOUR_INDEX];
        opponent = input.at(i)[OPPONENT_INDEX];

        switch(outcome)
        {
        case 'X': // Must Lose
            totalScore += (rps.at(opponent) + 1) % 3 + 1;
            break;
        case 'Y': // Must Tie
            totalScore += rps.at(opponent) + DRAW;
            break;
        case 'Z': // Must Win
            totalScore +=  (((rps.at(opponent) + 3) % 3) + 1) + WIN;
            break;
        default:
            break;
        }
    }

    return totalScore;
}

int main()
{
    d2 day2;

    // Part 1
    cout << "== Part 1 ==" << endl
         << day2.problem1() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << day2.problem2() << endl;

    return 0;
}