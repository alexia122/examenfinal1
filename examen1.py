from tkinter import *
from datetime import date
from datetime import datetime


#instancia
raiz = Tk()
raiz.geometry("600x400")
raiz.title("Ejecución de Funciones")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('ARIAL BLACK', 19))


#--Funciones

#--Caputara de datos en variable
nombre = StringVar()
apellido = StringVar()
dia = IntVar()
mes = IntVar()
año = IntVar()


#--Convertir fecha a binario
def funbin():
     day=int(dia.get())
     month=int(mes.get())
     year=int(año.get())
     binday=format(day, '0b' )
     binmonth=format(month, '0b')
     binyear=format(year, '0b')

     lblResp['text'] = "La fecha es: {}/{}/{} y  en binario es:{}".format(day, month, year, binday, binmonth, binyear)


#--Retorno de días Vividos
def conteoDias():
    fechaString = f"{año.get()}-{mes.get()}-{dia.get()}"
    date_object = datetime.strptime(fechaString, '%Y-%m-%d')
    
    today=datetime.today()

    d1 = today
    d2 = date_object
    result1 = abs(d1-d2).days 

    #--today = str(date.today())
    #--result1 = today
    #--result2 = f"{result1}"
    respuesta = f"Usted nacio el {date_object} y ha vivido {result1} días."

    lblResp.configure(text = respuesta)


    #--Conteo de Letras de Nombre / Apellido
def conteoLetras():
    #--concatNombApelli = f"{nombre.get()}{apellido.get()}"
    sNombre = f"{nombre.get()}"
    sApellido = f"{apellido.get()}"

    conteoN = len(sNombre)
    conteoA = len(sApellido)
  
#--Validacion Nombre
    if conteoN % 2 == 0:
        r1 = f"{sNombre} su Nombre es de número Par"
    else:
        r1 = f"{sNombre} su Nombre es de número Inpar"
#--Validacion Apellido
    if conteoA % 2 == 0:
        r2 = f"{sApellido} su Apellido es de número Par."
    else:
        r2 = f"{sApellido} su Apellido es de número Inpar."

    respuesta = f"{r1} y  {r2} "

    lblResp.configure(text =respuesta )


    #--Conteo de Vocales y vocalesConsonantes
def vycon():
        sNombre=str(nombre.get())
        sApellido=str(apellido.get())
        cuenta = 0
        for carac in sNombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in sApellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        oso=len(sNombre)
        oso1=len(sApellido)
        consonante=oso+oso1-cuenta 

        lblResp['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)


        #--Nombre al alReves
def nomalrev():
     otro = nombre.get()+" "+apellido.get()
     otro = otro[::-1]
     lblResp["text"] = nombre.get() + " " + apellido.get() + " al revés es: " + otro


    #--Nombre
lblnombre= Label(miFrame, text="Nombre:")
lblnombre.grid(row=1, column=0)
lblnombre.config(padx=10, pady=10)
txtNombre=Entry(miFrame, textvariable =nombre)
txtNombre.grid(row=1, column=1)

#--Apellido
lblapellido=Label(miFrame, text="Apellido:")
lblapellido.grid(row=2, column=0)
lblapellido.config(padx=10, pady=10)
txtApellido=Entry(miFrame, textvariable =apellido)
txtApellido.grid(row=2, column=1)

#--Día
lbldia=Label(miFrame, text="Día: ")
lbldia.grid(row=3, column=0)
lbldia.config(padx=10, pady=10)
txtDia=Entry(miFrame, textvariable =dia)
txtDia.grid(row=3, column=1)

#--Mes
lblmes=Label(miFrame, text="Mes: ")
lblmes.grid(row=4, column=0)
lblmes.config(padx=10, pady=10)
txtMes=Entry(miFrame, textvariable =mes)
txtMes.grid(row=4, column=1)

#--Año
lblanio=Label(miFrame, text="Año: ")
lblanio.grid(row=5, column=0)
lblanio.config(padx=10, pady=10)
txtanio=Entry(miFrame, textvariable =año)
txtanio.grid(row=5, column=1)

#--Botones
btnFuncion1 = Button(miFrame, text="Función 1", command=funbin)
btnFuncion1.grid(row=6, column=0)
btnFuncion1.config(padx=8, pady=8)
btnFuncion2 = Button(miFrame, text ="Función 2", command=conteoDias)
btnFuncion2.grid(row=7, column=0)
btnFuncion2.config(padx=8, pady=8)
btnFuncion3 = Button(miFrame, text = "Función 3", command=conteoLetras)
btnFuncion3.grid(row=8, column=0)
btnFuncion3.config(padx=8, pady=8)
btnFuncion4 = Button(miFrame, text = "Función 4", command=vycon)
btnFuncion4.grid(row=6, column=1)
btnFuncion4.config(padx=8, pady=8)
btnFuncion5 = Button(miFrame, text = "Función 5", command=nomalrev)
btnFuncion5.grid(row=7, column=1)
btnFuncion5.config(padx=8, pady=8)

#--Respuesta
lblResp=Label(miFrame, text="Respuesta:")
lblResp.grid(row=9, column=0)
lblResp.config(padx=15, pady=15)
lblR=Label(miFrame)
lblR.grid(row=10, column=0)
lblR.config(padx=10, pady=10)

raiz.mainloop()