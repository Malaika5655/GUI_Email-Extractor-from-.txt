import tkinter as tk
from tkinter import filedialog, messagebox
import re

class EmailExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📧 Email Extractor")
        self.root.geometry("600x500")
        self.root.configure(bg="#f9f5f0")  # Nude background

        # Title
        tk.Label(root, text="Email Extractor Tool", font=("Segoe UI", 18, "bold"),
                 bg="#f9f5f0", fg="#5e4b3c").pack(pady=(20, 10))

        # Instruction Label
        tk.Label(root, text="Select a .txt file to extract emails:", font=("Segoe UI", 12),
                 bg="#f9f5f0", fg="#6c5b4c").pack()

        # Browse Button
        self.button = tk.Button(root, text="📂 Browse File", command=self.browse_file,
                                font=("Segoe UI", 11, "bold"), bg="#d3bfa0", fg="white",
                                activebackground="#c4a484", activeforeground="white", relief="flat", bd=5)
        self.button.pack(pady=10)

        # Status Message
        self.status = tk.Label(root, text="", font=("Segoe UI", 11), bg="#f9f5f0", fg="#3e3e3e", wraplength=500)
        self.status.pack()

        # Text Box to Display Sorted Emails
        self.text_area = tk.Text(root, height=15, bg="#fffaf5", fg="#444", font=("Consolas", 11),
                                 wrap="word", relief="sunken", bd=2)
        self.text_area.pack(padx=20, pady=10, fill='both', expand=True)
        self.text_area.config(state='disabled')

        # Footer
        tk.Label(root, text="Developed by Malaika 💻", font=("Segoe UI", 9), bg="#f9f5f0", fg="#998675").pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as f:
                content = f.read()

            # Extract and sort emails
            emails = sorted(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)))

            if emails:
                output_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("Text files", "*.txt")])
                if output_file:
                    with open(output_file, "w") as f:
                        for email in emails:
                            f.write(email + "\n")

                # Display in text area
                self.text_area.config(state='normal')
                self.text_area.delete(1.0, tk.END)
                for email in emails:
                    self.text_area.insert(tk.END, email + "\n")
                self.text_area.config(state='disabled')

                self.status.config(text=f"✅ {len(emails)} email(s) extracted and displayed (sorted alphabetically).", fg="green")
            else:
                self.status.config(text="⚠️ No emails found in the file.", fg="orange")
                self.text_area.config(state='normal')
                self.text_area.delete(1.0, tk.END)
                self.text_area.config(state='disabled')

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Run the GUI
root = tk.Tk()
EmailExtractorGUI(root)
root.mainloop()
