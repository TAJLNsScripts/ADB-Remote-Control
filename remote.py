import tkinter as tk
from ppadb.client import Client as AdbClient

class TVRemoteApp:
    def __init__(self, master):
        self.master = master
        master.title("TV Remote")

        self.screen_var = tk.StringVar()
        self.screen_var.set("")

        # Set background color
        master.configure(bg='#f0f0f0')

        self.create_widgets()
        
        self.master.rowconfigure(7, minsize=100)

    def create_widgets(self):
        # Screen widget to display button presses
        screen = tk.Entry(self.master, textvariable=self.screen_var, font=('Arial', 14), bd=5, insertwidth=4, width=20,
                          justify='right', bg='#e0e0e0')
        screen.grid(row=0, column=0, columnspan=3, pady=10)

        # Power button
        power_btn = tk.Button(self.master, text='Power', padx=15, pady=15, font=('Arial', 10),
                              command=lambda: self.button_click('177'), bg='#FF0000', fg='white',
                              activebackground='#d9534f')
        power_btn.grid(row=1, column=1, padx=5, pady=5)

        # Button grid
        buttons = [
            ('1', 2, 0, '145'), ('2', 2, 1, '146'), ('3', 2, 2, '147'),
            ('4', 3, 0, '148'), ('5', 3, 1, '149'), ('6', 3, 2, '150'),
            ('7', 4, 0, '151'), ('8', 4, 1, '152'), ('9', 4, 2, '153'),
                                ('0', 5, 1, '144'),
                                ('^', 7, 1, '19'),
            ('<', 8, 0, '21'), ('v', 8, 1, '20'), ('>', 8, 2, '22')
        ]

        for (text, row, col, value) in buttons:
            btn = tk.Button(self.master, text=text, padx=15, pady=15, font=('Arial', 10),
                            command=lambda t=value: self.button_click(t),
                            bg='#4CAF50', fg='white', activebackground='#45a049')
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Enter and Return buttons (centered)
        enter_btn = tk.Button(self.master, text='Enter', padx=15, pady=15, font=('Arial', 10),
                              command=lambda: self.button_click('66'), bg='#008CBA', fg='white',
                              activebackground='#007bb5')
        enter_btn.grid(row=9, column=0, padx=5, pady=5)

        return_btn = tk.Button(self.master, text='Return', padx=15, pady=15, font=('Arial', 10),
                               command=lambda: self.button_click('4'), bg='#008CBA', fg='white',
                               activebackground='#007bb5')
        return_btn.grid(row=9, column=2, padx=5, pady=5)

    def button_click(self, value):
        self.screen_var.set(value)
        device.shell('input keyevent ' + value)
        
try:        
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.devices()[0]
    print('Found device', device.serial)
except:
    print('Failed connection to device')

root = tk.Tk()
app = TVRemoteApp(root)
root.mainloop()
