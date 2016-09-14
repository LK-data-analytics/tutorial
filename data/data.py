import numpy as np
from matplotlib import pyplot as plt

class Data(object):
    def __init__(self):
        self.brand = np.fromfile('BRAND.dat', sep = ',')
        self.campaign = np.fromfile('CAMPAIGN.dat')
        self.card = np.fromfile('CARD.dat')
        self.category = np.fromfile('CATEGORY.dat')
        self.gdg = np.fromfile('GDG.dat')
        self.item = np.fromfile('ITEM.dat')
        self.subcategory = np.fromfile('SUBCATEGORY.dat')
        self.transaction = np.fromfile('TRANSACTION.dat')
        self.transaction_item = np.fromfile('TRANSACTION_ITEM.dat')


if __name__ == '__main__':
    mydata = Data()
    print (mydata.brand)




"""plt.hist(brand_data)
plt.show(brand_data)

brand_data.shape"""

