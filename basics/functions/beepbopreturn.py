def sum_weights (beepweight, bopweight):
  sumweight = int(beepweight + bopweight)
  return sumweight

def calc_avg_weight(beepweight, bopweight):
  avgweight = (int(beepweight + bopweight) /2)
  return avgweight

def run():
  beepweight = int(input("What is beeps weight?"))
  print (beepweight)

  bopweight = int(input("What is bops weight?"))

  print (bopweight)

  avgorsum = input("Would you like to calculate the sum or average?")

  if avgorsum == "sum":
    print (sum_weights(beepweight, bopweight))

  elif avgorsum == "average":
    print (calc_avg_weight(beepweight, bopweight))

run()