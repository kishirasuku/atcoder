#include<iostream>

int main(){
  int month;
  std::cin >> month;

  if(month == 12){
    std::cout << 1 << "\n";
  }else{
    std::cout << month+1 << "\n";
  }

  return 0;
}
