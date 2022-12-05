#include "d5_solution.h"

// Reads input file and stores it into a vector
vector<string> d5::getFileInput()
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

int d5::ctoi(char &c)
{
    return c - '0';
}

int d5::getNumStacks(string &line)
{
    int numStacks = 0;

    for (int i = 1; i < line.length(); i++)
    {
        // Using ascii values to determine if contains int
        if ((int)line[i] >= 49 && (int)line[i] <= 57)
        {
            numStacks = ctoi(line[i]);
        }
    }

    return numStacks;
}

int d5::getStackIndex(vector<string> &fileInput)
{
    int index = 0;

    for (int i = 0; i < fileInput.size(); i++)
    {
        // Using ascii values to determine if contains int
        if ((int)fileInput.at(i)[1] >= 49 && (int)fileInput.at(i)[1] <= 57)
        {
            index = i;
            break;
        }
    }

    return index;
}

void d5::initializeStacks(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS, const int &STACK_INDEX)
{
    vector<char> crates;
    int currStackIndex = 1;

    for (int i = 0; i < NUM_STACKS; i++)
    {
        for (int j = STACK_INDEX - 1; j >= 0; j--)
        {
            if (fileInput.at(j)[currStackIndex] != ' ')
            {
                crates.push_back(fileInput.at(j)[currStackIndex]);
            }
        }

        stacks.push_back(crates);

        // Shifts over to location of next crate content
        currStackIndex += 4;
        crates.clear();
    }

    return;
}

vector<int> d5::getInstuctions(string s)
{
    vector<int> instructions;
    string delimiter;
    string subString;

    // remove "move"
    s.erase(0, s.find(" ") + 1);

    subString = s.substr(0, s.find(" "));
    instructions.push_back(stoi(subString));
    s.erase(0, s.find(" ") + 1);

    // remove "from"
    s.erase(0, s.find(" ") + 1);

    subString = s.substr(0, s.find(" "));
    instructions.push_back(stoi(subString));
    s.erase(0, s.find(" ") + 1);

    // remove "to"
    s.erase(0, s.find(" ") + 1);

    subString = s.substr(0, s.find(" "));
    instructions.push_back(stoi(subString));

    return instructions;
}

void d5::crateMover9000(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS)
{
    char crate;
    int
        numToMove,
        sourceCrate,
        destCrate;

    vector<int> instructions;

    for (int i = NUM_STACKS + 1; i < fileInput.size(); i++)
    {
        instructions = getInstuctions(fileInput.at(i));

        numToMove = instructions.at(0);
        sourceCrate = instructions.at(1);
        destCrate = instructions.at(2);

        for (int j = 0; j < numToMove; j++)
        {
            stacks.at(destCrate - 1).push_back(stacks.at(sourceCrate - 1).back());
            stacks.at(sourceCrate - 1).pop_back();
        }
    }

    return;
}

void d5::crateMover9001(vector<string> &fileInput, vector<vector<char>> &stacks, const int &NUM_STACKS)
{
    char crate;
    int
        numToMove,
        sourceCrate,
        destCrate;

    vector<int> instructions;
    vector<char> crates;

    for (int i = NUM_STACKS + 1; i < fileInput.size(); i++)
    {
        instructions = getInstuctions(fileInput.at(i));

        numToMove = instructions.at(0);
        sourceCrate = instructions.at(1);
        destCrate = instructions.at(2);

        for (int j = 0; j < numToMove; j++)
        {
            // Get crate from sourceCrate and remove it from the stack.
            // Then add it to new stack to simulate moving more than one at a time
            crates.push_back(stacks.at(sourceCrate - 1).back());
            stacks.at(sourceCrate - 1).pop_back();
        }

        for (int k = 0; k < numToMove; k++)
        {
            crate = crates.back();
            crates.pop_back();

            // Add crates removed from sourceCrate to destCrate
            stacks.at(destCrate - 1).push_back(crate);
        }
    }

    return;
}

string d5::problem1()
{
    vector<string> fileInput = getFileInput();
    string returnVal = "";
    vector<vector<char>> stacks;

    const int STACK_INDEX = getStackIndex(fileInput);
    const int NUM_STACKS = getNumStacks(fileInput.at(STACK_INDEX));

    // Initialize stacks
    initializeStacks(fileInput, stacks, NUM_STACKS, STACK_INDEX);

    // Follow instructions
    crateMover9000(fileInput, stacks, NUM_STACKS);

    // Get results
    for (int i = 0; i < stacks.size(); i++)
    {
        returnVal += stacks.at(i).back();
    }

    return returnVal;
}

string d5::problem2()
{
    vector<string> fileInput = getFileInput();
    string returnVal = "";
    vector<vector<char>> stacks;

    const int STACK_INDEX = getStackIndex(fileInput);
    const int NUM_STACKS = getNumStacks(fileInput.at(STACK_INDEX));

    // Initialize stacks
    initializeStacks(fileInput, stacks, NUM_STACKS, STACK_INDEX);

    // Follow instructions
    crateMover9001(fileInput, stacks, NUM_STACKS);

    // Get results
    for (int i = 0; i < stacks.size(); i++)
    {
        returnVal += stacks.at(i).back();
    }

    return returnVal;
}

int main()
{
    d5 day5;

    // Part 1
    cout << "== Part 1 ==" << endl
         << day5.problem1() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << day5.problem2() << endl;

    return 0;
}