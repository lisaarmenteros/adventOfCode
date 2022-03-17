#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// Opens file and converts file input to vector
void getFileInput(vector<string> &fileInput)
{
    string line;

    fstream file("../input/d2_input.txt");

    if (!file)
        cout << "Error opening file!";
    else
        while (getline(file, line))
            fileInput.push_back(line);
}

void instructions(vector<string> &fileInput, int &horizontal, int &depth, int &aim)
{
    string instruction;
    string direction;

    for(int i=0; i < fileInput.size(); i++)
    {
        instruction = fileInput.at(i).substr(0, fileInput.at(i).find(" "));
        direction = fileInput.at(i).substr(fileInput.at(i).find(" ") + 1);

        if (instruction == "forward")
        {
            horizontal += stoi(direction);
            depth += aim * stoi(direction);
        }
        else if (instruction == "down")
            aim += stoi(direction);
        else if (instruction == "up")
            aim -= stoi(direction);
    }
}

int main()
{
    int horizontal=0, depth=0, aim=0;
    vector<string> fileInput;
    
    getFileInput(fileInput);
    instructions(fileInput, horizontal, depth, aim);

    cout << "Result: " << horizontal * depth << endl;

    return 0;
}