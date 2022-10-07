"""
A basic complex number calculator to do simples algebrics operations (+, -, *, /),
complex numbers in retangular ou polar form.
(+) and (-) operations required numbers in retangular form
(*) and (/) operations required numbers in polar form

This is the python script to do algebric operations with complex numbers

A GUI is created to interact with users:

1-) Enter the numbers
2-) Select the algebric operation (+, -, *, /)
3-) Click on Compute
4-) Results and history are updated

Important: In linux systems coment line --> # window.iconbitmap("circuit.ico")

Enjoyed

Joel Sánchez Domínguez
02_10_2022
"""
from tkinter import *
from tkinter import Frame
import tkinter.font as font
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math


# ComboBox Parent Class
class CustomBox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        #   initialisation of the combobox entry
        super().__init__(*args, **kwargs)
        #   "initialisation" of the combobox popdown
        self._handle_popdown_font()

    def _handle_popdown_font(self):
        """ Handle popdown font
        Note: https://github.com/nomad-software/tcltk/blob/master/dist/library/ttk/combobox.tcl#L270
        """
        #   grab (create a new one or get existing) popdown
        popdown = self.tk.eval('ttk::combobox::PopdownWindow %s' % self)
        #   configure popdown font
        self.tk.call('%s.f.l' % popdown, 'configure', '-font', self['font'])

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget. Overridden!

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """

        #   default configure behavior
        self.configure('configure')
        #   if font was configured - configure font for popdown as well
        if 'font' in kw or 'font' in cnf:
            self._handle_popdown_font()

    #   keep overridden shortcut
    config = configure


# Main Window
window = Tk()
window.title('Complex Number Calculator')
window.geometry("1030x400")
window.iconbitmap("circuit.ico")

# Fonts to used
buttonFont = font.Font(family='Arial', size=10, weight='bold')
lbltitlefont = font.Font(family='Arial', size=12, weight='bold')
lblfrfont = font.Font(family='Arial', size=10)


# Class Operator
class Operator:

    def __init__(self, caplblop, xlblop, ylblop, xfr, yfr, isop):
        # Atributos da classe
        self.real = 0.0
        self.imag = 0.0
        self.modulo = 0.0
        self.angle = 0.0

        # Elementos visuais de cada operador
        self.label = Label(text=caplblop, fg='black', font=lbltitlefont)
        self.label.place(x=xlblop, y=ylblop)
        self.fr: Frame = Frame(window, height=130, bg="azure2", width=280)
        self.fr.place(x=xfr, y=yfr)

        self.lbl_fr_ret = Label(self.fr, text="Retan:", fg='black', font=lblfrfont)
        self.lbl_fr_ret.place(x=10, y=10)
        self.real_txt = Text(self.fr, height=1, width=9)
        self.real_txt.place(x=60, y=10)
        self.lbl_j = Label(self.fr, text="j", fg='black', font=lblfrfont)
        self.lbl_j.place(x=150, y=10)

        self.imag_txt = Text(self.fr, height=1, width=9)
        self.imag_txt.place(x=160, y=10)

        self.lbl_fr_pol = Label(self.fr, text="Polar:", fg='black', font=lblfrfont)
        self.lbl_fr_pol.place(x=10, y=50)

        self.mod_txt = Text(self.fr, height=1, width=9)
        self.mod_txt.place(x=60, y=50)

        self.lbl_angle = Label(self.fr, text='\u2220', fg='black', font=lblfrfont)
        self.lbl_angle.place(x=140, y=50)

        self.angle_txt = Text(self.fr, height=1, width=9)
        self.angle_txt.place(x=160, y=50)

        self.lbl_grau = Label(self.fr, text='\u00B0', fg='black', font=("ArialBlack", 12))
        self.lbl_grau.place(x=240, y=50)

        # if isop == 0:
        #    self.btn_rigth = Button(self.fr, text="Res " + '\u279C' + " Op1", font=buttonFont)
        # else:
        if isop != 0:
            self.btn_rigth = Button(self.fr, text="Ret " + '\u279C' + " Pol", font=buttonFont, command=self.rettopolbtn)
            self.btn_rigth.place(x=50, y=90)

        # if isop == 0:
        #    self.btn_left = Button(self.fr, text="Res " + '\u279C' + " Op2", font=buttonFont)
        # else:
        if isop != 0:
            self.btn_left = Button(self.fr, text="Pol " + '\u279C' + " Ret", font=buttonFont, command=self.poltoretbtn)
            self.btn_left.place(x=150, y=90)

        if isop == 0:
            self.real_txt.configure(state='disabled')
            self.imag_txt.configure(state='disabled')
            self.mod_txt.configure(state='disabled')
            self.angle_txt.configure(state='disabled')
        self.clearvalues()

    # Metodos da classe
    # Get values from text box and update class variávels
    def getvalues(self):
        tmpstr = self.real_txt.get(1.0, "end")
        if tmpstr != "\n":
            tmpstr = tmpstr[:-1]
            self.real = float(tmpstr)
        else:
            self.real = 0.0
        tmpstr = self.imag_txt.get("1.0", "end")
        if tmpstr != "\n":
            tmpstr = tmpstr[:-1]
            self.imag = float(tmpstr)
        else:
            self.imag = 0.0
        tmpstr = self.mod_txt.get("1.0", "end")
        if tmpstr != "\n":
            tmpstr = tmpstr[:-1]
            self.modulo = float(tmpstr)
        else:
            self.modulo = 0.0
        tmpstr = self.angle_txt.get("1.0", "end")
        if tmpstr != "\n":
            tmpstr = tmpstr[:-1]
            self.angle = float(tmpstr)
        else:
            self.angle = 0.0

    # Updates text box from class variávels
    def setvalues(self):
        self.clearvalues()
        self.real_txt.insert("1.0", f'{self.real:.4f}')
        self.imag_txt.insert("1.0", f'{self.imag:.4f}')
        self.mod_txt.insert("1.0", f'{self.modulo:.4f}')
        self.angle_txt.insert("1.0", f'{self.angle:.4f}')

    # clear text box
    def clearvalues(self):
        self.real_txt.delete(1.0, tk.END)
        self.imag_txt.delete(1.0, tk.END)
        self.mod_txt.delete(1.0, tk.END)
        self.angle_txt.delete(1.0, tk.END)

    # retangular to polar transformation
    def rettopol(self):
        self.modulo = math.sqrt(self.real * self.real + self.imag * self.imag)
        if self.real != 0:
            if self.real > 0:
                self.angle = math.degrees(math.atan(self.imag / self.real))
            else:
                self.angle = math.degrees(math.atan(self.imag / self.real) + 3.141592)
        elif self.imag < 0:
            self.angle = -90
        elif self.imag > 0:
            self.angle = 90
        else:
            self.angle = 0
        self.setvalues()
        sign = '+'
        if self.imag < 0:
            sign = ''
        history_text.insert("1.0", f'{self.real:.2f}' + sign + f'{self.imag:.2f}' + 'j=' + f'{self.modulo:.2f}'
                            + '\u2220' + f'{self.angle:.2f}' + '\n')

    # Function to check valid retangular values
    def checkretvalues(self):
        try:
            float(self.real_txt.get(1.0, "end"))
            float(self.imag_txt.get(1.0, "end"))
        except ValueError:
            messagebox.showinfo("Error", "A forma retangular do numero deve ter valores válidos.")
            return FALSE
        else:
            return TRUE

    # Function to check valid polar values
    def checkpolvalues(self):
        try:
            float(self.mod_txt.get(1.0, "end"))
            float(self.angle_txt.get(1.0, "end"))
        except ValueError:
            messagebox.showinfo("Error", "A forma polar do numero deve ter valores válidos.")
            return FALSE
        else:
            return TRUE

    # method activate with rettopol button
    def rettopolbtn(self):
        if self.checkretvalues():
            self.getvalues()
            self.rettopol()

    # polar to retangular transformation
    def poltoret(self):
        sign = '+'
        self.real = self.modulo * math.cos(math.radians(self.angle))
        self.imag = self.modulo * math.sin(math.radians(self.angle))
        self.setvalues()
        if self.imag < 0:
            sign = ''
        history_text.insert("1.0",
                            f'{self.modulo:.2f}' + '\u2220' + f'{self.angle:.2f}' + '=' + f'{self.real:.2f}' + sign
                            + f'{self.imag:.2f}' + 'j\n')

    # method activate with poltoret button
    def poltoretbtn(self):
        if self.checkpolvalues():
            self.getvalues()
            self.poltoret()


# end Class Operator

# Funções do formulario


# clear all text box in the form
def clearall():
    Operator1.clearvalues()
    Operator2.clearvalues()
    Results.real_txt.configure(state='normal')
    Results.imag_txt.configure(state='normal')
    Results.mod_txt.configure(state='normal')
    Results.angle_txt.configure(state='normal')
    Results.clearvalues()
    Results.real_txt.configure(state='disabled')
    Results.imag_txt.configure(state='disabled')
    Results.mod_txt.configure(state='disabled')
    Results.angle_txt.configure(state='disabled')


# Verify operators to sum and subctration operations
def validopaddsub():
    if Operator1.checkretvalues() and Operator2.checkretvalues():
        return TRUE
    else:
        return FALSE


# Verify operators to multiplication operation
def validoproduto():
    if Operator1.checkpolvalues() and Operator2.checkpolvalues():
        return TRUE
    else:
        return FALSE


# Update results text box
def resultsupdate():
    Results.real_txt.configure(state='normal')
    Results.imag_txt.configure(state='normal')
    Results.mod_txt.configure(state='normal')
    Results.angle_txt.configure(state='normal')
    Results.setvalues()
    Results.real_txt.configure(state='disabled')
    Results.imag_txt.configure(state='disabled')
    Results.mod_txt.configure(state='disabled')
    Results.angle_txt.configure(state='disabled')


# Execute sum and subtraction operations
def computeaddsub(current_op):
    Operator1.getvalues()
    Operator2.getvalues()
    if current_op == 0:
        Results.real = Operator1.real + Operator2.real
        Results.imag = Operator1.imag + Operator2.imag
        strop = '+'
    else:
        Results.real = Operator1.real - Operator2.real
        Results.imag = Operator1.imag - Operator2.imag
        strop = '-'
    Results.rettopol()
    resultsupdate()
    sign1 = '+'
    sign2 = '+'
    signr = '+'
    if Operator1.imag < 0:
        sign1 = '-'
    if Operator2.imag < 0:
        sign2 = '-'
    if Results.imag < 0:
        signr = '-'
    history_text.insert("1.0", f'{Operator1.real:.2f}' + sign1 + f'{Operator1.imag:.2f}' + 'j ' + strop + ' ' +
                        f'{Operator2.real:.2f}' + sign2 + f'{Operator2.imag:.2f}' + 'j = ' +
                        f'{Results.real:.2f}' + signr + f'{Results.imag:.2f}' + 'j' + '\n')


# Execute multiplication operations
def computeproduto():
    Operator1.getvalues()
    Operator2.getvalues()
    Results.modulo = Operator1.modulo * Operator2.modulo
    Results.angle = Operator1.angle + Operator2.angle
    Results.poltoret()
    resultsupdate()
    history_text.insert("1.0", f'{Operator1.modulo:.2f}' + '\u2220' + f'{Operator1.angle:.2f}' + ' * ' +
                        f'{Operator2.modulo:.2f}' + '\u2220' + f'{Operator2.angle:.2f}' + ' = ' +
                        f'{Results.modulo:.2f}' + '\u2220' + f'{Results.angle:.2f}' + '\n')


# Execute division operations
def computedivision():
    Operator1.getvalues()
    Operator2.getvalues()
    Results.modulo = Operator1.modulo / Operator2.modulo
    Results.angle = Operator1.angle - Operator2.angle
    Results.poltoret()
    resultsupdate()
    history_text.insert("1.0", f'{Operator1.modulo:.2f}' + '\u2220' + f'{Operator1.angle:.2f}' + ' / ' +
                        f'{Operator2.modulo:.2f}' + '\u2220' + f'{Operator2.angle:.2f}' + ' = ' +
                        f'{Results.modulo:.2f}' + '\u2220' + f'{Results.angle:.2f}' + '\n')


# method activate with compute button
def compute():
    # Operations: 0: Soma, 1: Resta, 2: Produto, 3: Divisão
    current_op = operations.current()
    # current_op = operations.get()
    if current_op == 0 or current_op == 1:
        if validopaddsub():
            # calcular a operação
            computeaddsub(current_op)
        else:
            messagebox.showinfo("Error", "As partes reais e imaginarias dos operadores 1 e 2 devem possuir valores "
                                         "válidos.")
    elif current_op == 2:
        if validoproduto():
            # calcular a operação
            computeproduto()
        else:
            messagebox.showinfo("Error", "Os modulos e angulos dos operadores 1 e 2 devem possuir valores "
                                         "válidos.")
    else:
        if validoproduto() and float(Operator2.mod_txt.get(1.0, "end")) != 0:
            # calcular a operação
            computedivision()
        else:
            messagebox.showinfo("Error", "Os modulos e angulos dos operadores 1 e 2 devem possuir valores "
                                         "válidos.")


# method activate with resttop1 button
def restoop1():
    Operator1.clearvalues()
    Operator1.real_txt.insert("1.0", Results.real_txt.get(1.0, "end"))
    Operator1.imag_txt.insert("1.0", Results.imag_txt.get(1.0, "end"))
    Operator1.mod_txt.insert("1.0", Results.mod_txt.get(1.0, "end"))
    Operator1.angle_txt.insert("1.0", Results.angle_txt.get(1.0, "end"))


# method activate with resttop2 button
def restoop2():
    Operator2.clearvalues()
    Operator2.real_txt.insert("1.0", Results.real_txt.get(1.0, "end"))
    Operator2.imag_txt.insert("1.0", Results.imag_txt.get(1.0, "end"))
    Operator2.mod_txt.insert("1.0", Results.mod_txt.get(1.0, "end"))
    Operator2.angle_txt.insert("1.0", Results.angle_txt.get(1.0, "end"))


# MAIN
Operator1 = Operator("Operator 1", 10, 5, 10, 30, 1)

algebric_op = tk.StringVar()
algebric_op.font = lbltitlefont
operations = ttk.Combobox(window, width=2, font=lbltitlefont, textvariable=algebric_op)

# Adding combobox drop down list
operations['values'] = (' +',
                        ' -',
                        '\u2217',
                        ' /')

operations.place(x=310, y=70)
operations.current(0)

Operator2 = Operator("Operator 2", 370, 5, 370, 35, 1)

btn_compute = Button(window, text="COMPUTE", font=buttonFont, bg='turquoise', command=compute)
btn_compute.place(x=250, y=170)

btn_clear = Button(window, text="   CLEAR   ", font=buttonFont, bg='turquoise', command=clearall)
btn_clear.place(x=350, y=170)

Results = Operator("Result ", 200, 200, 200, 230, 0)

btn_rt1 = Button(window, text="Res " + '\u279C' + " Op1", font=buttonFont, command=restoop1)
btn_rt1.place(x=250, y=320)

btn_rt2 = Button(window, text="Res " + '\u279C' + " Op2", font=buttonFont, command=restoop2)
btn_rt2.place(x=350, y=320)

history_label = Label(text="History", fg='black', font=lbltitlefont)
history_label.place(x=680, y=5)

history_text = Text(window, height=20, width=40)
history_text.place(x=680, y=30)

window.mainloop()
