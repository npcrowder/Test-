def main():
 print('Hello World! Bellevue family!')
 x = input("What is your favorite animal?")
 if x == "yes":
  print ("yes is not an animal")
  y = input ("Could you enter an animal now?")
  if y == "yes":
    main()
 else:
  print ("I love " + x + "s. ")
  z = input("Do you like any other animals?")
  if z == "yes":
    main()
main()