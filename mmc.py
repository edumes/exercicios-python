print("copie e cole este padrão e digite os numeros desejados e coloque virgulas entre eles mmc([ ])")
def mmc(nums):
      max_ = max(nums)
      i = 1
      while True:
            mult = max_ * i
            if all(mult%nr == 0 for nr in nums):
                  return mult
            i += 1


            
