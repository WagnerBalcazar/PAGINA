class Persona:
    def __init__(self, nombre_completo):
        nombres = nombre_completo.split()
        self.nombre = nombres[0] if nombres else ""
        self.apellido = " ".join(nombres[1:]) if len(nombres) > 1 else ""

class Jugador(Persona):
    def __init__(self, nombre_completo):
        super().__init__(nombre_completo)

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class Inscripcion:
    def __init__(self, equipo, campeonato, jugadores):
        self.equipo = equipo
        self.campeonato = campeonato
        self.jugadores = jugadores

class Campeonato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.encuentros = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def agregar_encuentro(self, encuentro):
        self.encuentros.append(encuentro)

class EncuentroDeportivo:
    VICTORIA_LOCAL = "Victoria Local"
    VICTORIA_VISITANTE = "Victoria Visitante"
    EMPATE = "Empate"

    def __init__(self, equipoLocal, equipoVisitante, fecha, golesLocal, golesVisitante):
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.fecha = fecha
        self.golesLocal = golesLocal
        self.golesVisitante = golesVisitante

    def get_resultado(self):
        if self.golesLocal > self.golesVisitante:
            return self.VICTORIA_LOCAL
        elif self.golesLocal < self.golesVisitante:
            return self.VICTORIA_VISITANTE
        else:
            return self.EMPATE

class TablaPosiciones:
    def __init__(self):
        self.posiciones = {}

    def actualizar_tabla(self, encuentros):
        for encuentro in encuentros:
            if encuentro.equipoLocal.nombre not in self.posiciones:
                self.posiciones[encuentro.equipoLocal.nombre] = 0
            if encuentro.equipoVisitante.nombre not in self.posiciones:
                self.posiciones[encuentro.equipoVisitante.nombre] = 0

            resultado = encuentro.get_resultado()
            if resultado == EncuentroDeportivo.VICTORIA_LOCAL:
                self.posiciones[encuentro.equipoLocal.nombre] += 3
            elif resultado == EncuentroDeportivo.VICTORIA_VISITANTE:
                self.posiciones[encuentro.equipoVisitante.nombre] += 3
            elif resultado == EncuentroDeportivo.EMPATE:
                self.posiciones[encuentro.equipoLocal.nombre] += 1
                self.posiciones[encuentro.equipoVisitante.nombre] += 1

        # Ordenar la tabla por puntos en orden descendente
        self.posiciones = dict(sorted(self.posiciones.items(), key=lambda item: item[1], reverse=True))

def ingresar_datos():
    equipos = {}
    campeonatos = {}

    # Ingresar equipos y jugadores
    num_equipos = int(input("Ingrese el número de equipos: "))
    for _ in range(num_equipos):
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        equipo = Equipo(nombre_equipo)

        num_jugadores = int(input(f"Ingrese el número de jugadores para {nombre_equipo}: "))
        for _ in range(num_jugadores):
            nombre_completo = input("Ingrese el nombre y apellido del jugador: ")
            jugador = Jugador(nombre_completo)
            equipo.agregar_jugador(jugador)

        equipos[nombre_equipo] = equipo

    # Ingresar campeonatos
    num_campeonatos = int(input("Ingrese el número de campeonatos: "))
    for _ in range(num_campeonatos):
        nombre_campeonato = input("Ingrese el nombre del campeonato: ")
        campeonato = Campeonato(nombre_campeonato)

        num_equipos_campeonato = int(input(f"Ingrese el número de equipos para {nombre_campeonato}: "))
        for _ in range(num_equipos_campeonato):
            nombre_equipo = input("Ingrese el nombre del equipo: ")
            campeonato.agregar_equipo(equipos[nombre_equipo])

        campeonatos[nombre_campeonato] = campeonato

    # Ingresar encuentros deportivos
    for nombre_campeonato, campeonato in campeonatos.items():
        num_encuentros = int(input(f"Ingrese el número de encuentros para {nombre_campeonato}: "))
        for _ in range(num_encuentros):
            nombre_equipo_local = input("Ingrese el nombre del equipo local: ")
            nombre_equipo_visitante = input("Ingrese el nombre del equipo visitante: ")
            fecha_encuentro = input("Ingrese la fecha del encuentro (YYYY-MM-DD): ")
            goles_local = int(input(f"Ingrese los goles de {nombre_equipo_local}: "))
            goles_visitante = int(input(f"Ingrese los goles de {nombre_equipo_visitante}: "))
            encuentro = EncuentroDeportivo(equipos[nombre_equipo_local], equipos[nombre_equipo_visitante], fecha_encuentro, goles_local, goles_visitante)
            campeonato.agregar_encuentro(encuentro)

    return campeonatos

def main():
    # Mensaje de bienvenida
    print("¡Bienvenido al Campeonato Loja!")

    # Ingresar datos
    campeonatos = ingresar_datos()

    # Procesar y mostrar la tabla de posiciones
    for nombre_campeonato, campeonato in campeonatos.items():
        tabla_posiciones = TablaPosiciones()
        tabla_posiciones.actualizar_tabla(campeonato.encuentros)

        print(f"\nTabla de Posiciones de {nombre_campeonato}:")
        for equipo, puntos in tabla_posiciones.posiciones.items():
            print(f"{equipo}: {puntos} puntos")

if __name__ == "__main__":
    main()
