import threading
import queue
import numpy as np
import sounddevice as sd
import keyboard
import tkinter as tk


class AudioControl:
    def __init__(self):
        self.SAMPLING_RATE = 44100  # callback
        self.BUFFER_SIZE = 1024  # Number of audio frames per buffer # callback
        self.data_queue = queue.Queue()  # thread-safe queue # callback
        self.audio_lock = threading.Lock()
        self.exit_audio = False
        self.exit_program = False  # Global flag to indicate when to exit the program
        self.current_frequency = 0  # Initial frequency
        self.phase = 0  # Phase accumulator
        self.current_wave_form = '2'
        self.current_amplitude = 1.0  # Initial amplitude
        self.current_wavelength = 1.0  # Initial wavelength (this will be used to adjust frequency)


    def start_new_stream(self, entry_widget):

        self.exit_audio = False  # Reset the exit flag
        self.set_freestyle_frequency(entry_widget)  # Set the new frequency
        print(f"Starting new stream with frequency {self.current_frequency}")
        threading.Thread(target=self.start_stream).start()  # Start a new thread for the audio stream

    def start_stream(self):
        with self.audio_lock:  # Acquire the lock
            if self.exit_audio or self.exit_program:  # Check if the audio or program should be stopped
                return
            self.exit_audio = False  # Reset the flag
            with sd.OutputStream(callback=self.callback, channels=1, samplerate=self.SAMPLING_RATE,
                                 blocksize=self.BUFFER_SIZE):
                while not self.exit_program:  # Keep running until exit_program is True
                    if keyboard.is_pressed('esc'):  # Check if 'esc' is pressed
                        break
                    sd.sleep(100)  # Sleep for a short duration to reduce CPU usage

    def callback(self, outdata, frames, time, status):

        if self.exit_audio:
            outdata[:, 0] = 0
            return sd.CallbackStop  # Stop the callback
        t = np.linspace(self.phase, self.phase + (frames / self.SAMPLING_RATE), frames, endpoint=False)

        if self.current_wave_form == '1':  # Square wave
            outdata[:, 0] = 0.5 * (1 + np.sign(np.sin(2 * np.pi * self.current_frequency * t)))
        elif self.current_wave_form == '2':  # Sine wave
            outdata[:, 0] = np.sin(2 * np.pi * self.current_frequency * t)
        elif self.current_wave_form == '3':  # Sawtooth wave
            outdata[:, 0] = 2.0 * (self.current_frequency * t % 1) - 1.0
        elif self.current_wave_form == '4':  # Triangle wave
            outdata[:, 0] = 4 * np.abs(t % 1 - 0.5) - 1
        elif self.current_wave_form == '5':  # Two crossing waves (sine and square)
            outdata[:, 0] = np.sin(2 * np.pi * self.current_frequency * t) + 0.5 * (
                    1 + np.sign(np.sin(2 * np.pi * (self.current_frequency / 2) * t)))

        self.phase += frames / self.SAMPLING_RATE
        self.phase %= 1.0  # Keep the phase between 0 and 1
        self.data_queue.put(outdata[:, 0])

    def on_escape(self, root, event=None):
        root.quit()  # This will break the Tkinter main loop

    def stop_audio(self, entry_widget):

        self.exit_audio = True  # Stop the current audio stream
        sd.stop()  # Stop the audio device
        entry_widget.delete(0, tk.END)  # Clear the Entry widget
        print("Audio stopped.")

    def on_exit(self, root):

        self.exit_program = True  # Set the flag to True
        self.exit_audio = True  # Also set the audio exit flag to True
        sd.stop()  # Stop the audio stream
        root.quit()  # Close the Tkinter window

    def set_freestyle_frequency(self, entry_widget):
        try:
            self.current_frequency = int(entry_widget.get())
            print(f"Freestyle frequency set to {self.current_frequency} Hz")

            self.exit_audio = False  # Reset the flag for the new audio stream
        except ValueError:
            print("Invalid input. Using the previous frequency.")
