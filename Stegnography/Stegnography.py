import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, PngImagePlugin
import codecs

# Create the main window
root = tk.Tk()
root.title("Image Text Encryption Tool")
root.geometry("400x300")


# Function to encode text into an image
def encode_text():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter text to encode.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not save_path:
        return

    try:
        hex_encoded = codecs.encode(text.encode(), "hex").decode()
        img = Image.open(file_path)
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("text", hex_encoded)
        img.save(save_path, "PNG", pnginfo=metadata)
        messagebox.showinfo("Success", "Text successfully encoded into image!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to decode text from an image
def decode_text():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    try:
        img = Image.open(file_path)
        hex_encoded = img.git text.get("text", "")
        decoded_text = codecs.decode(hex_encoded, "hex").decode()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decoded_text)
        messagebox.showinfo("Decoded Text", decoded_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Elements
label = tk.Label(root, text="Enter text to hide:")
label.pack(pady=5)

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

encode_button = tk.Button(root, text="Encode Text into Image", command=encode_text)
encode_button.pack(pady=5)

decode_button = tk.Button(root, text="Decode Text from Image", command=decode_text)
decode_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
