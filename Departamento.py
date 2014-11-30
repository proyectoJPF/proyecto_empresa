__author__ = 'jpflorido'

HOLA DESARROLLADOR 1
HOLA DE NUEVO DESARROLLADOR 1
class Departamento():
    def __init__(self, nombre_depto, id_depto):
        """
        Constructor de la clase departamento

        :param nombre_depto:
        :param id_depto:
        :return:
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self, objeto_empleado):
        self.empleados.append(objeto_empleado)

    def get_salario_total(self):
        """
        Get salario total. Buena funcion

        :return: devuelve el salario total de todos los empleados
        """
        salario_total = 0
        for current_empleado in self.empleados:
            salario_total += current_empleado.get_salario()

        return salario_total


    def get_nombre_depto(self):
        return self.nombre_depto

    def get_salario_total_mensual(self):
        return 40  # Hacerlo bien
