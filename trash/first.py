# wages.py
# Computes the taxes and wages for an employee given the
# number of hours worked and their pay rate.

# Set tax rates as constants.
STATE_TAX_RATE = 0.035
FED_TAX_RATE = 0.15

# Extract data from the user.
employee = raw_input( "Employee name: " )
hours = float( raw_input( "Hours worked: " ) )
payRate = float( raw_input( "Pay rate: " ) )

# Compute the employee's taxes and wages.
wages = hours * payRate
stateTaxes = wages * STATE_TAX_RATE
fedTaxes = wages * FED_TAX_RATE
takeHome = wages - stateTaxes - fedTaxes

# Print the results.
print "PAY REPORT"
print "Employee: ", employee
print "----------------------------------"
print "Wages:       ", wages
print "State Taxes: ", stateTaxes
print "Fed Taxes:   ", fedTaxes
print "Pay:         ", takeHome