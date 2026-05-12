#include <iostream>
#include <string>

using namespace std;

class Config {
private:
    static Config* instance;
    string sistemaNombre;

    // Constructor privado: esencia del patrón Singleton
    Config() {
        sistemaNombre = "Sistema de Ingenieria de Sistemas - UNA";
    }

public:
    // Método para obtener la instancia única
    static Config* getInstance() {
        if (instance == nullptr) {
            instance = new Config();
        }
        return instance;
    }

    void showMessage() {
        cout << "Configuracion global cargada: " << sistemaNombre << endl;
    }
};

// Inicialización del puntero estático
Config* Config::instance = nullptr;

int main() {
    // Obtenemos la instancia única
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();

    obj1->showMessage();

    // Verificación de que son la misma instancia
    if (obj1 == obj2) {
        cout << "Resultado: Ambos objetos apuntan a la misma instancia (Singleton exitoso)." << endl;
    }

    return 0;
}
