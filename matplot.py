import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart
from time import sleep
import numpy as np

matplotlib.use("svg")
import sys



class PlotterMatplot(ft.UserControl):
    def build(self):
    
        self.mu_default, self.sigma_default= 1, 0.1
        self.bins_default, self.events_default=100,1000
        self.fig, self.ax = plt.subplots()

        s = np.random.normal(self.mu_default,self.sigma_default, self.events_default)
        
        
        self.ax.hist(s, self.bins_default , density=True)
        self.chart= MatplotlibChart(self.fig, isolated=True)
        self.muslider=ft.Slider(min=0, max=100, divisions=100,value=self.mu_default, label="mean: {value}", on_change_end=self.action_slider)
        self.sigmaslider=ft.Slider(min=0, max=100, divisions=100,value=self.sigma_default, label="sigma: {value}",on_change_end=self.action_slider)
        self.bins=ft.TextField(label="number of bin", hint_text="Please enter number of bins",value=str(self.bins_default), on_submit=self.action_slider)
        self.events=ft.TextField(label="number of event", hint_text="Please enter number of events",value=str(self.events_default), on_submit=self.action_slider)
        self.bar=ft.SnackBar(content=ft.Text("please enter a proper value (integer)", color=ft.colors.WHITE), bgcolor=ft.colors.RED,action="reset to default value",action_color=ft.colors.GREEN, on_action=self.reset_default)
        
        self.plot=ft.Column(width=1000, controls=[self.chart, self.muslider, self.sigmaslider, ft.Row(controls=[self.bins, self.events]), self.bar])

        #application's root control (i.e. "view") containing all other controls
        return self.plot
    def recompute_gaussian(self):
        
        mu=self.muslider.value
        sigma=self.sigmaslider.value
        try :
            bins=int(self.bins.value)
            events=int(self.events.value)
            
            print(f"mu: {mu}, sigma: {sigma}") 
            print(f"events: {events}, bins: {bins}")
            s = np.random.normal(self.muslider.value, self.sigmaslider.value, events)
            self.ax.clear()
            self.ax.hist(s, bins, density=True)
            self.chart.update()
        except ValueError:
           self.bar.open=True
           self.update()
           print("please enter a proper value (integer)")
           sys.exit(1)
        except Exception:
            self.bar.content="an unknow error has occur, closing the application"
            self.bar.open=True
            print("an unknow error has occur, closing the application")
           
        return
        
    def reset_default(self,e):
        self.bins.value=str(self.bins_default)
        self.events.value=str(self.events_default)
        self.recompute_gaussian()
        self.bins.update()
        self.events.update()
        return
        
        
    def action_slider(self,e):
        self.recompute_gaussian()


def main(page: ft.Page):
    page.title = "matplot App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll=True
    page.update()

    # create application instance
    plotter = PlotterMatplot()
    # add application's root control to the page
    page.add(plotter)
    page.update()

ft.app(target=main)
