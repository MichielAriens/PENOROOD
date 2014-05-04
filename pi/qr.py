import os
import rsa

def decodeQR(self):
    result = None
    try:
        pathname = "data/cam/QR"
        os.system("java -jar resources/read_qr_zep.jar > " + pathname)
        #p = subprocess.Popen("java -jar resources/QR_decoder.jar")
        #out, err = p.communicate()
        #Try to open the file
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

testRSA()
