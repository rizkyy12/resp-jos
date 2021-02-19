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

int bagi(double a, double b){
    int hasil = a / b;
    return hasil;
}

int kali(double a, double b){
    int hasil = a * b;
    return hasil;
}

int main(){
    int a, b;
    double hasil1, hasil2, hasil3, hasil4;
    cout << "== aritmatika == \n";
    cout << "Masukan angka : ";
    cin >> a;
    cin >> b;
    hasil1 = tambah(a, b);
    hasil2 = kurang(a, b);
    hasil3 = bagi(a, b);
    hasil4 = kali(a, b);
    cout << "Penjumlahan = " << hasil1 << endl;
    cout << "Pengurangan = " << hasil2 << endl;
    cout << "Pembagian = " << hasil3 << endl;
    cout << "Perkalian = " << hasil4 << endl;
}
