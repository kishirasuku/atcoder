#include<iostream>
#include<vector>
#include<algorithm>

bool n_in_ng(int n,std::vector<int> ng){
  for(auto number:ng){
    if(n==number){
      return true;
    }
  }

  return false;
}

int step(int n,std::vector<int> ng){
  if(!n_in_ng(n-3,ng)){
    return n-3;
  }else if(!n_in_ng(n-2,ng)){
    return n-2;
  }else if(!n_in_ng(n-1,ng)){
    return n-1;
  }else{
    return -1;
  }
}

int main(){
  int n;
  std::vector<int> ng;

  std::cin >> n;
  for(int i=0;i<3;i++){
    int num;
    std::cin >> num;
    ng.push_back(num);
  }

  std::sort(ng.begin(),ng.end());

  if(n_in_ng(n,ng)){
    std::cout << "NO\n";
    return 0;
  }

  for(int i=0;i<100;i++){
    if(n>3){
      n = step(n,ng);
    }else if(n<=3 && n>=0){
      n=0;
    }
  }

  if(n==0){
    std::cout << "YES\n";
    return 0;
  }else{
    std::cout << "NO\n";
    return 0;
  }
}
