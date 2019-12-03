ID_LIMITOR = 1


class City:
    """The city class is related to each of the cities
    that are being scraped from tripadvisor"""

    def __init__(self, id_c, name):
        """

        :param id_c (int): id of city
        :param name (string): name of city
        """
        self.id = id_c[ID_LIMITOR:]
        self.name = ''.join([i for i in name if i.isalpha() or i == ' ']).strip()
