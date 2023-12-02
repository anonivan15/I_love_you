import webbrowser
import time

print("SEY 'yes' OR 'no': ")
time.sleep(0.5)

print("")
print("I LOVE YOU")
time.sleep(0.5)
print("ARE YOU LOVE ME")

print("")
odgovor = input("--) ")

if odgovor.lower() == 'no':
    print("I FUCK YOU")
    time.sleep(1.5)
    url = "https://www.youtube.com/watch?v=I9Tqx3ajFc0"


    webbrowser.open(url)
    webbrowser.open(url)
    webbrowser.open(url)
 

    
elif odgovor.lower() == 'yes':
    time.sleep(0.5)
    print("I LOVE YOU TU...")
    time.sleep(0.5)
    print("SONG FOR YOU...")
    time.sleep(1.5)
    url = "https://www.youtube.com/watch?v=I9Tqx3ajFc0&t=2s"  # Ovdje dodajte URL koji želite otvoriti kad je odgovor 'yes'
    webbrowser.open(url)
else:
    print("YES OR NO :)")

# Otvori URL u zadanim web pregledniku


