import tkinter as tk   
from tkinter import ttk   
from googletrans import Translator, LANGUAGES   

class TranslatorApp:
    def __init__(self, root):
        self.root = root   
        self.root.title("Language Translator")   
        self.translator = Translator()   
        self.setup_gui()   

    def setup_gui(self):
        #  label for input text
        tk.Label(self.root, text="Enter text:", font=("Arial", 12,)).grid(row=0, column=0, padx=10, pady=10)
        
        #  Text widget for user input
        self.input_text = tk.Text(self.root, height=5, width=50)
        self.input_text.grid(row=0, column=1, padx=10, pady=10)
        
        # label for source language selection
        tk.Label(self.root, text="Source language:").grid(row=1, column=0, padx=10, pady=10)
        
        #  ComboBox for selecting the source language
        self.source_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.source_lang.grid(row=1, column=1, padx=10, pady=10)
        self.source_lang.set("English")  # Set default value to "English"
        
        # label for target language selection
        tk.Label(self.root, text="Target language:").grid(row=2, column=0, padx=10, pady=10)
        
        # ComboBox for selecting the target language
        self.target_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.target_lang.grid(row=2, column=1, padx=10, pady=10)
        self.target_lang.set("French")  # Set default value to "French"
        
        # a button that will trigger the translation process
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # label for the output text area
        tk.Label(self.root, text="Translated text:",font=("Arial", 12,)).grid(row=4, column=0, padx=10, pady=10)
        
        # Text widget to display the translated text
        self.output_text = tk.Text(self.root, height=5, width=50)
        self.output_text.grid(row=4, column=1, padx=10, pady=10)
        self.output_text.config(state=tk.DISABLED)  # Set the output text area to be read-only initially

    def translate_text(self):
        # Retrieve the text entered by the user
        text = self.input_text.get("1.0", tk.END).strip()
        
        # Retrieve the selected source and target language names from ComboBoxes
        source_lang_name = self.source_lang.get()
        target_lang_name = self.target_lang.get()
        
        # Find the language codes corresponding to the selected language names
        source_lang_code = [key for key, value in LANGUAGES.items() if value.lower() == source_lang_name.lower()]
        target_lang_code = [key for key, value in LANGUAGES.items() if value.lower() == target_lang_name.lower()]
        
        # Check if the source or target language is not found
        if not source_lang_code or not target_lang_code:
            # Display an error message if languages are not found
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Error: Source or target language not found.")
            self.output_text.config(state=tk.DISABLED)
            return
        
        # Translate the text using the selected source and target language codes
        translated = self.translator.translate(text, src=source_lang_code[0], dest=target_lang_code[0])
        
        # Display the translated text in the output text area
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated.text)
        self.output_text.config(state=tk.DISABLED)  # Set the output text area to be read-only after updating

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = TranslatorApp(root)  # Instantiate the TranslatorApp class
    root.mainloop()  # Start the Tkinter event loop