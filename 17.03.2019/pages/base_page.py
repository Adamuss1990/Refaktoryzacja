# -*- coding: utf-8 -*-

class BasePage():


    """
    Klasowa bazowa, z której będą korzystały wszystkie strony
    """


    def __init__(self, driver):
        self.driver = driver


    def _verify_page(self):
        return
