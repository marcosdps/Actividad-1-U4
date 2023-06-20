from tkinter import *
from tkinter import ttk
import math

class Interfaz():
    __ventana= None
    __cantVestimenta=None
    __cantAlimento=None
    __cantEducacion=None
    __precioBaseVesti=None
    __precioBaseAli=None
    __precioBaseEdu=None
    __precioActualVesti=None
    __precioActualAli=None
    __precioActualEdu=None


    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("450x210")
        self.__ventana.title("Calculadora IPC")
        opcion={ "padx":7, "pady":7}
        self.ingresoDatos()
        self.botones(opcion)
        self.subtitulos(opcion)
        
    def calcular(self):
        canastaAñoBase = (int(self.__cantVestimenta.get()) * float(self.__precioBaseVesti.get()))+ (int(self.__cantAlimento.get()) * float(self.__precioBaseAli.get()))+(int(self.__cantEducacion.get()) * float(self.__precioBaseEdu.get()))
        canastaAñoActual = (float(self.__cantVestimenta.get()) * float(self.__precioActualVesti.get())) + (float(self.__cantAlimento.get()) * float(self.__precioActualAli.get())) + (float(self.__cantEducacion.get()) * float(self.__precioActualEdu.get()))
        resultado=canastaAñoActual/canastaAñoBase
        fraccional, noUso = math.modf(resultado)
        IPC = round(fraccional*100, 2)
        labelResultado = ttk.Label(self.__ventana, text="")
        labelResultado.grid(row = 6, column=1,padx=7, pady=7)
        labelResultado.config(text=f"IPC: {IPC}%")
        
    def botones(self, opcion):
        salir = ttk.Button(self.__ventana, text = "Salir", command=self.__ventana.destroy)
        calcular = ttk.Button(self.__ventana, text = "Calcular IPC", command= self.calcular)
        calcular.grid(row=5, column=1, sticky="SE",**opcion)
        salir.grid(row= 5, column=3, sticky="SE",**opcion)
        

    def ejecutar(self):
        self.__ventana.mainloop()
    
    def subtitulos(self, opcion):
        ttk.Label(self.__ventana,text="Item").grid(row = 0, column=0,**opcion)
        ttk.Label(self.__ventana,text="Cantidad").grid(row = 0, column=1, **opcion)
        ttk.Label(self.__ventana,text="Precio Año Base").grid(row = 0, column=2, **opcion)
        ttk.Label(self.__ventana,text="Precio Año Actual").grid(row = 0, column=3,**opcion)
        ttk.Label(self.__ventana,text="Vestimenta").grid(row = 1, column=0,**opcion)
        ttk.Label(self.__ventana,text="Alimentos").grid(row = 2, column=0, **opcion)
        ttk.Label(self.__ventana,text="Educacion").grid(row = 3, column=0,**opcion)

    def ingresoDatos(self):
        self.__cantVestimenta = ttk.Entry(self.__ventana, width=10)
        self.__cantVestimenta.grid(row=1, column=1)
        self.__precioBaseVesti = ttk.Entry(self.__ventana, width=10)
        self.__precioBaseVesti.grid(row=1, column=2)
        self.__precioActualVesti = ttk.Entry(self.__ventana, width=10)
        self.__precioActualVesti.grid(row=1, column=3)
        self.__cantAlimento = ttk.Entry(self.__ventana, width=10)
        self.__cantAlimento.grid(row=2, column=1)
        self.__precioBaseAli = ttk.Entry(self.__ventana, width=10)
        self.__precioBaseAli.grid(row=2, column=2)
        self.__precioActualAli = ttk.Entry(self.__ventana, width=10)
        self.__precioActualAli.grid(row=2, column=3)
        self.__cantEducacion = ttk.Entry(self.__ventana, width=10)
        self.__cantEducacion.grid(row=3, column=1)
        self.__precioBaseEdu = ttk.Entry(self.__ventana, width=10)
        self.__precioBaseEdu.grid(row=3, column=2)
        self.__precioActualEdu = ttk.Entry(self.__ventana, width=10)
        self.__precioActualEdu.grid(row=3, column=3)
        
    
        