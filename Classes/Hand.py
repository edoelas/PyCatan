from Classes.Materials import Materials

from typing import List

class Hand:
    """
    Clase que representa la mano de los jugadores
    """

    def __init__(self):
        self.resources = Materials(0,0,0,0,0)

    def set_material(self, new_resources: Materials):
        """
        Establece los materiales de la mano a los que se le pasan.
        :param new_resources: (Materials) materiales a establecer.
        :return: None
        """
        self.resources = new_resources
    
    def update_material(self, resource_id, amount):
        """
        Suma amount al material seleccionado (si es negativo resta).
        :param resource: (int) tipo de recurso a actualizar.
        :param amount: (int) cantidad del recurso a actualizar.
        :return: None
        """
        if self.resources.get_from_id(resource_id) + amount < 0:
            return
        self.resources = self.resources.add_from_id(resource_id, amount)
    
    def update_material_list(self, resource_ids, amount):
        """
        Suma amount a los materiales seleccionados (si es negativo resta).
        :param resource: (list) tipo de recursos a actualizar.
        :param amount: (int) cantidad del recurso a actualizar.
        :return: None
        """
        for resource in resource_ids:
            self.update_material(resource, amount)

    def get_from_id(self, material_id):
        return self.resources.get_from_id(material_id)

    def get_total(self):
        return sum(self.resources)

    def __str__(self):
        return f'Hand: {str(self.resources)}' 