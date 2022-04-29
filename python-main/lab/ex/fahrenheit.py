"""Erstellen Sie ein Script fahrenheit.py und lesen Sie von der Konsole die Temperatur in Fahrenheit ein.
Die eingelesene Zahl ist vom Typ Integer (int). Konvertieren Sie diese in eine Gleitkommazahl (float).
Berechnen Sie die Temperatur in Grad Celisus nach der Formel: Grad Celsius = 5 * (Fahrenheit-32) / 9
Geben Sie das Resultat auf der Konsole aus.
Beispiel Ausgabe:
Temperatur in Fahrenheit = 75.2
Fahrenheit   = 75.2
Grad Celsius = 24.0
"""

tempF = input("Temperature (F) : ") 
tempF = float(tempF)

tempC = 5*(tempF-32)/9
  
print("Temperatur in Fahrenheit = ",str(tempF),"\n", "- Fahrenheit   = ", str(tempF), "\n","- Celsius   = ", str(tempC),)

