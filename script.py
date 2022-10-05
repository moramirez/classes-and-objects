class Owner:
  def __init__(self, sq_footage, gla, addy, room_count):
    self.sq_footage = sq_footage
    self.gla = gla
    self.addy = addy 
    self.room_count = room_count

  def __repr__(self):
    return "Address is {addy}, the sq footage is {sq_footage}, the gross living area is {gla}, & the room count is {room_count}".format(addy = self.addy, sq_footage = self.sq_footage, gla = self.gla, room_count = self.room_count)


class Seller:
  def __init__(self, name, addy, contract_price):
    self.name = name 
    self.addy = addy 
    self.contract_price = contract_price
  
  def __repr__(self):
    return "The Seller Name is {name} & has the Contract Price as {contract_price}".format(name = self.name, contract_price = self.contract_price)

first_sale = Owner(5000, 2500, "13 Victory St", 4)
print(first_sale)

second_sale = Seller("ez", "13 Victory St", "13333333")
print(second_sale)
