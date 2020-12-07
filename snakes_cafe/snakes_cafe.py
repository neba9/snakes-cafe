print('welcome to the snakes cafe!')

greeting = """
**************************************
**    Welcome to the Snakes Cafe!   **      
**    Please see our menu below.    ** 
**
** To quit at any time, type "quit" **
**************************************
"""
print(greeting)

print(
  """
  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls
  """
)
print(
  """
  Entrees
  ----------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden
  """
)
print(
  """
  Desserts
  ----------
  Ice Cream
  Cake
  Pie
  """
)
print(
  """
  Drinks
  ----------
  Coffee
  Tea
  Unicorn Tears
  """
)


list_items = {
  'Wings': 0,
  'Cookies': 0,
  'Spring Rolls': 0,
  'Salmon': 0,
  'Steak': 0,
  'Meat Tornado': 0,
  'A Literal Garden': 0,
  'Ice Cream': 0,
  'Cake': 0,
  'Pie': 0,
  'Coffee': 0,
  'Tea': 0,
  'Unicorn Tears': 0,
}
# for item in list_items:
#   print(item)


print(
  """
  ***********************************
  ** What would you like to order? **
  ***********************************
  """
)
while (True):
 order_input = input('> ').title()
 if order_input == 'Quit':
   break

 for item in list_items:
    if order_input == item:
      list_items[item] += 1
      order_num = list_items[item]
      order_response = f"""
      **{order_num} yourquit
       order of {order_input} have been added to your meal**
      """
      print(order_response)


       
      
       
     



