#Dictionary to contain game name and serial number
game_data={
  "pac man world":"40394","game of life":"69302","call of duty:big red one":"76034","cardinal syn":"40395","nhl '99":"22490"
}

def verify_name(name,dic):
  if name.lower() in dic.keys():
    return "True"
  else:
    return "False"

def verify_disknumber(disk_num):
  if (int(disk_num)>=1496833 and int(disk_num)<=5930214):
    return "True"
  else:
    return "False"

def verify_serial(name,serial,dic):
  if(serial==dic.get(name.lower())):
    return "True"
  else:
    return "False"

    
    



title="PythonCo. Disk Validation Checker"
#Initial program menu
print("="*37+"\n")
print(title.center(37)+"\n")
print("="*37+"\n")

disk_Name=input("Enter in the name of the disk and press ENTER:")
disk_Number=input("Enter in the disk number and press ENTER:")
disk_Serial=input("Enter in the disk serial number and press ENTER:")



#Display results
print("\n"*3+"RESULTS"+"\n")
print("="*40+"\n")

print("On Disk List:  "+verify_name(disk_Name,game_data))
print("Disk number Match: "+verify_disknumber(disk_Number))
print("Disk Serial Number Match: "+verify_serial(disk_Name,disk_Serial,game_data))

if(eval(verify_name(disk_Name,game_data)) and eval(verify_disknumber(disk_Number)) and eval(verify_serial(disk_Name,disk_Serial,game_data)) ):
  print ("\nTHIS IS A GENUINE DISK")
else:
  print("\nINVALID DISK")
