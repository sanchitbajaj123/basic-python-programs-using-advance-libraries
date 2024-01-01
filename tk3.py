from tksheet import Sheet
import tkinter as tk

app = tk.Tk()
app.grid_columnconfigure(0, weight = 1)
app.grid_rowconfigure(0, weight = 1)

main_frame = tk.Frame(app)
main_frame.grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 10)

entry = tk.Entry(main_frame)
entry.grid(row = 0, column = 0, sticky = "ew", padx = 10, pady = 10)

main_frame.grid_columnconfigure(0, weight = 1)
main_frame.grid_rowconfigure(1, weight = 1)

sheet = Sheet(main_frame,
              total_rows = 1200,
              total_columns = 30)
sheet.grid(row = 1, column = 0, sticky = "nswe", padx = 10, pady = 10)
app.mainloop()
