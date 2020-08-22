import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

class Entertainment:
    def __init__(self, price, hours, categories):
        self.price = price
        self.hours = hours
        self.categories = categories
        
    def getGlobe(self, cat):
        if cat in self.categories:
            return True
        return False

