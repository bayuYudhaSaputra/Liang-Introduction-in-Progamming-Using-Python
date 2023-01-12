# Check Prime number
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
    # selama nilai divisor tidak lebih dari setengah dari number kerjakan
        if number % divisor == 0:
        # jika nilai number habis dibagi divisor maka
            return False
            # nilai dalam number bukan bilangan prima
        divisor += 1
    return True

def printPrimeNumbers(numberOfPrimes):
    NUMBER_OF_PRIMES = 50 # banyak bilangan prima yang ditampilkan
    NUMBER_OF_PRIMES_PER_LINE = 10 # banyak bilangan prima per baris
    count = 0 # nilai awal untuk looping untuk menampilkan bilangan prima
    number = 2 # nilai awal untuk dicek apakah prima atau bukan

    while count < numberOfPrimes:
        # selama nilai count tidak lebih dari numberOfPrime
        if isPrime(number):
        # 1. memanggil fungsi isPrime
        # 2. jika fungsi isPrime() bernilai true, kerjakan :
            count += 1 # nilai count ditambah satu
            print(format(number, "3d"), end = " ") # tampilkan nilai variabel number

            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # jika 10 bilangan sudah di-looping maka baris berpindah
                print()

        number += 1

def main():
    print("The first 50 prime numbers are")
    printPrimeNumbers(50)

main()