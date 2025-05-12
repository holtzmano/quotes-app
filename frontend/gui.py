import requests
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class QuoteClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quote Viewer")
        self.geometry("600x300")

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Input field for adding a new quote
        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Add a new quote...")
        self.entry.pack(pady=(20, 5))

        submit_btn = ctk.CTkButton(self.main_frame, text="Submit Quote", command=self.submit_quote)
        submit_btn.pack()


        self.quote_label = ctk.CTkLabel(self.main_frame, text="Click to get a quote!", font=("Helvetica", 16), wraplength=500, justify="center")
        self.quote_label.pack(pady=30)

        fetch_btn = ctk.CTkButton(self.main_frame, text="Get Quote", command=self.fetch_quote_from_server)
        fetch_btn.pack()

    def fetch_quote_from_server(self):
        try:
            response = requests.get("http://127.0.0.1:5000/api/quote", timeout=5)
            response.raise_for_status()
            quote = response.json()["quote"]
            self.quote_label.configure(text=quote)
        except Exception as e:
            self.quote_label.configure(text=f"Error: {e}")
            
    def submit_quote(self):
        quote_text = self.entry.get().strip()
        if not quote_text:
            self.quote_label.configure(text="Please enter a quote first.")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:5000/api/quote",
                json={"text": quote_text},
                timeout=5
            )
            if response.status_code == 201:
                self.quote_label.configure(text="Quote added successfully!")
                self.entry.delete(0, 'end')
            else:
                self.quote_label.configure(text=f"Error: {response.json().get('error')}")
        except Exception as e:
            self.quote_label.configure(text=f"Error: {e}")
            
    

if __name__ == "__main__":
    app = QuoteClientApp()
    app.mainloop()
