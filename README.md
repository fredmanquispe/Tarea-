# Tarea-

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
