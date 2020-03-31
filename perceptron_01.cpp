#include <iostream>
#include <stdio.h>
#include <random>
using namespace std;
int sign(int n){
  if (n>0){return 1;}
  else{return -1;}
}
class perceptron{
  int sum=0;
  //randomize();
  float weight[2];
public:
    void weight_cal(){
    int HIGH = -1;
    int LOW  =  1;
    int n = sizeof(weight);
    int i;
    for(i=0;i<n;i++)
    {
      weight[i]=rand() % (HIGH - LOW + 1) + LOW;
    }
  }

  int guess(float inputs[],int size)
  {
    for (int i=0;i<sizeof(weight);i++)
    {
      sum += inputs[i]*weight[i];
    }

  int output = sign (sum);
  return output;
 }
};

int main(){
  perceptron p;
  float inputs[]={-1,0.5};
  int n=sizeof(inputs);
  int guess = p.guess(inputs,n);
  cout<<guess;
  return 0;
}
