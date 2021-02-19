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

void tampilkan(double a, double b){
    cout << "Hasilnya : \n";
    cout << "Tambah : ";
    cout << tambah(a, b) << endl;
    cout << "Kurang : ";
    cout << kurang(a, b) << endl;
    cout << "Bagi : ";
    cout << bagi(a, b) << endl;
}
int main(){
    int a, b;
    double hasil1, hasil2, hasil3;
    cout << "== aritmatika == \n";
    cout << "Masukan angka : ";
    cin >> a;
    cin >> b;
    tampilkan(a, b);
}
