#include "d3_solution.h"

// Reads input file and stores it into a vector
vector<string> d3::getFileInput()
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

char d3::findSharedLetter(string &input)
{
    char sharedLetter;
    map<char, int> firstHalf, secondHalf;

    for (int i = 0; i < (input.length() / 2); i++)
    {

        firstHalf.insert(make_pair(input[i], i));
        secondHalf.insert(make_pair(input[(input.length() / 2) + i], i));

        if (firstHalf.find(input[(input.length() / 2) + i]) != firstHalf.end())
        {
            sharedLetter = input[(input.length() / 2) + i];
            return sharedLetter;
        }
        else if (secondHalf.find(input[i]) != secondHalf.end())
        {
            sharedLetter = input[i];
            return sharedLetter;
        }
    }

    return sharedLetter;
}

char d3::findSharedLetter(string &input1, string &input2, string &input3)
{
    char sharedLetter;
    map<char, int> first, second, third;

    for (int i = 0; i < input1.length(); i++)
    {
        first.insert(make_pair(input1[i], i));
    }

    for (int i = 0; i < input2.length(); i++)
    {
        second.insert(make_pair(input2[i], i));
    }

    for (int i = 0; i < input3.length(); i++)
    {
        third.insert(make_pair(input3[i], i));
    }

    for (int i = 0; i < input1.length(); i++)
    {
        if (second.find(input1[i]) != second.end() && third.find(input1[i]) != third.end())
        {
            sharedLetter = input1[i];
        }
    }

    return sharedLetter;
}

int d3::charToNum(char &letter)
{
    int num;

    if (islower(letter))
    {
        num = (int)letter - 96; // 1-26
    }
    else
    {
        num = (int)letter - 38; // 27-52
    }

    return num;
}

int d3::problem1()
{
    vector<string> fileInput = getFileInput();
    char sharedLetter;
    int total = 0;

    for (int i = 0; i < fileInput.size(); i++)
    {
        sharedLetter = findSharedLetter(fileInput.at(i));
        total += charToNum(sharedLetter);
    }

    return total;
}

int d3::problem2()
{
    vector<string> fileInput = getFileInput();
    char sharedLetter;
    int total = 0;

    for (int i = 0; i < fileInput.size(); i += 3)
    {
        sharedLetter = findSharedLetter(fileInput.at(i), fileInput.at(i + 1), fileInput.at(i + 2));
        total += charToNum(sharedLetter);
    }

    return total;
}

int main()
{
    d3 day3;

    // Part 1
    cout << "== Part 1 ==" << endl
         << day3.problem1() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << day3.problem2() << endl;

    return 0;
}