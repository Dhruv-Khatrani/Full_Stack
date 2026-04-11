#include<iostream>
usin namespace std;

void call()
{
	int sum=1;
	int i;
	for(i=1;i<=5;i++){
		sum=sum*i;
		cout"\nfactorial= %d"<<sum;
	}
}

int main()
{
   call();
	return 0;
}
