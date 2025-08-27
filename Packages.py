# import e_commerce.Shipping  # For importing whole file from a package
''' from e_commerce.Shipping import shipping, products  # For specific function from a file of a package'''
from e_commerce import Shipping
# e_commerce.Shipping.shipping() # Used after importing whole file
'''shipping()  # Used after importing specific function
products()'''
Shipping.shipping()
Shipping.products()
Shipping.cost_total()