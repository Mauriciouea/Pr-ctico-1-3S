"""
Sistema de Agenda de Turnos de Pacientes
Clínica "Salud Integral"
Desarrollado con Programación Orientada a Objetos
Estructuras de datos utilizadas: listas (vectores), diccionarios (registros)
"""

from datetime import datetime, timedelta
import os

class Paciente:
    """Clase que representa a un paciente de la clínica"""
    
    def __init__(self, cedula, nombre, apellido, edad, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.historial_turnos = []  # Lista para almacenar turnos anteriores
        
    def obtener_nombre_completo(self):
        """Retorna el nombre completo del paciente"""
        return f"{self.nombre} {self.apellido}"
    
    def agregar_turno_historial(self, turno):
        """Agrega un turno al historial del paciente"""
        self.historial_turnos.append(turno)
    
    def mostrar_informacion(self):
        """Muestra la información completa del paciente"""
        return (f"Paciente: {self.obtener_nombre_completo()}\n"
                f"Cédula: {self.cedula}\n"
                f"Edad: {self.edad} años\n"
                f"Teléfono: {self.telefono}\n"
                f"Email: {self.email}\n"
                f"Turnos atendidos: {len(self.historial_turnos)}")


class Doctor:
    """Clase que representa a un doctor de la clínica"""
    
    def __init__(self, id_doctor, nombre, apellido, especialidad, telefono):
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.telefono = telefono
        self.horarios_disponibles = []  # Lista de horarios disponibles
        
    def obtener_nombre_completo(self):
        """Retorna el nombre completo del doctor"""
        return f"Dr. {self.nombre} {self.apellido}"
    
    def agregar_horario_disponible(self, fecha_hora):
        """Agrega un horario disponible para el doctor"""
        self.horarios_disponibles.append(fecha_hora)
    
    def eliminar_horario_disponible(self, fecha_hora):
        """Elimina un horario disponible"""
        if fecha_hora in self.horarios_disponibles:
            self.horarios_disponibles.remove(fecha_hora)
    
    def mostrar_informacion(self):
        """Muestra la información completa del doctor"""
        return (f"Doctor: {self.obtener_nombre_completo()}\n"
                f"ID: {self.id_doctor}\n"
                f"Especialidad: {self.especialidad}\n"
                f"Teléfono: {self.telefono}\n"
                f"Horarios disponibles: {len(self.horarios_disponibles)}")


class Turno:
    """Clase que representa un turno médico"""
    
    ESTADOS = ["PENDIENTE", "CONFIRMADO", "CANCELADO", "ATENDIDO"]
    
    def __init__(self, id_turno, paciente, doctor, fecha_hora, motivo):
        self.id_turno = id_turno
        self.paciente = paciente
        self.doctor = doctor
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.estado = "PENDIENTE"  # Estado inicial
        self.observaciones = ""
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del turno"""
        if nuevo_estado in self.ESTADOS:
            self.estado = nuevo_estado
            return True
        return False
    
    def agregar_observacion(self, observacion):
        """Agrega observaciones al turno"""
        self.observaciones = observacion
    
    def mostrar_informacion(self):
        """Muestra la información completa del turno"""
        return (f"Turno ID: {self.id_turno}\n"
                f"Paciente: {self.paciente.obtener_nombre_completo()}\n"
                f"Doctor: {self.doctor.obtener_nombre_completo()}\n"
                f"Fecha y Hora: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}\n"
                f"Motivo: {self.motivo}\n"
                f"Estado: {self.estado}\n"
                f"Observaciones: {self.observaciones}")


class SistemaTurnosClinica:
    """Sistema principal de gestión de turnos de la clínica"""
    
    def __init__(self):
        # Estructuras de datos principales
        self.pacientes = []  # Lista de pacientes
        self.doctores = []   # Lista de doctores
        self.turnos = []     # Lista de turnos
        self.contador_turnos = 1
        self.contador_pacientes = 1
        self.contador_doctores = 1
        
        # Inicializar con datos de ejemplo
        self.inicializar_datos_ejemplo()
    
    def inicializar_datos_ejemplo(self):
        """Inicializa el sistema con datos de ejemplo"""
        # Crear doctores de ejemplo
        doctores_ejemplo = [
            ("Carlos", "Mendoza", "Cardiología", "0991234567"),
            ("Ana", "García", "Pediatría", "0992345678"),
            ("Luis", "Rodríguez", "Dermatología", "0993456789")
        ]
        
        for nombre, apellido, especialidad, telefono in doctores_ejemplo:
            doctor = Doctor(
                f"D{self.contador_doctores:03d}",
                nombre,
                apellido,
                especialidad,
                telefono
            )
            self.doctores.append(doctor)
            self.contador_doctores += 1
        
        # Crear pacientes de ejemplo
        pacientes_ejemplo = [
            ("1723456789", "María", "Pérez", 35, "0991112233", "maria@email.com"),
            ("1724567890", "Juan", "López", 42, "0992223344", "juan@email.com"),
            ("1725678901", "Carmen", "Vega", 28, "0993334455", "carmen@email.com")
        ]
        
        for cedula, nombre, apellido, edad, telefono, email in pacientes_ejemplo:
            paciente = Paciente(cedula, nombre, apellido, edad, telefono, email)
            self.pacientes.append(paciente)
            self.contador_pacientes += 1
        
        # Crear horarios disponibles para doctores
        fecha_base = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        for i in range(5):  # 5 días
            for doctor in self.doctores:
                for j in range(4):  # 4 turnos por día
                    fecha_hora = fecha_base + timedelta(days=i, hours=j*2)
                    doctor.agregar_horario_disponible(fecha_hora)
    
    # ========== MÉTODOS PARA PACIENTES ==========
    
    def registrar_paciente(self):
        """Registra un nuevo paciente en el sistema"""
        print("\n" + "="*50)
        print("REGISTRO DE NUEVO PACIENTE")
        print("="*50)
        
        try:
            cedula = input("Cédula: ")
            
            # Verificar si la cédula ya existe
            for paciente in self.pacientes:
                if paciente.cedula == cedula:
                    print("Error: Ya existe un paciente con esta cédula.")
                    return
            
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            telefono = input("Teléfono: ")
            email = input("Email: ")
            
            paciente = Paciente(cedula, nombre, apellido, edad, telefono, email)
            self.pacientes.append(paciente)
            
            print(f"\n✓ Paciente registrado exitosamente: {paciente.obtener_nombre_completo()}")
            
        except ValueError:
            print("Error: La edad debe ser un número válido.")
    
    def buscar_paciente_por_cedula(self, cedula):
        """Busca un paciente por cédula"""
        for paciente in self.pacientes:
            if paciente.cedula == cedula:
                return paciente
        return None
    
    def listar_pacientes(self):
        """Lista todos los pacientes registrados"""
        print("\n" + "="*50)
        print("LISTADO DE PACIENTES")
        print("="*50)
        
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        
        for i, paciente in enumerate(self.pacientes, 1):
            print(f"{i}. {paciente.obtener_nombre_completo()} - Cédula: {paciente.cedula}")
    
    # ========== MÉTODOS PARA TURNOS ==========
    
    def agendar_turno(self):
        """Agenda un nuevo turno"""
        print("\n" + "="*50)
        print("AGENDAR NUEVO TURNO")
        print("="*50)
        
        # Verificar que haya pacientes y doctores
        if not self.pacientes:
            print("Error: No hay pacientes registrados.")
            return
        
        if not self.doctores:
            print("Error: No hay doctores disponibles.")
            return
        
        # Buscar paciente
        cedula = input("Cédula del paciente: ")
        paciente = self.buscar_paciente_por_cedula(cedula)
        
        if not paciente:
            print("Error: Paciente no encontrado.")
            return
        
        # Listar doctores
        print("\nDoctores disponibles:")
        for i, doctor in enumerate(self.doctores, 1):
            print(f"{i}. {doctor.obtener_nombre_completo()} - {doctor.especialidad}")
        
        try:
            opcion_doctor = int(input("\nSeleccione el doctor (número): ")) - 1
            
            if opcion_doctor < 0 or opcion_doctor >= len(self.doctores):
                print("Error: Selección inválida.")
                return
            
            doctor = self.doctores[opcion_doctor]
            
            # Mostrar horarios disponibles del doctor
            print(f"\nHorarios disponibles del {doctor.obtener_nombre_completo()}:")
            
            if not doctor.horarios_disponibles:
                print("No hay horarios disponibles para este doctor.")
                return
            
            horarios_disponibles = []
            for i, fecha_hora in enumerate(doctor.horarios_disponibles, 1):
                print(f"{i}. {fecha_hora.strftime('%d/%m/%Y %H:%M')}")
                horarios_disponibles.append(fecha_hora)
            
            opcion_horario = int(input("\nSeleccione el horario (número): ")) - 1
            
            if opcion_horario < 0 or opcion_horario >= len(horarios_disponibles):
                print("Error: Selección inválida.")
                return
            
            fecha_hora_seleccionada = horarios_disponibles[opcion_horario]
            motivo = input("Motivo de la consulta: ")
            
            # Crear el turno
            turno = Turno(
                f"T{self.contador_turnos:04d}",
                paciente,
                doctor,
                fecha_hora_seleccionada,
                motivo
            )
            
            self.turnos.append(turno)
            paciente.agregar_turno_historial(turno)
            doctor.eliminar_horario_disponible(fecha_hora_seleccionada)
            self.contador_turnos += 1
            
            print(f"\n✓ Turno agendado exitosamente")
            print(f"ID del Turno: {turno.id_turno}")
            print(f"Paciente: {paciente.obtener_nombre_completo()}")
            print(f"Doctor: {doctor.obtener_nombre_completo()}")
            print(f"Fecha: {fecha_hora_seleccionada.strftime('%d/%m/%Y %H:%M')}")
            
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    def listar_turnos(self, filtro_estado=None):
        """Lista todos los turnos, opcionalmente filtrados por estado"""
        print("\n" + "="*50)
        
        if filtro_estado:
            print(f"TURNOS - ESTADO: {filtro_estado}")
        else:
            print("LISTADO DE TODOS LOS TURNOS")
        
        print("="*50)
        
        turnos_filtrados = []
        for turno in self.turnos:
            if not filtro_estado or turno.estado == filtro_estado:
                turnos_filtrados.append(turno)
        
        if not turnos_filtrados:
            print("No hay turnos registrados.")
            return
        
        for i, turno in enumerate(turnos_filtrados, 1):
            print(f"{i}. Turno {turno.id_turno}: {turno.paciente.obtener_nombre_completo()} "
                  f"con {turno.doctor.obtener_nombre_completo()} "
                  f"({turno.fecha_hora.strftime('%d/%m/%Y %H:%M')}) - Estado: {turno.estado}")
    
    def buscar_turno_por_id(self, id_turno):
        """Busca un turno por su ID"""
        for turno in self.turnos:
            if turno.id_turno == id_turno:
                return turno
        return None
    
    def cambiar_estado_turno(self):
        """Cambia el estado de un turno"""
        print("\n" + "="*50)
        print("CAMBIAR ESTADO DE TURNO")
        print("="*50)
        
        id_turno = input("ID del turno: ")
        turno = self.buscar_turno_por_id(id_turno)
        
        if not turno:
            print("Error: Turno no encontrado.")
            return
        
        print(f"\nTurno actual: {turno.mostrar_informacion()}")
        print(f"\nEstados disponibles: {', '.join(Turno.ESTADOS)}")
        
        nuevo_estado = input("Nuevo estado: ").upper()
        
        if turno.cambiar_estado(nuevo_estado):
            print(f"\n✓ Estado cambiado a: {nuevo_estado}")
            
            if nuevo_estado == "ATENDIDO":
                observacion = input("Ingrese observaciones de la consulta: ")
                turno.agregar_observacion(observacion)
        else:
            print("Error: Estado no válido.")
    
    # ========== MÉTODOS DE CONSULTA Y REPORTERÍA ==========
    
    def consultar_turnos_por_paciente(self):
        """Consulta todos los turnos de un paciente"""
        print("\n" + "="*50)
        print("CONSULTA DE TURNOS POR PACIENTE")
        print("="*50)
        
        cedula = input("Cédula del paciente: ")
        paciente = self.buscar_paciente_por_cedula(cedula)
        
        if not paciente:
            print("Error: Paciente no encontrado.")
            return
        
        print(f"\nTurnos del paciente: {paciente.obtener_nombre_completo()}")
        print("-" * 40)
        
        turnos_paciente = [t for t in self.turnos if t.paciente.cedula == cedula]
        
        if not turnos_paciente:
            print("El paciente no tiene turnos registrados.")
            return
        
        for i, turno in enumerate(turnos_paciente, 1):
            print(f"\nTurno {i}:")
            print(f"  ID: {turno.id_turno}")
            print(f"  Doctor: {turno.doctor.obtener_nombre_completo()}")
            print(f"  Fecha: {turno.fecha_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"  Estado: {turno.estado}")
            print(f"  Motivo: {turno.motivo}")
    
    def consultar_turnos_por_doctor(self):
        """Consulta todos los turnos de un doctor"""
        print("\n" + "="*50)
        print("CONSULTA DE TURNOS POR DOCTOR")
        print("="*50)
        
        # Listar doctores
        for i, doctor in enumerate(self.doctores, 1):
            print(f"{i}. {doctor.obtener_nombre_completo()}")
        
        try:
            opcion = int(input("\nSeleccione el doctor (número): ")) - 1
            
            if opcion < 0 or opcion >= len(self.doctores):
                print("Error: Selección inválida.")
                return
            
            doctor = self.doctores[opcion]
            print(f"\nTurnos del {doctor.obtener_nombre_completo()}")
            print("-" * 40)
            
            turnos_doctor = [t for t in self.turnos if t.doctor.id_doctor == doctor.id_doctor]
            
            if not turnos_doctor:
                print("El doctor no tiene turnos asignados.")
                return
            
            for i, turno in enumerate(turnos_doctor, 1):
                print(f"\nTurno {i}:")
                print(f"  ID: {turno.id_turno}")
                print(f"  Paciente: {turno.paciente.obtener_nombre_completo()}")
                print(f"  Fecha: {turno.fecha_hora.strftime('%d/%m/%Y %H:%M')}")
                print(f"  Estado: {turno.estado}")
                print(f"  Motivo: {turno.motivo}")
        
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    def generar_estadisticas(self):
        """Genera estadísticas del sistema"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("="*50)
        
        print(f"\n📊 RESUMEN GENERAL:")
        print(f"  • Pacientes registrados: {len(self.pacientes)}")
        print(f"  • Doctores registrados: {len(self.doctores)}")
        print(f"  • Turnos totales: {len(self.turnos)}")
        
        if self.turnos:
            print(f"\n📈 ESTADÍSTICAS DE TURNOS:")
            
            # Contar por estado
            estados = {}
            for turno in self.turnos:
                estados[turno.estado] = estados.get(turno.estado, 0) + 1
            
            for estado, cantidad in estados.items():
                print(f"  • {estado}: {cantidad} ({cantidad/len(self.turnos)*100:.1f}%)")
            
            # Turnos por doctor
            print(f"\n👨‍⚕️ TURNOS POR DOCTOR:")
            for doctor in self.doctores:
                turnos_doctor = len([t for t in self.turnos if t.doctor.id_doctor == doctor.id_doctor])
                print(f"  • {doctor.obtener_nombre_completo()}: {turnos_doctor} turnos")
    
    # ========== MÉTODO PRINCIPAL DE EJECUCIÓN ==========
    
    def ejecutar(self):
        """Método principal que ejecuta el sistema"""
        while True:
            self.mostrar_menu_principal()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.registrar_paciente()
            elif opcion == "2":
                self.listar_pacientes()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.listar_turnos()
            elif opcion == "5":
                self.listar_turnos("PENDIENTE")
            elif opcion == "6":
                self.cambiar_estado_turno()
            elif opcion == "7":
                self.consultar_turnos_por_paciente()
            elif opcion == "8":
                self.consultar_turnos_por_doctor()
            elif opcion == "9":
                self.generar_estadisticas()
            elif opcion == "10":
                print("\n¡Gracias por usar el Sistema de Turnos de la Clínica!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
            
            input("\nPresione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print(" SISTEMA DE GESTIÓN DE TURNOS - CLÍNICA 'SALUD INTEGRAL' ")
        print("="*50)
        print("\n📋 MENÚ PRINCIPAL")
        print("-" * 30)
        print("1. Registrar nuevo paciente")
        print("2. Listar pacientes")
        print("3. Agendar nuevo turno")
        print("4. Listar todos los turnos")
        print("5. Listar turnos pendientes")
        print("6. Cambiar estado de turno")
        print("7. Consultar turnos por paciente")
        print("8. Consultar turnos por doctor")
        print("9. Ver estadísticas del sistema")
        print("10. Salir")
        print("-" * 30)


# ========== EJECUCIÓN DEL PROGRAMA ==========
if __name__ == "__main__":
    print("="*60)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE TURNOS")
    print("Clínica 'Salud Integral'")
    print("="*60)
    print("\nEste sistema utiliza Programación Orientada a Objetos y")
    print("estructuras de datos como listas, diccionarios y registros.")
    
    sistema = SistemaTurnosClinica()
    sistema.ejecutar()