ID_LIMITOR = 1


class City:

    def __init__(self, id_c, name):
        self.id = id_c[ID_LIMITOR:]
        self.name = name
