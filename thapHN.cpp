#include <iostream>
using namespace std;
int c[3] = {'A', 'B', 'C'};

void thap(int n, int i, int j, int k)
{
    if (n == 1)
    {
        cout << "Chuyen dia " << n << " tu cot " << c[i] << " sang cot " << c[j] << endl;
    }
    else
    {
        thap(n - 1, i, k, j);
        cout << "Chuyen dia " << n << " tu cot " << c[i] << " sang cot " << c[j] << endl;
        thap(n - 1, k, j, i);
    }
}

int main()
{
    int n;

    cout << "Nhap so luong dia: ";
    cin >> n;

    thap(n, 0, 2, 1);
    return 0;
}