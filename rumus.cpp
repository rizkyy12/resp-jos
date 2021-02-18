// Function of calculated Area and Perimeter a rectangle

#include <iostream>

using namespace std;

int hitung_luas(int p, int l){
  int hasil;
  hasil = p * l;
  return hasil;
}

void tampilkan_luas(int p, int l){
  cout << "Luasnya adalah : ";
  cout << hitung_luas(p, l);
  cout << endl;
}

int hitung_keliling(int p, int l){
  int hasil;
  hasil = 2*(p+l);
  return hasil;
} 

void tampilkan_keliling(int p, int l){
  cout << "Kelilingnya adalah : ";
  cout << hitung_keliling(p, l);
  cout << endl;
}
int main(){
  int panjang, lebar;
  cout << "== Hitung Luas =="<< endl;
  cout << "Panjang : ";
  cin >> panjang;
  cout << "Lebar : ";
  cin >> lebar;
  tampilkan_luas(panjang, lebar);
  tampilkan_keliling(panjang, lebar);
}
