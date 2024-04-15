import random

print("Ben aklımdan bir sayı tutacağım ve sen o sayıyı bilmeye çalışacaksın.")

print("Zorluk seviyesini seçin.\n0) Çok Kolay (1'dan 3'e kadar)\n1) Kolay (1'dan 5'e kadar)\n2) Normal (1'dan 10'a kadar)\n3) Zor (1'dan 25'e kadar)\n4) Çok Zor (1'dan 50'ye kadar)\n5) Ekstrem Zor (1'dan 100'e kadar)\n6) İmkansız (1'dan 1000'e kadar)")


difficulty = int(input("Seçim: "))

if difficulty == 0:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 3)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 1:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 5)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 2:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 10)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 3:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 25)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 4:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 50)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 5:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 100)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

elif difficulty == 6:
    while True:
        guess = int(input("Tahmin et: "))

        answer = random.randrange(1, 1000)

        if answer == guess:
            print("Doğru")
        else:
            print("Yanlış")

else:
    print("Yanlış girdi girdiniz! Tekrar deneyin.")
        
