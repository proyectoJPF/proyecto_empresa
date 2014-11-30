__author__ = 'jpflorido'


class Empresa():
    def __init__(nombre_empresa, CIF, razon_social):
        """
        Constructor de la clase empresa

        :param nombre_empresa:
        :param CIF:
        :param razon_social:
        :return:
        """
        self.nombre = nombre_empresa
        self.cif = CIF
        self.razon_social = razon_social
        self.departamentos = []