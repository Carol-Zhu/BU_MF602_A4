# author: Xujiahui Zhu
# 2023/06/29
# A4-task1

import numpy as np

# function 1
""" Write the function cashflow_times(n, m) to develop the list of the times
    at which a bond makes coupon payments, with n years and m coupon payments per year.
"""
def cashflow_times(n, m):
  return [x + 1 for x in range(n * m)]

# function 2
""" Write the function discount_factors(r, n, m)
    to calculate and return a list of discount factors
    for a given annualized interest rate r, for n years, and m discounting periods per year.
"""
def discount_factors(r, n, m):
  return [1 / (1 + r/m) ** t for t in cashflow_times(n, m)]


# function 3
""" Write the function bond_cashflows(fv, c, n, m) to calculate and
    return a list of cashflows for a bond specified by the parameters.
    The parameters are: fv is the future (maturity) value of the bond;

    c is the annual coupon rate expressed as percentage per year;

    n is the number of years until maturity;

    m is the number of coupon payments per year.
"""
def bond_cashflows(fv, c, n, m):
  coupon = c * fv / m
  bond_cf = [coupon for t in cashflow_times(n, m)]
  bond_cf[-1] = bond_cf[-1] + fv
  return bond_cf

# function 4
""" Write the function bond_price(fv, c, n, m, r) to calculate and return the price of a bond.
    The parameters are: fv is the future (maturity) value of the bond;

    c is the annual coupon rate expressed as percentage per year;

    n is the number of years until maturity;

    m is the number of coupon payments per year;

    and r, the annualized yield to maturity of the bond

"""
def bond_price(fv, c, n, m, r):
  price_list = [bond_cashflows(fv, c, n, m)[x] * discount_factors(r, n, m)[x] for x in range(n * m)]
  price = sum(price_list)
  return price


# function 5
""" Write the function bond_yield_to_maturity(fv, c, n, m, price):
    to calculate the annualized yield_to_maturity on a bond.
    The parameters are: fv is the future (maturity) value of the bond;

    c is the annual coupon rate expressed as percentage per year;

    n is the number of years until maturity;

    m is the number of coupon payments per year;

    and price is the current market price of the bond
"""
def bond_yield_to_maturity(fv, c, n, m, price):
  ACCURACY = 0.0001
  abs_diff = 1

  a = 0.0
  b = 1.0
  middle = 0.5

  count = 0

  while abs_diff > ACCURACY:
    diff = bond_price(fv, c, n, m, middle) - price

    if diff < 0:
      b = middle
      middle = (a + b) / 2

      test_price = bond_price(fv, c, n, m, middle)
      diff = test_price - price
      abs_diff = abs(diff)

    else:
      a = middle
      middle = (a + b) / 2

      test_price = bond_price(fv, c, n, m, middle)
      diff = test_price - price
      abs_diff = abs(diff)

    # print("Iteration =",count, "test_rate =", middle, "price =", test_price, "diff =", diff )
    count += 1

  bond_yield = middle

  return bond_yield



if __name__ == '__main__':
  # test functions 
  print("[x + 1 for x in range(2 * 3)] returned", [x + 1 for x in range(2 * 3)])
  print("discount_factors(0.05, 2, 12) returned", discount_factors(0.05, 2, 12))
  print("bond_cashflows(10000, 0.0575, 2, 2) returned", bond_cashflows(10000, 0.0575, 2, 2))
  print("bond_price(100, 0.04, 3, 2, 0.05) returned", bond_price(100, 0.04, 3, 2, 0.05))
  print("bond_yield_to_maturity(100, 0.04, 3, 2, 101.75) returned", bond_yield_to_maturity(100, 0.04, 3, 2, 101.75))


