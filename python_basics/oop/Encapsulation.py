class Computer:

  def __init__(self):
    self.__maxprice = 900

  def sell(self):
    print("Selling Price: {}".format(self.__maxprice))

  def setMaxPrice(self, price):
    self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''
In the above program, we defined a Computer class.
We used __init__() method to store the maximum selling price of Computer. 
We tried to modify the price.
However, we can't change it because Python treats the __maxprice as private attributes.
As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.
'''