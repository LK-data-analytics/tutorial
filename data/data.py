class Data(object):
  def __init__(self):
    """
    construct a new Data object
    :return:
    """
    self._raw_brand = self.__read_dat_files('BRAND.dat')
    self._raw_campaign = self.__read_dat_files('CAMPAIGN.dat')
    self._raw_card = self.__read_dat_files('CARD.dat')
    self._raw_category = self.__read_dat_files('CATEGORY.dat')
    self._raw_gdg = self.__read_dat_files('GDG.dat')
    self._raw_item = self.__read_dat_files('ITEM.dat')
    self._raw_subcategory = self.__read_dat_files('SUBCATEGORY.dat')
    self._raw_transaction = self.__read_dat_files('TRANSACTION.dat')
    self._raw_transaction_item = self.__read_dat_files('TRANSACTION_ITEM.dat')

  def __read_dat_files(self, filename):
    """
    reads one of the dat files that contain the data
    :param filename: the filename of the file to be read
    :return: a list of lists containing all the data by line
    """
    data = []
    with open(filename, 'r') as file:
      for line in file:
        l = line.split(",")
        data.append(map(lambda s: s.rstrip(), l))
    return data


if __name__ == '__main__':
  mydata = Data()
  print (mydata._raw_brand[0])

"""plt.hist(brand_data)
plt.show(brand_data)

brand_data.shape"""
