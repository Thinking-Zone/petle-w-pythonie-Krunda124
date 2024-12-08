import random

pada = random.choice([True, False]) 
zgadtwanie = True

while zgadywanie:
  odpowiedz = input("Czy pada? (t/n) ")
  if odpowiedz = pada:
    print("zgadłeś! brawo!") 
    zgadywanie = False 
  else:
    print("niestety nie zgadłeś")
    pada = random.choice([True, False]) 
