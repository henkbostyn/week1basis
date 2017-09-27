print("hallo")
print("nog eens hallo")
# dit betekent commentaar
# python interpreter gaat dit niet verwerken

# python GEEN declaratie van types
#bv java
# int x = 3;
# python ontdekt wel type het is
# Hoe ?
x = 3 #int, integer of geheel getal kan ook negatief -3
y= 3.0 #float door het punt
z = "3" # met een string

# commando type
print("x is van het type " + str(type(x)))
print(type(y))
print(type(z))

# naam = input("Tik aub uw naam in")
# print(naam)

print("een tekst \t met \"quotes\"  rond ")

print("Labo basic programming,\n\t Labo week1 Kennismaking met \"Python\"")

naam = "Bostyn"
voornaam  = "Henk"
leeftijd = 56

#slechte code
#print("Voornaam is : " + voornaam + "naam : " + naam + "leeftijd : " + leeftijd)

#veel beter is format gebruiken
# getallen formateren en vraagt minder resources
print("Voornaam is : {0} naam is : {1} en leeftijd is {2}".format(voornaam,naam,leeftijd))

