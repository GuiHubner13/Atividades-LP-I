#include <iostream>
#include <string>

int main()
{
    for (int i = 1; i < 31; i++){

        if (i % 3 == 0){
            cout << "Fizz" << endl;
        }
        if (i % 5 == 0){
            cout << "Buzz" << endl;
        }
        if (i % 3 == 0 && i % 5 == 0){
            cout << "FizzBuzz" << endl;
        }
        else {
            cout << i << endl;
        }
    }

}