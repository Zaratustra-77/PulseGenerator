import tkinter as tk
from tkinter import ttk
import threading
from audio_control import AudioControl
from utility_functions import UtilityFunctions


class Ui:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.audio_control = AudioControl()
        self.root.title("Sound Generator")
        # style configuration
        self.style.configure('GreenText.TButton', foreground='green', font=('Arial', 15))
        self.style.configure('RedText.TButton', foreground='red', font=('Arial', 15))
        self.style.configure('OrangeText.TButton', foreground='orange', font=('Arial', 15))
        self.style.configure('BlueText.TButton', foreground='blue', font=('Arial', 15))
        self.style.configure('PurpleText.TButton', foreground='purple', font=('Arial', 15))
        self.style.configure('GreyText.TButton', foreground='grey', font=('Arial', 15))
        self.style.configure('PinkText.TButton', foreground='pink', font=('Arial', 15))
        self.style.configure('YellowText.TButton', foreground='yellow', font=('Arial', 15))
        # Row 0 col 0
        utilities = UtilityFunctions(self.audio_control)
        self.increase_frequency_button = ttk.Button(self.root, text="Increase freq by 1 Hz",
                                                    command=utilities.increase_frequency,
                                                    style='GreenText.TButton')
        self.increase_frequency_button.grid(row=0, column=0, sticky='nsew')
        # Row 0 col 1
        self.increase_increment_button = ttk.Button(self.root, text="Increase freq by 0.1 Hz",
                                                    command=utilities.increase_frequency_small,
                                                    style='GreenText.TButton')
        self.increase_increment_button.grid(row=0, column=1, sticky='nsew')
        # Row 0 col 2
        # self.increase_wavelength_button = ttk.Button(self.root, text="Increase Wavelength",
        #                                              command=utilities.increase_wavelength,
        #                                              style='GreenText.TButton')
        # self.increase_wavelength_button.grid(row=0, column=2, sticky='nsew')
        # Row 0 col 2
        self.increase_amplitude_button = ttk.Button(self.root, text="Increase amplitude",
                                                    command=utilities.increase_amplitude,
                                                    style='GreenText.TButton')
        self.increase_amplitude_button.grid(row=0, column=2, sticky='nsew')
        # Row 1 col 0
        self.decrease_frequency_button = ttk.Button(self.root, text="Decrease freq by 1 Hz ",
                                                    command=utilities.decrease_frequency,
                                                    style='RedText.TButton')
        self.decrease_frequency_button.grid(row=1, column=0, sticky='nsew')
        # Row 1 col 1
        self.decrease_increment_button = ttk.Button(self.root, text="Decrease freq by 0.1 Hz",
                                                    command=utilities.decrease_frequency_small,
                                                    style='RedText.TButton')
        self.decrease_increment_button.grid(row=1, column=1, sticky='nsew')
        # Row 1 col 2
        # self.decrease_wavelength_button = ttk.Button(self.root, text="Decrease Wavelength",
        #                                              command=utilities.decrease_wavelength,
        #                                              style='RedText.TButton')
        # self.decrease_wavelength_button.grid(row=1, column=2, sticky='nsew')
        # Row 1 col 2
        self.decrease_amplitude_button = ttk.Button(self.root, text="Decrease amplitude",
                                                     command=utilities.decrease_amplitude,
                                                     style='RedText.TButton')
        self.decrease_amplitude_button.grid(row=1, column=2, sticky='nsew')
        # Row 2 col 0
        self.square_wave_button = ttk.Button(self.root, text="Square Wave", command=utilities.set_square_wave,
                                             style='OrangeText.TButton')
        self.square_wave_button.grid(row=2, column=0, sticky='nsew')
        # Row 2 col 1
        self.sin_wave_button = ttk.Button(self.root, text="Sin Wave", command=utilities.set_sine_wave,
                                          style='OrangeText.TButton')
        self.sin_wave_button.grid(row=2, column=1, sticky='nsew')
        # Row 2 col 2
        self.sawtooth_wave_button = ttk.Button(self.root, text="Sawtooth Wave", command=utilities.set_sawtooth_wave,
                                               style='OrangeText.TButton')
        self.sawtooth_wave_button.grid(row=2, column=2, sticky='nsew')
        # Row 3 col 0
        self.triangle_wave_button = ttk.Button(self.root, text="Triangle Wave", command=utilities.set_triangle_wave,
                                               style='OrangeText.TButton')
        self.triangle_wave_button.grid(row=3, column=0, sticky='nsew')
        # Row 3 col 1
        self.crossing_wave_button = ttk.Button(self.root, text="Crossing Wave", command=utilities.set_crossing_waves,
                                               style='OrangeText.TButton')
        self.crossing_wave_button.grid(row=3, column=1, sticky='nsew')
        # Row 3 col 2
        self.root.bind('<Escape>', lambda event=None: self.audio_control.on_escape(self.root))
        self.stop_audio_button = ttk.Button(self.root, text="Stop Audio",
                                            command=lambda: self.audio_control.stop_audio(self.freestyle_entry),
                                            style='RedText.TButton')
        self.stop_audio_button.grid(row=3, column=2, sticky='nsew')
        # Row 4 col 0
        self.freestyle_label = ttk.Label(self.root, text="Freestyle Frequency (Hz):", style='GreenText.TButton')
        self.freestyle_label.grid(row=4, column=0, sticky='nsew')
        # Row 4 col 1
        self.freestyle_entry = ttk.Entry(self.root)
        self.freestyle_entry.grid(row=4, column=1, sticky='nsew')
        # Row 4 col 2
        self.submit_button = ttk.Button(self.root, text="Submit",
                                        command=lambda: self.audio_control.set_freestyle_frequency(
                                            self.freestyle_entry), style='BlueText.TButton')
        self.submit_button.grid(row=4, column=2, sticky='nsew')
        # Row 5 col 2
        self.exit_button = ttk.Button(self.root, text="* * * E x i t * * *",
                                      command=lambda: self.audio_control.on_exit(self.root),
                                      style='GreenText.TButton')
        self.exit_button.grid(row=5, column=2, sticky='nsew')
        # start the window
        threading.Thread(target=self.audio_control.start_stream).start()
        self.root.mainloop()


if __name__ == '__main__':
    Ui()
