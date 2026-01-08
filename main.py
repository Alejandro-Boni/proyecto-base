import customtkinter as ctk
import os

class AppGastos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Base - Gastos")
        self.geometry("400x550") # Aumentamos un poco el alto

        # --- Interfaz (UI) ---
        self.label = ctk.CTkLabel(self, text="GESTIÓN DE GASTOS", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Descripción (ej. Cena)")
        self.entry_nombre.pack(pady=10)

        self.entry_monto = ctk.CTkEntry(self, placeholder_text="Monto $")
        self.entry_monto.pack(pady=10)

        self.btn_guardar = ctk.CTkButton(self, text="Guardar Gasto", command=self.guardar_dato)
        self.btn_guardar.pack(pady=20)

        self.textbox = ctk.CTkTextbox(self, width=300, height=180)
        self.textbox.pack(pady=10)

        # ETIQUETA DEL TOTAL (Nueva)
        self.label_total = ctk.CTkLabel(self, text="TOTAL ACUMULADO: $0.00", font=("Arial", 16, "bold"), text_color="#1f6aa5")
        self.label_total.pack(pady=15)

        self.cargar_datos()

    def calcular_total(self):
        """Lee el archivo datos.txt y suma todos los montos"""
        total = 0.0
        if os.path.exists("datos.txt"):
            with open("datos.txt", "r") as archivo:
                for linea in archivo:
                    try:
                        # Buscamos el símbolo $ y tomamos lo que está a la derecha
                        monto_str = linea.split("$")[-1].strip()
                        total += float(monto_str)
                    except:
                        continue
        self.label_total.configure(text=f"TOTAL ACUMULADO: ${total:,.2f}")

    def guardar_dato(self):
        nombre = self.entry_nombre.get()
        monto = self.entry_monto.get()
        if nombre and monto:
            try:
                # Validamos que el monto sea un número
                float(monto)
                linea = f"{nombre}: ${monto}\n"
                with open("datos.txt", "a") as archivo:
                    archivo.write(linea)
                
                self.textbox.insert("end", linea)
                self.entry_nombre.delete(0, 'end')
                self.entry_monto.delete(0, 'end')
                
                # Actualizamos el total después de guardar
                self.calcular_total()
            except ValueError:
                print("Error: El monto debe ser un número")

    def cargar_datos(self):
        if os.path.exists("datos.txt"):
            with open("datos.txt", "r") as archivo:
                contenido = archivo.read()
                self.textbox.insert("0.0", contenido)
            self.calcular_total() # Calculamos al abrir la app

if __name__ == "__main__":
    app = AppGastos()
    app.mainloop()