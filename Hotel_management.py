#creating the class hotel
class hotel:
  def __init__(self):
    self.Break_fast_menu = hotel
#Created function to show the menus
  def show(self):
    print('**********************************************************************\tMENU\t**********************************************************************')
    print("                            \nIdly - Rs 15\t\t\tPoori - Rs 20\t\t\tDosa - Rs 30\t\t\tPongal - Rs 25\t\t\tVadai - Rs 10\n")
#creating the class customer
class customer:
  def request_order(self):
    Total_items=[]
    idly=[]
    poori=[]
    dosa=[]
    pongal=[]
    vadai=[]
    while True:
      print("1 - Idly \n2 - Poori \n3 - Dosa\n4 - Pongal\n5 - Vadai\n0 - Done")
      #creating options for the menus
      option=int(input("Choose the item:"))
      if option ==1:
        idly_no=int(input("You have choosen Idly. Please enter the quantity:"))
        idly.append(idly_no)
        if len(idly) == 0:
          Total_items.append(0)
        else:
          Total_items.append(15*idly_no)
      elif option ==2:
        poori_no=int(input("You have choosen Poori. Please enter the quantity:"))
        poori.append(poori_no)
        if len(poori) == 0:
          Total_items.append(0)
        else:
          Total_items.append(20*poori_no)
      elif option ==3:
        dosa_no=int(input("You have choosen Dosa. Please enter the quantity:"))
        dosa.append(dosa_no)
        if len(dosa) == 0:
          Total_items.append(0)
        else:
          Total_items.append(30*dosa_no)
      elif option ==4:
        pongal_no=int(input("You have choosen Pongal. Please enter the quantity:"))
        pongal.append(pongal_no)
        if len(pongal) == 0:
          Total_items.append(0)
        else:
          Total_items.append(25*pongal_no)
      elif option ==5:
        vadai_no=int(input("You have choosen Vadai. Please enter the quantity:"))
        vadai.append(vadai_no)
        if len(vadai) == 0:
          Total_items.append(0)
        else:
          Total_items.append(10*vadai_no)
      elif option==0:
          print("\n***************************************************************************")
          print("ITEM NAME\t\t  QUANTITY \t\t          PRICE")
          print("***************************************************************************")
          if len(idly)!=0:
            print(" Idly:   \t\t     ",idly[0],"  \t\t\t  ",15*idly[0])
          if len(poori)!=0:
            print(" Poori:  \t\t     ",poori[0]," \t\t\t  ",20*poori[0])
          if len(dosa)!=0:
            print(" Dosa:   \t\t     ",dosa[0],"  \t\t\t  ",30*dosa[0])
          if len(pongal)!=0:
            print(" Pongal: \t\t     ",pongal[0],"\t\t\t  ",25*pongal[0])
          if len(vadai)!=0:
            print(" Vadai:  \t\t     ",vadai[0]," \t\t\t  ",10*vadai[0])
          print("***************************************************************************")
          print(" Total:  \t\t\t\t\t\t  ",sum(Total_items))
          print("***************************************************************************\n")
          print("You have successfully placed your order.\n")
          break
    return Total_items
class Bill_counter:
  def Cutomer_billing(self,Order_details):
    self.order_details=Order_details
    print("\nYour order total:",sum(self.order_details),"\n")

#created object "pondy_star" for class "hotel"

pondy_star = hotel()

#created object "pandiyarajan" for class "customer"

pandiyarajan = customer()

#created object "Billing" for class "Bill_counter"

Billing = Bill_counter()

#printing text to welcome the customers

print("*******************************************************************************************************************************************************")
print("*                                                 Welcome to PONDY STAR. We are here to serve you. Enjoy your Food.                                   *")
print("*******************************************************************************************************************************************************")
while True:
  print('-------------------')
  print("Choose your option:")
  print("1 - Show the Menu \n2 - Place the order \n3 - Pay Bill\n0 - Exit")
  print('-------------------')
  option = int(input("Enter your option here:"))
  if option == 1:
    pondy_star.show()
  elif option == 2:
    Give_order = pandiyarajan.request_order()
  elif option == 3:
    Bill=Billing.Cutomer_billing(Give_order)
  elif option == 0:
    print("******************************************************************Thank you visit again.***********************************************************")
    break
