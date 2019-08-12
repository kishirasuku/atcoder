#include<iostream>
#include<string>

int main(){
  std::string s_input;
  std::cin >> s_input;

  if(!s_input.compare("a")){
    std::cout << "-1\n";
  }else{
    std::cout << "a\n";
  }

  return 0;
}
