#include <iostream>

using namespace std;
int main(){
    int n;
    int fn;
    int fn1 = 1;
    int fn2 = 0;

    cout << "== Fibonaci =="<< endl;
    cout << "Masukan nilai ke n : ";
    cin >> n;
    cout << fn1<< endl;
    for(int i = 1; i < n; i++) {
        fn = fn1 + fn2;
        fn2 = fn1;
        fn1 = fn;
        cout << fn << endl;
    }
}
