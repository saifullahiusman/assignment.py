Annual_salary = float(input( "Enter your annual salary:")) 
Portion_saved = float(input( "Enter the percent of your salary to save, as a decimal:" )) 
Total_cost = float(input( "Enter the cost of your dream home:" )) 
Semi_annual_raise = float(input( "The semiannualcare raise:" ))  
Portion_down_payment = 0.25 
r = 0.04
Current_saving = 0 
Month_count = 1 
Down_payment = total_cost * portion_down_payment 
while True: 
  Current_savings=current_saving+annual_salary/12*portion_saved+current_saving*r/12
if current_savings >= down_payment: 
  print("Number of months: {}" .format(month_count)) 
  "break"
if month_count % 6 == 0 :
  Annual_salary += annual_salary * semi_annual_raise  
  Month_count += 1 