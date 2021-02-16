import tkinter
from PIL import ImageTk, Image

ventana = tkinter.Tk()
ventana.geometry("770x380")
ventana.title("Metodo de los Cuadrados Medios")
ventana.iconbitmap('./Images/unap.ico')

img_unap = ImageTk.PhotoImage(Image.open("./Images/una.png"))
labelImg = tkinter.Label(image = img_unap)

label1 = tkinter.Label(ventana, text = "UNIVERSIDAD NACIONAL DEL ALTIPLANO \nFACULTAD DE INGENIERÍA MECÁNICA ELÉCTRICA, ELECTRÓNICA Y SISTEMAS \nESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS \nSIMULACIÓN - VIII SEMESTRE", font=("Helvetica",8),justify = "left")
label2 = tkinter.Label(ventana, text = "MÉTODO DE LOS CUADRADOS MEDIOS", font=("Helvetica",10),justify = "right")

label3 = tkinter.Label(ventana, text = "Semilla: ",font=("Helvetica",10), justify="left")
label4 = tkinter.Label(ventana, text = "Digitos Significativos: ", font=("Helvetica",10),justify="left")
label5 = tkinter.Label(ventana, text = "Longitud de la Serie: ", font=("Helvetica",10),justify="left")
label6 = tkinter.Label(ventana, width=80, height= 12, bg="#4a9ff2", fg="black", font=("Helvetica",9))

text1 = tkinter.Entry(ventana, font="Helvetica 9")
text2 = tkinter.Entry(ventana, font="Helvetica 9")
text3 = tkinter.Entry(ventana, font="Helvetica 9")

def MetodoCuadradosMedios():
    semilla = text1.get()
    semilla = int(semilla)
    
    dig_sign = text2.get()
    dig_sign = int(dig_sign)

    len_serie = text3.get()
    len_serie = int(len_serie)

    textRes = ""
    for i in range(len_serie):
        cuadrado = semilla ** 2
        sem = str(cuadrado)
        aux = i
        textRes += "x"+str(i)+" = "+ str(semilla) + " => x^2 = "+ str(cuadrado) 
        if dig_sign >= len(sem):
            semilla = int(sem)
            alt = int(sem) / (10**dig_sign)
        else: 
            i = 0
            while len(sem) != dig_sign:
                if i%2 == 0:
                    sem = sem[:-1]
                else:
                    sem = sem[1:]
                i += 1
            semilla = int(sem)
            alt = int(sem) / (10**dig_sign)
        textRes += " => x"+str(aux+1) + " = " + str(sem) + " => u"+str(aux+1) + " = "+str(alt)+"\n" 
    label6["text"] = textRes

btn1 = tkinter.Button(ventana, text = "Generar", bg="#02e17d", fg="black", borderwidth=2, font = "Helvetica 11",command = MetodoCuadradosMedios)
btn1.grid(row = 4, column = 2 , pady = 10)

labelImg.grid(row = 0, column = 0,padx=5,pady=2)

label1.grid(row = 0, column = 1,columnspan=2)
label2.grid(row = 0, column = 3, columnspan=2, padx=20)
label3.grid(row = 1, column = 1)
label4.grid(row = 1, column = 2)
label5.grid(row = 1, column = 3)
label6.grid(row = 5, column = 1, columnspan=3)

text1.grid(row = 2, column = 1)
text2.grid(row = 2, column = 2)
text3.grid(row = 2, column = 3)

ventana.mainloop()