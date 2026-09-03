#include <iostream>
#include <string>

int main()
{
    std::string texto;
    std::cout << "Digite uma frase para ser invertida:" << std::endl;
    std::getline(std::cin, texto);
    std::string texto_invertido(texto.rbegin(), texto.rend());
    std::cout << texto_invertido;
}