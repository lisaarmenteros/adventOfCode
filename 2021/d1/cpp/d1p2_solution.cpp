#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

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

int depthSweep(vector<int> &fileInput)
{
    int count = 0;

    for (int i = 0; i < fileInput.size() - 3; i++)
        if ((fileInput.at(i) + fileInput.at(i + 1) + fileInput.at(i + 2)) < (fileInput.at(i + 1) + fileInput.at(i + 2) + fileInput.at(i + 3)))
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