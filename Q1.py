import numpy as np
from PIL import Image
from colorama import Fore


def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    print(img.mode)

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print(Fore.RED +"ERROR: Need larger file size" + Fore.BLACK)

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully!!!" + Fore.BLACK)

def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print(Fore.GREEN + "Hidden Message:" + Fore.BLACK, message[:-5])
    else:
        print(Fore.RED + "No Hidden Message Found" + Fore.BLACK)

def Stego():
    print(Fore.BLUE + "<<<<<<<<<<Welcome to cryptography>>>>>>>>>>")
    print(Fore.YELLOW + "Please choose one of the two options below :")
    print(Fore.GREEN + "1-" + Fore.BLACK + " " + "Encode")
    print(Fore.GREEN + "2-" + Fore.BLACK + " " + "Decode" + Fore.GREEN)



    func = input()

    if func == '1':
        print(Fore.BLUE +"Enter Source Image Path :" + Fore.BLACK)
        src = input()
        print(Fore.BLUE +"Enter Message to Hide :" + Fore.BLACK)
        message = input()
        print(Fore.BLUE +"Enter Destination Image Path :" + Fore.BLACK)
        dest = input()
        print(Fore.YELLOW + "Encoding..." + Fore.GREEN)
        Encode(src, message, dest)

    elif func == '2':
        print(Fore.BLUE +"Enter Source Image Path :" + Fore.BLACK)
        src = input()
        print(Fore.YELLOW +"Decoding..." + Fore.GREEN)
        Decode(src)

    else:
        print(Fore.RED +"ERROR: Invalid option chosen"+ Fore.BLACK)

if __name__ == "__main__":
    Stego()