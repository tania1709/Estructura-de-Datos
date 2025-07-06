#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOMBRE 50
#define MAX_CORREO 100

// Estructura para representar un estudiante
typedef struct Estudiante {
    int cedula;
    char nombre[MAX_NOMBRE];
    char apellido[MAX_NOMBRE];
    char correo[MAX_CORREO];
    float nota;
    struct Estudiante* siguiente;
} Estudiante;

// Estructura para representar la lista de estudiantes
typedef struct {
    Estudiante* inicio;
    Estudiante* fin;
} ListaEstudi…
[00:25, 6/7/2025] Tania: .........................
[00:25, 6/7/2025] Tania: #include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOMBRE 50
#define MAX_CORREO 100

// Estructura para representar un estudiante
typedef struct Estudiante {
    int cedula;
    char nombre[MAX_NOMBRE];
    char apellido[MAX_NOMBRE];
    char correo[MAX_CORREO];
    float nota;
    struct Estudiante* siguiente;
} Estudiante;

// Estructura para representar la lista de estudiantes
typedef struct {
    Estudiante* inicio;
    Estudiante* fin;
} ListaEstudiantes;

// Función para crear un nuevo estudiante
Estudiante* crearEstudiante(int cedula, char* nombre, char* apellido, char* correo, float nota) {
    Estudiante* estudiante = (Estudiante*)malloc(sizeof(Estudiante));
    estudiante->cedula = cedula;
    strcpy(estudiante->nombre, nombre);
    strcpy(estudiante->apellido, apellido);
    strcpy(estudiante->correo, correo);
    estudiante->nota = nota;
    estudiante->siguiente = NULL;
    return estudiante;
}

// Función para agregar un estudiante a la lista
void agregarEstudiante(ListaEstudiantes* lista, Estudiante* estudiante) {
    if (estudiante->nota >= 6) {
        // Agregar al inicio de la lista si el estudiante aprobó
        estudiante->siguiente = lista->inicio;
        lista->inicio = estudiante;
        if (lista->fin == NULL) {
            lista->fin = estudiante;
        }
    } else {
        // Agregar al final de la lista si el estudiante reprobó
        if (lista->fin == NULL) {
            lista->inicio = estudiante;
            lista->fin = estudiante;
        } else {
            lista->fin->siguiente = estudiante;
            lista->fin = estudiante;
        }
    }
}

// Función para buscar un estudiante por cédula
Estudiante* buscarEstudiante(ListaEstudiantes* lista, int cedula) {
    Estudiante* actual = lista->inicio;
    while (actual != NULL) {
        if (actual->cedula == cedula) {
            return actual;
        }
        actual = actual->siguiente;
    }
    return NULL;
}

// Función para eliminar un estudiante de la lista
void eliminarEstudiante(ListaEstudiantes* lista, int cedula) {
    if (lista->inicio == NULL) return;

    if (lista->inicio->cedula == cedula) {
        Estudiante* temp = lista->inicio;
        lista->inicio = lista->inicio->siguiente;
        if (lista->inicio == NULL) {
            lista->fin = NULL;
        }
        free(temp);
        return;
    }

    Estudiante* actual = lista->inicio;
    while (actual->siguiente != NULL) {
        if (actual->siguiente->cedula == cedula) {
            Estudiante* temp = actual->siguiente;
            actual->siguiente = actual->siguiente->siguiente;
            if (actual->siguiente == NULL) {
                lista->fin = actual;
            }
            free(temp);
            return;
        }
        actual = actual->siguiente;
    }
}

// Función para contar el total de estudiantes aprobados
int totalAprobados(ListaEstudiantes* lista) {
    int total = 0;
    Estudiante* actual = lista->inicio;
    while (actual != NULL) {
        if (actual->nota >= 6) {
            total++;
        }
        actual = actual->siguiente;
    }
    return total;
}

// Función para contar el total de estudiantes reprobados
int totalReprobados(ListaEstudiantes* lista) {
    int total = 0;
    Estudiante* actual = lista->inicio;
    while (actual != NULL) {
        if (actual->nota < 6) {
            total++;
        }
        actual = actual->siguiente;
    }
    return total;
}
// Función para imprimir la lista de estudiantes
void imprimirLista(ListaEstudiantes* lista) {
    Estudiante* actual = lista->inicio;
    while (actual != NULL) {
        printf("Cédula: %d, Nombre: %s %s, Correo: %s, Nota: %.2f\n", actual->cedula, actual->nombre, actual->apellido, actual->correo, actual->nota);
        actual = actual->siguiente;
    }
}

int main() {
    ListaEstudiantes lista;
    lista.inicio = NULL;
    lista.fin = NULL;

    int opcion;
    do {
        printf("1. Agregar estudiante\n");
        printf("2. Buscar estudiante por cédula\n");
        printf("3. Eliminar estudiante\n");
printf("4. Total de estudiantes aprobados\n");
printf("5. Total de estudiantes reprobados\n");
printf("6. Imprimir lista de estudiantes\n");
printf("7. Salir\n");
printf("Ingrese su opción: ");
scanf("%d", &opcion);

switch (opcion) {
    case 1: {
        int cedula;
        char nombre[MAX_NOMBRE];
        char apellido[MAX_NOMBRE];
        char correo[MAX_CORREO];
        float nota;

        printf("Ingrese la cédula del estudiante: ");
        scanf("%d", &cedula);
        printf("Ingrese el nombre del estudiante: ");
        scanf("%s", nombre);
        printf("Ingrese el apellido del estudiante: ");
        scanf("%s", apellido);
        printf("Ingrese el correo del estudiante: ");
        scanf("%s", correo);
        printf("Ingrese la nota del estudiante: ");
        scanf("%f", &nota);

        Estudiante* estudiante = crearEstudiante(cedula, nombre, apellido, correo, nota);
        agregarEstudiante(&lista, estudiante);
        break;
    }
    case 2: {
        int cedula;
        printf("Ingrese la cédula del estudiante a buscar: ");
        scanf("%d", &cedula);
        Estudiante* estudiante = buscarEstudiante(&lista, cedula);
        if (estudiante != NULL) {
            printf("Estudiante encontrado:\n");
            printf("Cédula: %d, Nombre: %s %s, Correo: %s, Nota: %.2f\n", estudiante->cedula, estudiante->nombre, estudiante->apellido, estudiante->correo, estudiante->nota);
        } else {
            printf("Estudiante no encontrado\n");
        }
        break;
    }
    case 3: {
        int cedula;
        printf("Ingrese la cédula del estudiante a eliminar: ");
        scanf("%d", &cedula);
        eliminarEstudiante(&lista, cedula);
        break;
    }
    case 4:
        printf("Total de estudiantes aprobados: %d\n", totalAprobados(&lista));
        break;
    case 5:
        printf("Total de estudiantes reprobados: %d\n", totalReprobados(&lista));
        break;
    case 6:
        imprimirLista(&lista);
        break;
    case 7:
        printf("Saliendo del programa...\n");
        break;
    default:
        printf("Opción inválida\n");
        break;
}
} while (opcion != 7);

return 0;
}
