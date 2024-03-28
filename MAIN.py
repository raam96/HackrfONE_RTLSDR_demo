import tkinter as tk
from subprocess import Popen

# Mapping between button names and Python file names
program_mapping = {
    "NBFM RECEIVER": "nfbm_rx.py",
    "NBFM TRANSMITTER": "nfm_tx.py",
    "WBFM RECEIVER": "wfm_rx.py",
    "WBFM TRANSMITTER": "wbfm_tx.py",
    "ASK RECEIVER": "ASK_RX.py",
    "ASK TRANSMITTER": "ASK_TX.py",
    "FSK RECEIVER": "FSK_RX.py",
    "FSK TRANSMITTER": "FSK_TX.py",
    "QPSK RECEIVER": "qpsk_rx.py",
    "QPSK TRANSMITTER": "QPSK_TX.py",
    "SSB LSB RECEIVER": "SSB_LSB_RX.py",
    "SSB LSB TRANSMITTER": "SSB_LSB_TX.py",
    "SSB USB RECEIVER": "SSB_USB_RX.py",
    "SSB USB TRANSMITTER": "SSB_USB_TX.py",

}

def run_program(program_path):
    process = Popen(["python", program_path])

def on_button_click(button_name):
    program_path = program_mapping.get(button_name)
    if program_path:
        run_program(program_path)

def create_gui():
    root = tk.Tk()
    root.title("HACKRF RTL SDR DEMO")
    root.configure(bg="blue")

    # Maximize the window
    root.state('zoomed')

    # Center align the heading
    heading_label = tk.Label(root, text="HACKRF RTL SDR DEMO", font=("Helvetica", 20), bg="blue",fg="yellow")
    heading_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='nsew')

    # List of your buttons
    button_names = ["NBFM RECEIVER", "NBFM TRANSMITTER", "WBFM RECEIVER", "WBFM TRANSMITTER", "ASK RECEIVER",
                    "ASK TRANSMITTER", "FSK RECEIVER", "FSK TRANSMITTER", "QPSK RECEIVER", "QPSK TRANSMITTER",
                    "SSB LSB RECEIVER","SSB LSB TRANSMITTER","SSB USB RECEIVER","SSB USB TRANSMITTER"]

    # Center align the buttons in two columns
    for i, button_name in enumerate(button_names):
        row = i // 2 + 1
        col = i % 2
        button = tk.Button(root, text=button_name, command=lambda name=button_name: on_button_click(name), height=2, width=20, font=("Helvetica", 15),fg="white", bg="green")
        button.grid(row=row, column=col, pady=10, padx=15, sticky='nsew')

    # Developer information and copyright notice
    developer_label = tk.Label(root, text="Developed by Lt NPH Raam Copyright © 2024, All rights reserved\nLicensed under GNU License", font=("Helvetica", 12), fg="yellow",bg="blue")
    developer_label.grid(row=len(button_names)//2 + 1, column=0, columnspan=2, pady=10)

    # Configure rows and columns to expand proportionally
    for i in range(len(button_names)//2 + 2):  # Number of rows
        root.grid_rowconfigure(i, weight=1)
    for i in range(2):  # Number of columns
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
