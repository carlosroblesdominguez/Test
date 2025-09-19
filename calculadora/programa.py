import tkinter as tk

def operar(op):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if op == '+':
            resultado.set(n1 + n2)
        elif op == '-':
            resultado.set(n1 - n2)
        elif op == '*':
            resultado.set(n1 * n2)
        elif op == '/':
            resultado.set(n1 / n2 if n2 != 0 else "Error")
    except ValueError:
        resultado.set("Error")

root = tk.Tk()
root.title("Calculadora Básica")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack()

tk.Button(root, text="+", command=lambda: operar('+')).pack(side=tk.LEFT)
tk.Button(root, text="-", command=lambda: operar('-')).pack(side=tk.LEFT)
tk.Button(root, text="*", command=lambda: operar('*')).pack(side=tk.LEFT)
tk.Button(root, text="/", command=lambda: operar('/')).pack(side=tk.LEFT)

root.mainloop()
