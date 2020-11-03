Temp = input ("Temperatura esterna: ")

if Temp > "30" and Temp < "35":
    print("Indossa pure una t-shirt")
elif Temp > "20" and Temp < "30":
    print("Indossa un maglione")
elif Temp <= "20":
    print("Indossa un cappotto")
else:
    print("Vai pure in giro a petto nudo!")
