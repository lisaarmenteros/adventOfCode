#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// Opens file and converts file input to vector
void getFileInput(vector<int> &fileInput)
{
    string line;

    fstream file("../input/d1_input.txt");

    if (!file)
        cout << "Error opening file!";
    else
        while (getline(file, line))
            fileInput.push_back(stoi(line));
}

// Sweep depth and determine how many times it increments
int depthSweep(vector<int> &fileInput)
{
    int count = 0;

    for (int i = 0; i < fileInput.size() - 1; i++)
        if (fileInput.at(i + 1) > fileInput.at(i))
            count++;

    return count;
}

int main()
{
    vector<int> fileInput;
    getFileInput(fileInput);
    cout << depthSweep(fileInput);
    cout << endl;
    return 0;
}