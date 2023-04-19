from filtros import Filtro


class FiltroExclamacionAInterrogacion(Filtro):
    def __init__(self, lector_base):
        super().__init__(lector_base, 'x')

    def filtrar(self, c):
        if c == '!':
            c = '?'
        if c == '¡':
            c = '¿'
        return c
