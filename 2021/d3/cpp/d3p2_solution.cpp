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

void removeOnes(vector<string> &binaryList, int index)
{
    for (int i=0; i < binaryList.size(); i++)
    {
        if (binaryList.at(i)[index] == '1')
        {
            binaryList.erase(binaryList.begin() + i);
            i--;
        }
    }
}

void removeZeros(vector<string> &binaryList, int index)
{
     for (int i=0; i < binaryList.size(); i++)
    {
        if (binaryList.at(i)[index] == '0')
        {
            binaryList.erase(binaryList.begin() + i);
            i--;
        }
    }
}

void calculateCO2 (vector<string> &co2Scrub)
{
    int numOnes=0, numZeros=0;

    for(int i = 0; i < co2Scrub.at(0).size(); i++)
    {
        for(int j=0; j < co2Scrub.size(); j++)
        {
            if (co2Scrub.at(j)[i] == '0')
                numZeros++;
            else if (co2Scrub.at(j)[i] == '1')
                numOnes++;
        }
        
        if (co2Scrub.size() == 1)
            return;
        else if (numZeros > numOnes)
            removeZeros(co2Scrub, i);

        else
            removeOnes(co2Scrub, i);

        numZeros=0;
        numOnes=0;
    }
}

void calculateOxygen(vector<string> &oxygenGenRating)
{
    int numOnes=0, numZeros=0;

    for(int i = 0; i < oxygenGenRating.at(0).size(); i++)
    {
        for(int j=0; j < oxygenGenRating.size(); j++)
        {
            if (oxygenGenRating.at(j)[i] == '0')
                numZeros++;
            else if (oxygenGenRating.at(j)[i] == '1')
                numOnes++;
        }
        
        if (oxygenGenRating.size() == 1)
            return;
        else if (numZeros > numOnes)
            removeOnes(oxygenGenRating, i);
        else
            removeZeros(oxygenGenRating, i);
        numZeros=0;
        numOnes=0;
    }
}

int main ()
{
    vector<string> oxygenGenRating;
    vector<string> co2Scrub;
    
    getFileInput(oxygenGenRating);

    co2Scrub = oxygenGenRating;
    
    calculateOxygen(oxygenGenRating);
    calculateCO2(co2Scrub);

    cout << "Oxygen Generator Rating: " << stoi(oxygenGenRating.at(0), 0, 2) << endl;
    cout << "CO2 Scrubber Rating: " << stoi(co2Scrub.at(0), 0, 2) << endl;
    cout << "Life Support: " << stoi(oxygenGenRating.at(0), 0, 2) * stoi(co2Scrub.at(0), 0, 2) << endl;

    return 0;
}