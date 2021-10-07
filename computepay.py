# A program than calculates your salary related to the hours you work.

# The hours you work per week
h = float(input("Enter hours of work per week: "))
print()

# The amount you receive of money per hours of work
r = float(input("Enter rate per hour: "))
print()

def computepay():
  """ Returns the gross payment according the amount of hours of work """
  gross_pay = h * r
  
  # If you work extra hours:
  # For example if you work 9 hours and you receive and extra pay for more than 7 hours of work, you gain an extra rate for 2 hours
  extra_h = float(input("Enter how many hours you need for an extra payment: "))
  print()
  
  # Calculate the extra hours worked
  extra_h_worked = h - extra_h  
  
  extra_r = float(input("Enter how much do you gain for an extra hour: "))
  print()
  
  # Calculate the extra gross pay extra:
  gross_pay_extra = (extra_h_worked * extra_r) + ((h - extra_h_worked) * r)
  
  if h > extra_h:
    print(f"Your gross pay with extra hours per week it's of ${gross_pay_extra}")
  else:
    print(f"Your gross pay per week it's of ${gross_pay}")  

computepay()

