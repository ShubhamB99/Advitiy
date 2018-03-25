#include<iostream>

using namespace std;

int main()
{
    int n, start, finish;
    char sentence[1024];
    cin.getline(sentence, 1024);

    for (n=0;sentence[n] != '\0'; n++);

    start = finish = n;
    for (int i=n-1; i>=0; i--)
    {
        if (i == 0)
        {
            for (int a=0; a<finish; a++)
                cout<<sentence[a];
            cout<<" ";
        }

        else if (sentence[i] == ' ')
        {
            start = i+1;
            for (int a=start; a<finish; a++)
                cout<<sentence[a];
            cout<<" ";
        }

        finish = start;
    }
    return 0;
}
