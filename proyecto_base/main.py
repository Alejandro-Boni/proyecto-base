import customtkinter as ctk
import os

class AppGastos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Base - Gastos")
        self.geometry("400x500")

        # UI: Título y Entradas
        self.label = ctk.CTkLabel(self, text="GESTIÓN DE GASTOS", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Descripción (ej. Cena)")
        self.entry_nombre.pack(pady=10)

        self.entry_monto = ctk.CTkEntry(self, placeholder_text="Monto $")
        self.entry_monto.pack(pady=10)

        self.btn_guardar = ctk.CTkButton(self, text="Guardar Gasto", command=self.guardar_dato)
        self.btn_guardar.pack(pady=20)

        self.textbox = ctk.CTkTextbox(self, width=300, height=200)
        self.textbox.pack(pady=10)

        # Cargar datos previos al abrir
        self.cargar_datos()

    def guardar_dato(self):
        nombre = self.entry_nombre.get()
        monto = self.entry_monto.get()
        if nombre and monto:
            linea = f"{nombre}: ${monto}\n"
            with open("datos.txt", "a") as archivo:
                archivo.write(linea)
            self.textbox.insert("end", linea)
            self.entry_nombre.delete(0, 'end')
            self.entry_monto.delete(0, 'end')

    def cargar_datos(self):
        if os.path.exists("datos.txt"):
            with open("datos.txt", "r") as archivo:
                contenido = archivo.read()
                self.textbox.insert("0.0", contenido)

if __name__ == "__main__":
    app = AppGastos()
    app.mainloop()