__author__ = 'jpflorido'
HOLA DESARROLLADOR 2
HOLA DE NUEVO DESARROLLADOR 2

class Empleado():
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Constructor clase empleado

        :param nombre:
        :param apellidos:
        :param dni:
        :param direccion:
        :param edad:
        :param email:
        :param salario:
        :return:
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.dni = dni
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Get salario del empleado
        :return: salario del empleado
        """
        return self.salario

    def get_dni(self):
        return self.dni

    def get_nombre_appellidos(self, dni):
        return self.nombre + self.apellidos

    def get_edad(self):
        return self.edad

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.direccion

    def get_salario_mensual(self):
        return self.salario / float(12)
        # Podriamos definir mas funciones relacionadas con los atributos
