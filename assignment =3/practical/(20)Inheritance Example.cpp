#include <iostream>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:

    void setDetails() {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter age: ";
        cin >> age;
    }

    void displayDetails() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Student : public Person {
private:
    int studentID;
    string course;

public:
    void setStudentDetails() {
        setDetails(); 
        cout << "Enter Student ID: ";
        cin >> studentID;
        cout << "Enter Course: ";
        cin >> course;
    }

    void displayStudentDetails() {
        displayDetails(); 
        cout << "Student ID: " << studentID << ", Course: " << course << endl;
    }
};

class Teacher : public Person {
private:
    string subject;
    double salary;

public:
    void setTeacherDetails() {
        setDetails(); 
        cout << "Enter Subject: ";
        cin >> subject;
        cout << "Enter Salary: ";
        cin >> salary;
    }

    void displayTeacherDetails() {
        displayDetails(); 
        cout << "Subject: " << subject << ", Salary: $" << salary << endl;
    }
};

int main() {
    Student stu;
    Teacher tch;

    cout << "Enter Student Details:\n";
    stu.setStudentDetails();
    cout << "\nEnter Teacher Details:\n";
    tch.setTeacherDetails();

    cout << "\n--- Student Info ---\n";
    stu.displayStudentDetails();

    cout << "\n--- Teacher Info ---\n";
    tch.displayTeacherDetails();

    return 0;
}
