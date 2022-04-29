import json


class Criterio:

    def __init__(self, categoria, descripcion):
        self._descripcion = descripcion
        self._categoria = categoria

    def __str__(self) -> None:
        return json.dump(self.__dict__)
