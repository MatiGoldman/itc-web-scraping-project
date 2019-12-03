ID_LIMITOR = 1


class City:
    """The city class is related to each of the cities
    that are being scraped from tripadvisor"""
    def __init__(self, id_c, name):
        self.id = id_c[ID_LIMITOR:]
        self.name = name
