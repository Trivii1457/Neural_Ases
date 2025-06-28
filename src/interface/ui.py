from tkinter import Tk, Text, Button, Label, Scrollbar, END, messagebox
from pdf_generator.generator import PDFGenerator
from neural_network.model import NeuralNetwork

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Generador de Informes con Red Neuronal")

        self.label = Label(master, text="Ingrese el texto plano:")
        self.label.pack()

        self.text_input = Text(master, height=10, width=50)
        self.text_input.pack()

        self.generate_button = Button(master, text="Generar Informe", command=self.generate_report)
        self.generate_button.pack()

        self.scrollbar = Scrollbar(master, command=self.text_input.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.text_input.config(yscrollcommand=self.scrollbar.set)

        self.output_label = Label(master, text="Informe generado:")
        self.output_label.pack()

        self.output_text = Text(master, height=10, width=50)
        self.output_text.pack()

        self.neural_network = NeuralNetwork()
        self.pdf_generator = PDFGenerator()

    def generate_report(self):
        input_text = self.text_input.get("1.0", END).strip()
        if not input_text:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un texto.")
            return

        dimensions, generated_text = self.neural_network.process_input(input_text)
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, generated_text)

        pdf_path = self.pdf_generator.create_pdf(generated_text, dimensions)
        messagebox.showinfo("Informe Generado", f"El informe se ha guardado en: {pdf_path}")

if __name__ == "__main__":
    root = Tk()
    ui = UserInterface(root)
    root.mainloop()