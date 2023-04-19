from filtros import CreadorLector, ManejadorLectores
from filtros_adicionales import FiltroExclamacionAInterrogacion
from filtros_decoradores import espacio_a_guion, mayuscula_a_minuscula, parentesis_a_corchetes
from reader import Lector


if __name__ == "__main__":

    # creador = CreadorLector("test.txt")
    manejador = ManejadorLectores("test.txt")
    manejador.registrar_filtro(FiltroExclamacionAInterrogacion, 'x')
    # lector: Lector = creador.con_filtro_parentesis_a_corchetes().crear_lector()
    lector = manejador.crear_lector()

    @parentesis_a_corchetes
    @mayuscula_a_minuscula
    def leer(lec) -> int:
        return lec.leer()

    with lector as le:
        c = leer(le)
        while c != '':
            print(c, end='')
            c = leer(le)
