import tkinter

calculator=tkinter.Tk()
calculator.title("BMI Calculator")
calculator.geometry("300x200")


labelinho = tkinter.Label(text="BMI Calculator")
labelinho.grid(row=1,column=1)

wlabelinho = tkinter.Label(text="Enter Your Weight (kg):")
wlabelinho.grid(row=2,column=0)
wentryinho = tkinter.Entry()
wentryinho.grid(row=2,column=1)

hlabelinho = tkinter.Label(text="Enter Your Height (cm):")
hlabelinho.grid(row=3,column=0)
hentryinho = tkinter.Entry()
hentryinho.grid(row=3,column=1)

def Calculating():
    try:
        weight = float(wentryinho.get())
        height = float(hentryinho.get())
        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        bmi_result.set(f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        bmi_result.set("Please enter valid numbers")

bmi_result=tkinter.StringVar()
tkinter.Label(calculator,textvariable=bmi_result,).grid(row=5,columnspan=3)


buttoninho = tkinter.Button(text="Calculate",command=Calculating)
buttoninho.grid(row=4,columnspan=3)










tkinter.mainloop()