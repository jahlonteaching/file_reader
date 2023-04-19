from abc import ABC, abstractmethod


class Lector(ABC):
    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def cerrar(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()


class LectorArchivo(Lector):
    def __init__(self, file_path):
        self.file = open(file_path, mode='r', encoding='utf8')

    def leer(self):
        return self.file.read(1)

    def cerrar(self):
        self.file.close()
