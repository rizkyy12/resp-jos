#include <iostream>
#include <cmath>

using namespace std;

int tambah(double a, double b){
    int hasil = a + b;
    return hasil;
}

int kurang(double a, double b){
    int hasil = a - b;
    return hasil;
}
int main(){
    double a, b;
    int hasil1, hasil2;
    cout << "== aritmatika == \n";
    cout << "1. Penjumlahan \n";
    cin >> a;
    cin >> b;
    hasil1 = tambah(a, b);
    hasil2 = kurang(a, b);
    cout << "Penjumlahan = " << hasil1 << endl;
    cout << "Pengurangan = " << hasil2 << endl;
}