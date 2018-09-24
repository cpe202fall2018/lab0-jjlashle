#
# Name: Josiah Lashley
# ID: 014136534
# Date (9-24-2018)
#
# Lab 0
# Section 13/14
# Purpose of Lab (Environment, Python, and Testing!)
# Additional Comments

# Take inputed integer form user and transforms it into a float in context
def weight_on_planets():
   e_w = int(input("What do you weigh on earth? "))
   m_w = e_w * 0.38
   j_w = e_w * 2.34
   print("\nOn Mars you would weigh",m_w,"pounds.\nOn Jupiter you would weigh",j_w,"pounds.")
   # write your code here
if __name__ == '__main__':
   weight_on_planets()

