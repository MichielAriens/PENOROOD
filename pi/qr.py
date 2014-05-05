import os
import rsa

def decodeQR(path = "data/cam/QR"):
    result = None
    try:
        os.system("java -jar OTHER/read_qr_zep.jar > " + path)
        result = readQRstring()
    except:
        pass
    return result

def readQRstring(pathname):
    file_path = pathname
    f = open(file_path, 'r')
    string = f.read()
    return string

def decodeString():
    pass

def create_keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return(pubkey,privkey)

def encrypt_message(message, public_key):
    encrypted_message = rsa.encrypt(message,public_key)
    return encrypted_message

def decrypt_message(message, private_key):
    decrypted_message = rsa.decrypt(message, private_key)
    return decrypted_message

def testRSA():
    (pubkey,privkey) = create_keys()
    enc_mes = encrypt_message('Hallo, ik ben Michiel.', pubkey)
    print(enc_mes)
    dec_mes = decrypt_message(enc_mes, privkey)
    print(dec_mes)

def getImageFromSite():
    import urllib
    urllib.urlretrieve("http://192.168.2.134:5000/static/rood" +str(1) + ".png", "C:\PENO\pic.png")
    os.system("java -jar C:\PENO\qread_qr_zep.jar > C:\PENO\qrresults.txt")
    file = open("C:\PENO\qrresults.txt","r")
    results = file.read()
    print "*********************"
    print str(results)
    print "*********************"

getImageFromSite()
