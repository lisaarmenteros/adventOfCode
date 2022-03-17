#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// Opens file and converts file input to vector
void getFileInput(vector<string> &fileInput)
{
    string line;

    fstream file("../input/d3_input.txt");

    if (!file)
        cout << "Error opening file!";
    else
        while (getline(file, line))
            fileInput.push_back(line);
}

void calculate(vector<string> &fileInput, vector<char> &gamma, vector<char> &epsilon)
{
    int numOnes=0, numZeros=0;

    for(int i = 0; i < fileInput.at(0).size(); i++)
    {
        for(int j=0; j < fileInput.size(); j++)
        {
            if (fileInput.at(j)[i] == '0')
                numZeros++;
            else if (fileInput.at(j)[i] == '1')
                numOnes++;
        }
        // Reset counter values and pushback higher one
        if (numZeros > numOnes)
        {
            gamma.push_back('0');
            epsilon.push_back('1');
        }
        else
        {
            gamma.push_back('1');
            epsilon.push_back('0');
        }
        numZeros=0;
        numOnes=0;
    }

    cout << "Gamma: "  << stoi(&gamma.at(0), 0, 2) << endl;
    cout << "Epsilon:" << stoi(&epsilon.at(0), 0 , 2) << endl;
    cout << "Consumption: " << stoi(&gamma.at(0), 0, 2) * stoi(&epsilon.at(0), 0 , 2) << endl;
}

int main ()
{
    vector<string> fileInput;
    vector<char> gamma;
    vector<char> epsilon;
    
    getFileInput(fileInput);
    calculate(fileInput, gamma, epsilon);
    
    return 0;
}