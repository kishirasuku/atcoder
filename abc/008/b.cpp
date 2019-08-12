#include<iostream>
#include<string>
#include<vector>

struct Candidate_data{
  std::string name;
  int voted_num;

  void voted(){
    voted_num++;
  }
};

int main(){
  int vote_sums;
  std::cin >> vote_sums;
  std::vector<Candidate_data> datas;

  std::string names_1;
  std::cin >> names_1;
  datas.push_back({names_1,1});

  for(int i=1;i<vote_sums;i++){
    std::string names;
    std::cin >> names;

    for(auto c:datas){
      if(c.name.compare(names) == true){
	c.voted();
      }else{
	Candidate_data new_person;
	new_person.name = names;
	new_person.voted_num = 0;
	new_person.voted();
	
	datas.push_back(new_person);
      }
    }
  }

  Candidate_data elected = datas[0];
  
  for(auto& c:datas){
    if(c.voted_num > elected.voted_num){
      elected = c;
    }
  }

  std::cout << elected.name << "\n";

  return 0;
}
