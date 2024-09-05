import tkinter as tk
from tkinter import filedialog

class SimpleNotepad:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Notepad")

        # Text widget
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Save button
        self.save_button = tk.Button(self.button_frame, text='save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Load button
        self.load_button = tk.Button(self.button_frame, text='load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

    def save_file(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                               filetypes=[('Text files', '*.txt')])
        with open(file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f'File saved to: {file_path}')


    def load_file(self) -> None:
        file_path = filedialog.askopenfilename(defaultextension='.txt',
                                               filetypes=[('Text files', '*.txt')])
        
        with open(file_path, 'r') as file:
            content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
        
        print(f'File loaded from: {file_path}')

    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root = tk.Tk()
    app = SimpleNotepad(root=root)
    app.run()

if __name__ == "__main__":
    main()