#include <iostream>

using namespace std;

int main() {
  long prod = 1;
  int sum;
  for (long i = 100; i > 1; --i) {
    prod = prod * i;
    cout << prod << endl;
  }

  cout << prod << endl;
}
