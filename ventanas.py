from tkinter import Tk, ttk, messagebox

if __name__ == "__main__":
    def mostar_info():
        messagebox.showinfo("informacion", "hola mucho gusto")

    root = Tk()
    root.title("mi ventana")
    root.geometry("400x200")

    frm = ttk.Frame(root, padding=50)
    frm.grid()

    lbl = ttk.Label(frm, text="ventana python - ")
    lbl.grid(column=0, row=0)

    btn= ttk.Button(frm, text="quit", command=root.destroy)
    btn.grid(column=1, row=0)

    btn_info= ttk.Button(frm, text="informacion", command=mostar_info)
    btn_info.grid(column=2, row=0)

    root.mainloop()