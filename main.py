from pyscript import display 
#Restaurant Order System (Python Data Types) 

#String 
business_name = "Sophia's Bookspace "
owner_name = "Sophia S. Jimenez"

#integer 
year_since = 2025 

#Float
tax_rate = 0.08

#Boolean
bought_shipped = True 
bought_in_store = True 
is_digital = False 

#List 
product_names = ["The Two Enchanted Sisters Trilogy", "Forever in Time", "A Knitted Dream", "Camaraderie Camp", "Foiled in Tabs"]

#Tuple 
business_hours = ("8:00 AM", "6:00 PM")

#Dictionary 
menu = {
    "The Two Enchanted Sisters Trilogy": 500.00, 
    "Forever in Time": 250.00,
    "A Knitted Dream": 250.00, 
    "Camaraderie Camp": 300.00, 
    "Foiled in Tabs": 300.00,
}

#Display restaurant information 
display(business_name, target= "name1")
display(f"Author: {owner_name}", target = "owner")
display(f"Since {year_since}", target= "since")
display (f"Our Best Selling Novels ✨", target= "heading1")

#Display menu items 
display(product_names[0], target= "prod1")
display(f"P{menu['The Two Enchanted Sisters Trilogy']: .2f}", target="price1")
display(product_names[1], target= "prod2")
display(f"P{menu['Forever in Time']: .2f}", target="price2")
display(product_names[2], target= "prod3")
display(f"P{menu['A Knitted Dream']: .2f}", target="price3")
display(product_names[3], target= "prod4")
display(f"P{menu['Camaraderie Camp']: .2f}", target="price4")
display(product_names[4], target= "prod5")
display(f"P{menu['Foiled in Tabs']: .2f}", target="price5")

#Display additional information 
display(f"Open: {business_hours[0]} - {business_hours[1]}", target= "openingHours")

#Display Order Type 
display(f"Check in Available", target= "orderType")
