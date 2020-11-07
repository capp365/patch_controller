import commands as cmd 
import os
import time
from datetime import datetime
import pyautogui as pag

class PatchCon:
    def __init__(self,dir=None, difficulty='easy'):
        if dir is None:
            dir=str(datetime.now()).replace(':',"-").split('.')[0]
        self.dir='./playdata/'+dir+'/'
        os.mkdir(self.dir)
        cmd.start()
        boot_img=cmd.get_screenshot('first',self.dir)
        print(self.dir+boot_img+'.png')
        self.position=cmd.find_location(img_location=self.dir+boot_img+'.png')

    def get_cap(self):
        cmd.screen_capture(self.dir,self.position)
    
    def __call__(self):
        print('position:',self.position)
        time.sleep(5)
        print("skip first animation")
        #cmd.click(self.position[0]+100,self.position[1]+100)
        pag.click(self.position[0]+100,self.position[1]+100)
        time.sleep(0.5)
        print("skip first animation")
        pag.click(self.position[0]+500,self.position[1]+500)
        time.sleep(0.5)
        print("skip first animation")
        pag.click(self.position[0]+520,self.position[1]+500)
        time.sleep(0.5)
        print("skip first animation")
        pag.click(self.position[0]+250,self.position[1]+370)
        time.sleep(0.5)
        print("skip first animation")
        pag.click(self.position[0]+500,self.position[1]+180)

        while(True):
            self.get_cap()
            time.sleep(3)



def main():
    game=PatchCon()
    game()

if __name__ == '__main__':
    main()