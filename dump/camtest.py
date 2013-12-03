import modules.hardware.camera as cam


mycam = cam.Camera(height = 500, width = 500)
while(True):
    x = raw_input("go")
    mycam.click()
    print str(mycam.getQR())
    
    
