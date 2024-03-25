def prime_checker(number):
  is_prime = True
  
  #Check if number is not prime.  Only prime numbers can be divided into 1 and 2
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime")
  else:
    print("It's not a prime number")  

  

#DON'T CHANGE CODE BELOW HERE
n = int(input()) #Check this number
prime_checker(number=n)