import flet as ft
import time
import asyncio

class Timer(ft.UserControl):
    def __init__(self, page,initialtime=25):
            super().__init__()
            self.page = page
            self.initialtime=initialtime

    def build(self):
    
        self.runningtimer=False
        self.timer=ft.Text(str(self.initialtime),style=ft.TextThemeStyle.DISPLAY_LARGE,data= self.initialtime)
        self.startbutton=ft.ElevatedButton(text="Start timer !",on_click=self.timer_control)
    
        return ft.Column(width=1000, controls=[self.timer,self.startbutton])
        
    def counter(self):
        step=0.01
        while self.timer.data > 0 and self.runningtimer:
            time.sleep(step)
            self.timer.data-=0.01
            self.timer.value=str(int(self.timer.data)+1)
            self.timer.update()
            if self.timer.data<=0 :
                self.page.window_close()
                
                
    
    def timer_control(self,e):
        
        if not self.runningtimer:
            self.runningtimer=True
            self.counter()
        else:
            self.runningtimer=False
            self.counter()
            
