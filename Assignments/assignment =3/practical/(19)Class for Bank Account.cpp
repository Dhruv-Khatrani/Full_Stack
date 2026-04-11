#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance; 

public:
    
    BankAccount(double initialBalance) {
        if(initialBalance >= 0)
            balance = initialBalance;
        else
            balance = 0;
    }

    void deposit(double amount) {
        if(amount > 0) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        } else {
            cout << "Invalid deposit amount!" << endl;
        }
    }

    void withdraw(double amount) {
        if(amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
        } else {
            cout << "Insufficient balance or invalid amount!" << endl;
        }
    }

    void displayBalance() {
        cout << "Current balance: $" << balance << endl;
    }
};

int main() {
    BankAccount account(500); 

    account.displayBalance();
    
    account.deposit(200);      
    account.displayBalance();
    
    account.withdraw(100);     
    account.displayBalance();
    
    account.withdraw(700);     

    return 0;
}
