def monitor():
  try:
    temps = [50, 55, 60, 65, 70, 75]
    temp_readings = get_temps()
    num_readings = len(temp_readings) # Count the actual readings
   
    ave_temp = sum(temp_readings) / num_readings
    mesg = "Temperature OK"
    
    if (ave_temp < temps[0]):
      mesg = "Average temperature too cold!"
    elif (ave_temp > temps[-1]):
      mesg = "Average temperature too warm!"   
  except:
    mesg = "Temperature Error!"
  return mesg

# Function to simulate actual fish tank monitoring
def get_temps():
  return [65, 55, 70] 
