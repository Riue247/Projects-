##Tarique Cummings
## Write your code below
##this is project is a waiter to a user but will also perform calculations and be able to take 2 customers orders 

def menu():
  menu={
    "chicken wings":6.25,
    "cheese burger":5.50,
    "pasta":4.50,
    "chicken salad":4.75,
    "french fries":3.50,
    "onion rings":4.50,
    "southern ice tea":2.50,
    "fountain drink":2.25
  }
  ##the menu that customer will be choosing from 
def total_order():
  total_order=[]
  ##the list is where the total price of the order from each customer
def tax(value):
  if payment_choice==True:
    tax=0.06
    credit_tax=tax 
    return credit_tax
def calculations():
  total_price=0
  for elements in total_order:
    total_price+=elements
  tax_value=total_price*tax(payment_choice)
  total_price+=tax_value
  return total_price

def questions(list,dictonary):
  print(menu(menu))
  payment_choice=input("are you paying cash or credit?(y/n)credit we charge tax but if you pay with cash we won't but we just expect a tip for the waiter")
  if payment_choice=='credit':
    payment_choice=True
    tax(payment_choice)
    ## takes i weather the customer is taking a payment early and inputs into the tax function and is stored and used later
  
  for i in range(1):
    main_course=input('what would you like to eat?')
    if main_course=='chicken wings':
      total_order.append(menu(menu['chicken wings']))
      print('got that')
      side==input('would you like a side with that?')
      if side=='french fries':
        menu(menu['french fries'])+total_order[i]
        print('got that also')
      elif side=='onion rings':
        menu(menu['onion rings'])+total_order[i]
        print('got that also')
    elif main_course=='cheese burger':
      total_order.append(menu(menu['cheese burger']))
      print('got that')
      side==input('would you like a side with that?')
      if side=='french fries':
        menu(menu['french fries'])+total_order[i]
        print('got that also')
      elif side=='onion rings':
        menu(menu['onion rings'])+total_order[i]
        print('got that also')
    elif main_course=='pasta':
      total_order.append(menu(menu['pasta']))
      print('got that')
      side==input('would you like a side with that?')
      if side=='french fries':
        menu(menu['french fries'])+total_order[i]
        print('got that also')
      elif side=='onion rings':
        menu(menu['onion rings'])+total_order[i]
        print('got that also')
    elif main_course=='chicken salad':
      total_order.append(menu(menu['chicken salad']))
      side==input('would you like a side with that?')
      if side=='french fries':
          menu(menu['french fries'])+total_order[i]
          print('got that also')
        elif side=='onion rings':
          menu(menu['onion rings'])+total_order[i]
          print('got that also')
    drink=input('any drink with that?(y/n)')
    if drink=='y':
      drink_option=input('what drink would you like? We have southern Ice tea or a fountain drink.')
      if drink_option=='southern ice tea':
        menu(menu['southern ice tea'])+total_order[i]
        print('got that also')
      elif drink_option=='fountain drink':
        menu(menu['fountain drink'])+total_order[i]
        print('got that also')
        ##uses a foor loop for 2 people to take 2 peoples orders and takes a main dish and stores the value in the list and than adds the side and drink to that element in the list and then calculates the tax and then calculates the total price to then be printed back to the user
  print(f'your total is {calculations(tax(payment_choice))}')
  
  


def main():
  print(questions(total_order(),menu()))
##prints everything to the user