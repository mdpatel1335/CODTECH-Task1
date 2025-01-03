import tkinter as tk
import re

def check_password_strength(password):
    # Minimum password length
    min_length = 8
    
    # Check length of password
    if len(password) < min_length:
        return "Password is too short, it must be at least 8 characters long."

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check if the password contains at least one number
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check if the password contains at least one special character
    if not re.search(r'[@$!%*?&]', password):
        return "Password must contain at least one special character (@, $, !, %, *, ?, &)."

    # If password passes all checks, it's strong
    return "Password is strong."

def on_check_button_click():
    password = password_entry.get()  # Get the password entered by the user
    strength_message = check_password_strength(password)  # Check the password strength
    result_label.config(text=strength_message)  # Update the result label with the message

# Set up the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")  # Set the window size to be larger
root.configure(bg="lightblue")  # Set the background color of the entire window

# Label for instructions with bigger font
instruction_label = tk.Label(root, text="Enter your password:", font=("Arial", 16), bg="lightblue")
instruction_label.pack(pady=20)  # Increased padding for spacing

# Entry widget for password input with bigger font and width
password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=35, bg="lightyellow", bd=5)
password_entry.pack(pady=15)

# Button to check the password strength with a bigger font and size
check_button = tk.Button(root, text="Check Password Strength", font=("Arial", 14), command=on_check_button_click, bg="lightgreen", width=20, height=2)
check_button.pack(pady=20)

# Label to display the result with bigger font and color changes
result_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="lightblue")
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
