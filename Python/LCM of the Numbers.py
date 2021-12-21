def findlcm(x,y):
      if x > y:
            greaterno  = x
      else:
            greaterno = y

      while True:
            if((greaterno % x == 0) and (greaterno % y == 0)):
                  lcm = greaterno
                  break
            greaterno += 1
      return lcm

print(findlcm(5,3))

