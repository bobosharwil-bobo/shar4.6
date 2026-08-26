import customtkinter as ctk 
from PIL import Image

# Main frame colours
top_frame_color = "#11182D"
middle_frame_color = "#0B1020"
bottom_frame_color = "#11182D"

root = ctk.CTk()
root.geometry("600x500")
root.title("Crypto Message App")

# Creating top frame
top_frame = ctk.CTkFrame(
    root,
    fg_color=top_frame_color,
    height=120
)

top_frame.pack(
    fill="x",
    pady=4
)

# Loading Images
logo = ctk.CTkImage(
    Image.open("logo.png"),
    size=(180, 98)
)

orchids_image = ctk.CTkImage(
    Image.open("orchids.png"),
    size=(100, 100)
)

# Logo image
logo_image = ctk.CTkLabel(
    top_frame,
    image=logo,
    text="",
    fg_color=top_frame_color
)

logo_image.pack(
    side="left",
    padx=(10, 0)
)

# Orchids image
orchids_label = ctk.CTkLabel(
    top_frame,
    image=orchids_image,
    text="",
    fg_color=top_frame_color
)

orchids_label.pack(
    side="right",
    padx=(10, 20)
)

# Label inside top frame
message_label = ctk.CTkLabel(
    top_frame,
    text="Message Encrypter",
    font=("Cascadia Code SemiBold", 20, "bold"),
    text_color="#A78BFA"
)

message_label.pack(
    side="left",
    padx=(20, 0)
)

# Middle frame
middle_frame = ctk.CTkFrame(
    root,
    fg_color=middle_frame_color
)

middle_frame.pack(
    fill="both",
    expand=True,
    pady=(0, 0)
)

# Left middle frame
left_middle = ctk.CTkFrame(
    middle_frame,
    fg_color="#151D38",
    width=260,
    corner_radius=12
)

left_middle.pack(
    side="left",
    padx=(25, 5),
    fill="both",
    expand=True
)

# Right middle frame
right_middle = ctk.CTkFrame(
    middle_frame,
    fg_color="#202A4A",
    width=260,
    corner_radius=12
)

right_middle.pack(
    side="right",
    padx=(5, 25),
    fill="both",
    expand=True
)

# Label inside right frame
message_label1 = ctk.CTkLabel(
    right_middle,
    text="Enter Secret Message",
    font=("Cascadia Code SemiBold", 20, "bold"),
    text_color="#F8FAFC"
)

message_label1.pack(
    fill="x",
    pady=5
)

# Bottom frame
bottom_frame = ctk.CTkFrame(
    root,
    fg_color=bottom_frame_color
)

bottom_frame.pack(
    fill="x",
    pady=(4, 0)
)

# Buttons container
buttons_container = ctk.CTkFrame(
    bottom_frame,
    fg_color="#17213A"
)

buttons_container.pack(
    fill="x",
    expand=True,
    pady=15
)

root.mainloop()