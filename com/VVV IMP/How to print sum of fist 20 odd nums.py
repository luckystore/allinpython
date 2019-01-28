def sum_odd(n):
      val = 1
      tot = 0
      while val < (2*n) - 1:
          if val % 2 != 0:
              tot = tot + val
          val = val + 1
      return tot
print(sum_odd(20))