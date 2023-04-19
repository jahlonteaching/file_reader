from abc import ABC, abstractmethod

from reader import Lector, LectorArchivo


class Filtro(Lector, ABC):
    def __init__(self, lector_base, id):
        self.lector_base = lector_base
        self.id = id

    def leer(self):
        c = self.lector_base.leer()
        return self.filtrar(c)

    def cerrar(self):
        self.lector_base.cerrar()

    @abstractmethod
    def filtrar(self, c):
        pass


class FiltroMayAMin(Filtro):
    def __init__(self, lector):
        super().__init__(lector, 'm')

    def filtrar(self, c):
        if c.isupper():
            c = c.lower()
        return c


class FiltroEspacioAGuion(Filtro):
    def __init__(self, lector):
        super().__init__(lector, 'e')

    def filtrar(self, c):
        if c == ' ':
            c = '_'
        return c


class FiltroParentesisACorchetes(Filtro):
    def __init__(self, lector):
        super().__init__(lector, 'p')

    def filtrar(self, c):
        if c == '(':
            c = '['
        if c == ')':
            c = ']'
        return c


class ManejadorLectores:
    def __init__(self, file_path):
        self.lector = LectorArchivo(file_path)
        self.mapa_filtro = {
            'm': FiltroMayAMin,
            'e': FiltroEspacioAGuion,
            'p': FiltroParentesisACorchetes
        }

    def crear_lector(self, filtros=''):
        for c in filtros:
            self.lector = self.mapa_filtro[c](self.lector)
        return self.lector

    def registrar_filtro(self, clase_filtro, id):
        self.mapa_filtro[id] = clase_filtro


class CreadorLectorConOpciones:
    def __init__(self, file_path):
        self.lector = LectorArchivo(file_path)
        self.mapa_filtro = {
            'm' : 'crear_filtro_may_a_min',
            'e' : 'crear_filtro_espacio_a_guion',
            'p' : 'crear_filtro_parentesis_a_corchete'
        }

    def crear_lector(self, filtros=''):
        for c in filtros:
            getattr(self, self.mapa_filtro[c])()
        return self.lector

    def crear_filtro_may_a_min(self):
        self.lector = FiltroMayAMin(self.lector)

    def crear_filtro_espacio_a_guion(self):
        self.lector = FiltroEspacioAGuion(self.lector)

    def crear_filtro_parentesis_a_corchete(self):
        self.lector = FiltroParentesisACorchetes(self.lector)


class CreadorLector:

    def __init__(self, file_path):
        self.lector = LectorArchivo(file_path)

    def crear_lector(self) -> Lector:
        return self.lector

    def con_filtro_may_a_min(self):
        self.lector = FiltroMayAMin(self.lector)
        return self

    def con_filtro_espacio_a_guion(self):
        self.lector = FiltroEspacioAGuion(self.lector)
        return self

    def con_filtro_parentesis_a_corchetes(self):
        self.lector = FiltroParentesisACorchetes(self.lector)
        return self

    def con_filtro_personalizado(self, filtro_class):
        self.lector = filtro_class(self.lector)
        return self
