#include <iostream>
#include <vector>
#include <string>
#include <iomanip> 

struct Item {
    std::string nome;
    double preco;
    int quantidade;
};

int main() {
    
    std::vector<Item> lista_compras = {
        {"Arroz 1kg", 5.50, 2},
        {"Feijão 1kg", 8.00, 2},
        {"Patinho 500g", 21.50, 1}
    };

    double total = 0.0;


    std::cout << std::left << std::setw(15) << "Item" 
              << std::right << std::setw(10) << "Preço" 
              << std::setw(6) << "Qtd" 
              << std::setw(12) << "Total" << std::endl;
    
    std::cout << std::string(43, '-') << std::endl; 

    for (const auto& item : lista_compras) {
        double subtotal = item.preco * item.quantidade;
        total += subtotal;

        std::cout << std::left << std::setw(15) << item.nome 
                  << std::right << std::fixed << std::setprecision(2)
                  << std::setw(8) << "R$" << std::setw(8) << item.preco 
                  << std::setw(6) << item.quantidade 
                  << std::setw(8) << "R$" << std::setw(8) << subtotal << std::endl;
    }

    std::cout << std::string(43, '-') << std::endl;
    
    std::cout << std::left << std::setw(15) << "TOTAL GERAL" 
              << std::right << std::setw(8) << "" 
              << std::setw(8) << "" 
              << std::setw(8) << "R$" 
              << std::setw(8) << total << std::endl;

    return 0;
}