#include <iostream>
#include <cmath>

using namespace std;

int tambah(int a, int b){
    double hasil = a + b;
    return hasil;
}

int kurang(int a, int b){
    double hasil = a - b;
    return hasil;
}
int main(){
    int a, b;
    double hasil1, hasil2;
    cout << "== aritmatika == \n";
    cout << "1. Penjumlahan \n";
    cin >> a;
    cin >> b;
    hasil1 = tambah(a, b);
    hasil2 = kurang(a, b);
    cout << "Penjumlahan = " << hasil1 << endl;
    cout << "Pengurangan = " << hasil2 << endl;
}