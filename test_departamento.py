from unittest import TestCase

from mockito import *
import os
import sys
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.Departamento import *
from src.Empleado import *


__author__ = 'jpflorido'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        """
        test del departamento

        """
        empleado_1 = mock(Empleado)
        empleado_2 = mock(Empleado)
        empleado_3 = mock(Empleado)

        when(empleado_1).get_salario().thenReturn(45000)
        when(empleado_2).get_salario().thenReturn(25000)
        when(empleado_3).get_salario().thenReturn(35000)

        depto = Departamento('Ventas', 5)
        depto.aniadir_empleado(empleado_1)
        depto.aniadir_empleado(empleado_2)
        depto.aniadir_empleado(empleado_3)

        self.assertEqual(depto.get_salario_total(), 105000)