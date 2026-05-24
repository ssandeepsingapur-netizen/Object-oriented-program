import qrcode
img = qrcode.make("https://i.pinimg.com/control1/736x/31/dc/76/31dc76b88cfba521b6f3836b8f439a03.jpg")
img.save("python_notes.png")
print("File saved successfully.")