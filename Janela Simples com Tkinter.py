from tkinter import *

window = Tk()
window.title("Janelinha")
window.geometry("500x500")

# Cria um Frame interno com fundo cinza
inner_frame = Frame(window, bg='gray')
inner_frame.place(relx=0.5, rely=0.5, anchor='center')

equation_text = "Linha de texto"
label = Label(inner_frame, text=equation_text, font=("Helvetica", 30), fg='black', bg='gray')
label.pack()

window.mainloop()
