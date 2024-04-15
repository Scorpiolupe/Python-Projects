# Python ile yılan oyunu
# Kaynak: [1]

import turtle
import time
import random

# Ekran ayarları
ekran = turtle.Screen()
ekran.title("Yılan Oyunu")
ekran.bgcolor("green")
ekran.setup(width=600, height=600)
ekran.tracer(0) # Ekran güncellemelerini kapatır

# Yılan başı
bas = turtle.Turtle()
bas.speed(0)
bas.shape("square")
bas.color("black")
bas.penup()
bas.goto(0,0)
bas.direction = "stop"

# Yem
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0,100)

# Skor
skor = 0
yuksek_skor = 0

# Skor tahtası
tahta = turtle.Turtle()
tahta.speed(0)
tahta.shape("square")
tahta.color("white")
tahta.penup()
tahta.hideturtle()
tahta.goto(0, 260)
tahta.write("Skor: 0  Yüksek Skor: 0", align="center", font=("Courier", 24, "normal"))

# Yılan vücudu
vucutlar = []

# Hareket fonksiyonları
def yukari():
    if bas.direction != "down":
        bas.direction = "up"

def asagi():
    if bas.direction != "up":
        bas.direction = "down"

def saga():
    if bas.direction != "left":
        bas.direction = "right"

def sola():
    if bas.direction != "right":
        bas.direction = "left"

def hareket():
    if bas.direction == "up":
        y = bas.ycor()
        bas.sety(y + 20)

    if bas.direction == "down":
        y = bas.ycor()
        bas.sety(y - 20)

    if bas.direction == "right":
        x = bas.xcor()
        bas.setx(x + 20)

    if bas.direction == "left":
        x = bas.xcor()
        bas.setx(x - 20)

    if bas.direction == "up" and bas.direction == "down":
        pass

# Klavye bağlantıları
ekran.listen()
ekran.onkeypress(yukari, "Up")
ekran.onkeypress(asagi, "Down")
ekran.onkeypress(saga, "Right")
ekran.onkeypress(sola, "Left")

# Ana döngü
while True:
    ekran.update()

    # Kenarlara çarpma kontrolü
    if bas.xcor()>290 or bas.xcor()<-290 or bas.ycor()>290 or bas.ycor()<-290:
        time.sleep(1)
        bas.goto(0,0)
        bas.direction = "stop"

        # Vücutları gizleme
        for vucut in vucutlar:
            vucut.goto(1000, 1000)
        
        # Vücut listesini temizleme
        vucutlar.clear()

        # Skoru sıfırlama
        skor = 0

        # Skor tahtasını güncelleme
        tahta.clear()
        tahta.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal")) 


    # Yeme çarpma kontrolü
    if bas.distance(yem) < 20:
        # Yemi rastgele bir yere taşıma
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        yem.goto(x,y)

        # Yeni bir vücut parçası ekleme
        yeni_vucut = turtle.Turtle()
        yeni_vucut.speed(0)
        yeni_vucut.shape("square")
        yeni_vucut.color("grey")
        yeni_vucut.penup()
        vucutlar.append(yeni_vucut)

        # Skoru artırma
        skor += 10

        if skor > yuksek_skor:
            yuksek_skor = skor
        
        # Skor tahtasını güncelleme
        tahta.clear()
        tahta.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal")) 

    # Vücut parçalarını baştan sona doğru hareket ettirme
    for index in range(len(vucutlar)-1, 0, -1):
        x = vucutlar[index-1].xcor()
        y = vucutlar[index-1].ycor()
        vucutlar[index].goto(x, y)

    # Vücudun ilk parçasını başın arkasına taşıma
    if len(vucutlar) > 0:
        x = bas.xcor()
        y = bas.ycor()
        vucutlar[0].goto(x,y)

    hareket()    

    # Kendi vücuduna çarpma kontrolü
    for vucut in vucutlar:
        if vucut.distance(bas) < 20:
            time.sleep(1)
            bas.goto(0,0)
            bas.direction = "stop"

            # Vücutları gizleme
            for vucut in vucutlar:
                vucut.goto(1000, 1000)
        
            # Vücut listesini temizleme
            vucutlar.clear()

            # Skoru sıfırlama
            skor = 0

            # Skor tahtasını güncelleme
            tahta.clear()
            tahta.write("Skor: {}  Yüksek Skor: {}".format(skor, yuksek_skor), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)

ekran.mainloop()
