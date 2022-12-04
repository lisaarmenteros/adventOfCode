#include "d4_solution.h"

// Reads input file and stores it into a vector
vector<string> d4::getFileInput()
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

int d4::jobsOverlap(vector<int> job1, vector<int> job2)
{
    if (includes(job1.begin(), job1.end(), job2.begin(), job2.end()) || includes(job2.begin(), job2.end(), job1.begin(), job1.end()))
        return 1;

    return 0;
}

int d4::containsOverlap(vector<int> job1, vector<int> job2)
{
    if (find_first_of(job1.begin(), job1.end(), job2.begin(), job2.end()) != job1.end())
        return 1;

    return 0;
}

vector<int> d4::getJobs(string line)
{
    vector<int> jobs;
    string num;

    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == ',' || line[i] == '-')
        {
            jobs.push_back(stoi(num));
            num = "";
        }
        else
            num += line[i];
    }

    jobs.push_back(stoi(num));

    return jobs;
}

int d4::problem1()
{
    vector<string> input = getFileInput();
    vector<int> job1, job2;
    vector<int> jobs;
    int totalOverlaps = 0;

    for (int i = 0; i < input.size(); i++)
    {
        jobs = getJobs(input.at(i));

        for (int i = jobs.at(0); i < jobs.at(1) + 1; i++)
        {
            job1.push_back(i);
        }

        for (int i = jobs.at(2); i < jobs.at(3) + 1; i++)
        {
            job2.push_back(i);
        }

        totalOverlaps += jobsOverlap(job1, job2);

        job1.clear();
        job2.clear();
    }

    return totalOverlaps;
}

int d4::problem2()
{
    vector<string> input = getFileInput();
    vector<int> job1, job2;
    vector<int> jobs;
    int totalOverlaps = 0;

    for (int i = 0; i < input.size(); i++)
    {
        jobs = getJobs(input.at(i));

        for (int i = jobs.at(0); i < jobs.at(1) + 1; i++)
        {
            job1.push_back(i);
        }

        for (int i = jobs.at(2); i < jobs.at(3) + 1; i++)
        {
            job2.push_back(i);
        }

        totalOverlaps += containsOverlap(job1, job2);

        job1.clear();
        job2.clear();
    }

    return totalOverlaps;
}

int main()
{
    d4 day4;

    // Part 1
    cout << "== Part 1 ==" << endl
         << day4.problem1() << endl
         << endl;

    // Part 2
    cout << "== Part 2 ==" << endl
         << day4.problem2() << endl;

    return 0;
}