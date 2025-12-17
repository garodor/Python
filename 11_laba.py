import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Копылов Владислав Александрович")  
        self.root.geometry("600x400")
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        self.calculator()
        self.checkbox()
        self.text()


    def calculator(self):
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Калькулятор")
        input_frame = ttk.Frame(tab1)
        input_frame.pack(pady=20)

        self.num1_entry = ttk.Entry(input_frame, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.operation_var = tk.StringVar(value="+")
        operations = ['+', '-', '*', '/']
        self.operation_combo = ttk.Combobox(input_frame, textvariable=self.operation_var, 
                                          values=operations, state='readonly')
        self.operation_combo.grid(row=1, column=1, padx=5, pady=5)

        self.num2_entry = ttk.Entry(input_frame, width=15)
        self.num2_entry.grid(row=2, column=1, padx=5, pady=5)

        self.num3_entry = ttk.Entry(input_frame, width=15)
        self.num3_entry.grid(row=3, column=1, padx=5, pady=5)

        calc_button = ttk.Button(tab1, text="Вычислить", command=self.calculate)
        calc_button.pack(pady=10)
        
    def calculate(self):
        num1_str = self.num1_entry.get().strip()
        num2_str = self.num2_entry.get().strip()
        operation = self.operation_var.get()
        if not num1_str or not num2_str:
            messagebox.showerror("Ошибка", "Введите оба числа!")
            return
        num1 = float(num1_str)
        num2 = float(num2_str)
        if operation == '+':
            self.result = num1 + num2
        elif operation == '-':
            self.result = num1 - num2
        elif operation == '*':
            self.result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
                return
            self.result = num1 / num2
            
        self.num3_entry.delete(0, tk.END)
        self.num3_entry.insert(0, int(self.result))

    
    def checkbox(self):
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text="Чекбоксы")
        
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        
        checkbox1 = ttk.Checkbutton(
            tab2,
            text='Опция 1',
            command=self.check_message,
            variable=self.var1,
        )
        checkbox1.pack(pady=5)
        
        checkbox2 = ttk.Checkbutton(
            tab2,
            text='Опция 2', 
            command=self.check_message,
            variable=self.var2,
        )
        checkbox2.pack(pady=5)
        
        checkbox3 = ttk.Checkbutton(
            tab2,
            text='Опция 3',
            command=self.check_message,
            variable=self.var3,
        )
        checkbox3.pack(pady=5)
        
        ttk.Button(tab2, text="Показать состояние", 
                  command=self.show_state).pack(pady=10)
        
    def check_message(self):
        self.selected = []
        if self.var1.get():
            self.selected.append("Опция 1")
        if self.var2.get():
            self.selected.append("Опция 2") 
        if self.var3.get():
            self.selected.append("Опция 3")

    def show_state(self):
            messagebox.showinfo("Состояние", f"Выбрано: {', '.join(self.selected)}")
    
        
    def text(self):
        tab3 =ttk.Frame(self.notebook)
        self.notebook.add(tab3, text="Текст")
        text_frame = ttk.Frame(tab3)
        button = ttk.Button(tab3, text="Вставить текст", command=self.text_click)
        button.pack(pady=10)
        text_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.text_box = tk.Text(text_frame, height=40, width=40)
        self.text_box.pack()

    def text_click(self):
        path = "text.txt"
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(1.0, content)

        
      
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root) 
    root.mainloop()