#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> getFileInput()
{
    vector<int> fileInput;
    string line;

    fstream file("../input/d1_input.txt");

    if (!file)
        cout << "Error opening file!";
    else
        while (getline(file, line))
            fileInput.push_back(stoi(line));

    return fileInput;
}

int depthSweep(vector<int> inputFile)
{
    int count = 0;

    for (int i = 0; i < inputFile.size() - 3; i++)
        if ((inputFile.at(i) + inputFile.at(i + 1) + inputFile.at(i + 2)) < (inputFile.at(i + 1) + inputFile.at(i + 2) + inputFile.at(i + 3)))
            count++;

    return count;
}

int main()
{
    vector<int> inputFile = getFileInput();
    cout << depthSweep(inputFile);
    return 0;
}