from gpiozero import Button

button = Button(22)

button.wait_for_press()
print("Hello Linux Voice readers…your hacking with GPIO Zero")
