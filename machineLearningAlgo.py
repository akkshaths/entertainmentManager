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


class machineLearn:
    def __init__(self, username, pwd):
        #where we connect to database
        
        dict1 = {
            'service': ['Netflix', 'Fubo TV', 'Time', 'Wall Street Journal', 'New York Times', 'Smithsonian', 'Food and Wine'],
            'price': [12.99, 55.00, 3.33, 19.50, 17.00, 12.00, 3.00],
            'hour': [27, 32, 5, 7, 8, 3, 2],
            'type': ['TV', 'TV', 'News', 'News', 'News', 'News', 'Magazine'],
            'category':[['Hollywood', 'Entertainment', 'General'], ['Sports', 'Entertainment'], ['Politics', 'Current Events'], ['Finance', 'Politics', 'Current Events', 'International'],
            ['Politics', 'Current Events', 'International'], ['Current Events', 'International'], ['Food', 'International']]
        }
        self.df = pd.DataFrame.from_dict(dict1)
        self.total = pd.DataFrame()
        #print(self.df)

    def errorByType(self):
        x = list(self.df['type'].unique())
        lengthOfX = len(x)
        y = []
        tempList = []
        for u in x:
            tempList.append(0)
        for i in x:
            pricePerHour = 0
            for j in range(0,len(self.df)):
                if self.df.loc[j, 'type'] == i:
                    tempList[x.index(i)] += 1
                    pricePerHour += (self.df.loc[j, 'price'] / self.df.loc[j, 'hour'])
            y.append(pricePerHour)

        plt.scatter(x, y,  color='blue')
        plt.xlabel("Type")
        plt.ylabel("Price Per Hour")
        plt.show()
        avg = sum(y)/len(y)

        lineOfFitError = 0
        for l in y:
            lineOfFitError += abs(l - avg)

        z = []


        for q in range(0, len(tempList)):
            h = max(tempList)
            z.append(x[tempList.index(h)])
            del x[tempList.index(h)]
            del tempList[tempList.index(h)]
            

        return [lineOfFitError/lengthOfX, z]


    def errorByGenre(self):
        x = ['Fashion', 'Family', 'General', 'Sports', 'Food', 'International', 'Business', 'Finance', 'Politics', 'Hollywood', 'Entertainment']
        lengthOfX = len(x)
        y = []
        tempList = [0,0,0,0,0,0,0,0,0,0,0]
        for i in x:
            pricePerHour = 0
            for j in range(0,len(self.df)):
                for l in self.df.loc[j, 'category']:
                    if l == i:
                        tempList[x.index(i)] += 1
                        pricePerHour += (self.df.loc[j, 'price'] / self.df.loc[j, 'hour'])
            y.append(pricePerHour)

        plt.scatter(x, y,  color='blue')
        plt.xlabel("Genre")
        plt.ylabel("Price Per Hour")
        plt.show()
        avg = sum(y)/len(y)

        lineOfFitError = 0
        for l in y:
            lineOfFitError += abs(l - avg)

        z = []


        for q in range(0, len(tempList)):
            h = max(tempList)
            z.append(x[tempList.index(h)])
            del x[tempList.index(h)]
            del tempList[tempList.index(h)]
            

        return [lineOfFitError/lengthOfX, z]

    def analyze(self):
        types = self.errorByType()
        genre = self.errorByGenre()

        maxList = [types[0], genre[0]]
        order = []

        if types[0] == max(maxList):
            order = ['type', 'genre']

        else:
            order = ['genre', 'type']

        unusedElement = list(self.total['service'])
        listOfRecommendations = []
        if order[0] =='type':
            for un in unusedElement:
                for o in types[1]:
                    for p in genre[1]:
                        if self.total.loc[un, 'type'] == o and self.total.loc[un, 'category'].contains(p):
                            listOfRecommendations.append(self.total.loc[un, 'service'])
                            del unusedElement[unusedElement.index(self.total.loc[un, 'service'])]
                    if self.total.loc[un, 'type'] == o:
                        listOfRecommendations.append(self.total.loc[un, 'service'])
                        del unusedElement[unusedElement.index(self.total.loc[un, 'service'])]
                    
        else:
            for un in unusedElement:
                for o in genre[1]:
                    for p in types[1]:
                        if self.total.loc[un, 'type'] == p and self.total.loc[un, 'category'].contains(o):
                            listOfRecommendations.append(self.total.loc[un, 'service'])
                            del unusedElement[unusedElement.index(self.total.loc[un, 'service'])]
                    if self.total.loc[un, 'category'].contains(o):
                        listOfRecommendations.append(self.total.loc[un, 'service'])
                        del unusedElement[unusedElement.index(self.total.loc[un, 'service'])]
                    



        return listOfRecommendations








x = machineLearn('h', 'g')
print(x.errorByType())
print(x.errorByGenre())