# Tarea-

# Práctica: Patrones de Diseño Creacionales
**Escuela Profesional de Ingeniería de Sistemas - UNA**

* **Nombre:** Hanz Fredman Quispe Quispe
* **Curso:** Lenguajes de Programación Orientada a Objetos II
* **Docente:** Mg. Aldo Hernán Zanabria Gálvez

## Trabajo de Investigación (Patrones Creacionales)

### 1. Django ORM y el uso de Factory
En el framework **Django (Python)**, el patrón Factory se manifiesta a través de los Managers. Cuando utilizamos Model.objects.create(), el `Manager actúa como una fábrica que encapsula la lógica de instanciación del objeto y su persistencia en la base de datos. Esto permite que el desarrollador cree registros sin preocuparse por la complejidad interna de la creación del objeto y su relación con el motor de base de datos.

### 2. Spring Boot y el patrón Singleton
En el ecosistema de **Spring Boot (Java)**, el patrón Singleton es el núcleo de la gestión de dependencias. Por defecto, todos los objetos gestionados por el contenedor de Spring (conocidos como *Beans*) son **Singletons**. Spring garantiza que solo exista una instancia de cada Bean por contexto de aplicación, lo que optimiza el uso de memoria y asegura que servicios como la conexión a bases de datos o controladores de seguridad sean compartidos de manera consistente por toda la aplicación.

### 3. Patrón Builder en bibliotecas de Interfaz de Usuario (UI)
El patrón Builder es ampliamente utilizado en el desarrollo de interfaces gráficas para configurar componentes complejos de forma legible:
* **Android/Flutter:** Se utiliza en la creación de cuadros de diálogo (AlertDialog.Builder). Permite configurar el título, el mensaje, los botones y los iconos paso a paso antes de llamar al método .show() o .create().
* **Qt (C++):** Se emplea para la construcción de escenas gráficas y layouts donde se definen múltiples propiedades de un widget antes de su renderización final, evitando constructores con excesivos parámetros opcionales.

## Informe Comparativo de Patrones Creacionales

A continuación, se presenta un análisis comparativo de los tres patrones implementados en esta práctica:

| Característica | Singleton | Factory Method | Builder |
| :--- | :--- | :--- | :--- |
| **Propósito principal** | Garantizar una única instancia. | Delegar la creación de objetos. | Construcción paso a paso. |
| **Flexibilidad** | Baja (está ligado a una clase). | Alta (permite añadir productos). | Muy Alta (configuraciones variadas). |
| **Complejidad** | Muy baja. | Media. | Alta (requiere un Director/Builder). |
| **Cuándo usarlo** | Para recursos compartidos (BD). | Cuando no sabes qué objeto crear. | Cuando el objeto tiene muchas partes. |

### Conclusiones Técnicas
1. **Singleton** fue el más sencillo de implementar en C++, pero requiere cuidado con los hilos y punteros estáticos.
2. **Factory Method** en Python demostró ser muy útil para desacoplar el código; si mañana añadimos un transporte aéreo, el cliente no sufriría cambios.
3. **Builder** es, sin duda, la mejor opción para el caso del "Fast Food", ya que permite personalizar cada pedido (combo) de manera independiente antes de finalizar la construcción.
