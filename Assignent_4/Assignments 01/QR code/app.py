import qrcode


data = "hayasheikh109@gmail.con"

img = qrcode.make(data)

img.save("E:/Assignent_4/Assignments 01/QR code/qrcode.png")

print("QR code generated successfully")


# from pyzbar.pyzbar import decode
# from PIL import Image

# # Open the image properly
# img = Image.open("E:/Assignent_4/Assignments 01/QR code/qrcode.png")

# # Decode the QR code
# result = decode(img)

# # Print the result
# print(result)
