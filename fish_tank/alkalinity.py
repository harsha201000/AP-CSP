def monitor():
  try:
    val1 = 7 # Range should start at 7
    val2 = 12
    alkilines = list(range(val1, val2+1))
    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < alkilines[0]):
      mesg = "Alkalinity too low!"
    elif (current > alkilines[-1]): # Use -1 for the last item
      mesg = "Alkalinity too high!"
  except:
    mesg = "Alkalinity Error!" # Don't hide the error
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  # return 5 # too low
  # return 15 # too high
  return 9 # OK