#include <iostream>
#include <string>

int main()
{
    float peso = 0;
    float altura = 0;

    std::cout << "Digite o seu peso em quilos:" << std::endl;
    std::cin >> peso;
    std::cout << "Digite a sua altura em metros:" << std::endl;
    std::cin >> altura;

    float IMC = peso/(altura*altura);

    std::cout << "Seu IMC é de :";
    std::cout << IMC;
}