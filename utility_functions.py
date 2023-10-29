import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class UtilityFunctions:
    def __init__(self, audio_control):
        self.audioControl = audio_control

    def increase_frequency(self, e=None):
        self.audioControl.current_frequency += 1
        print(f"Frequency increased to {self.audioControl.current_frequency} Hz")
        logging.info(f"Frequency increased to {self.audioControl.current_frequency} Hz")

    def decrease_frequency(self, e=None):
        self.audioControl.current_frequency -= 1
        print(f"Frequency decreased to {self.audioControl.current_frequency} Hz")
        logging.info(f"Frequency decreased to {self.audioControl.current_frequency} Hz")

    def increase_frequency_small(self, e=None):
        self.audioControl.current_frequency += 0.1
        print(f"Frequency increased to {self.audioControl.current_frequency} Hz")
        logging.info(f"Frequency increased to {self.audioControl.current_frequency} Hz")

    def decrease_frequency_small(self, e=None):
        self.audioControl.current_frequency -= 0.1
        print(f"Frequency decreased to {self.audioControl.current_frequency} Hz")
        logging.info(f"Frequency decreased to {self.audioControl.current_frequency} Hz")

    def increase_amplitude(self, e=None):
        self.audioControl.current_amplitude += 5
        print(f"Amplitude increased to {self.audioControl.current_amplitude}")
        logging.info(f"Amplitude increased to {self.audioControl.current_amplitude}")

    def decrease_amplitude(self, e=None):
        self.audioControl.current_amplitude -= 5
        print(f"Amplitude decreased to {self.audioControl.current_amplitude}")
        logging.info(f"Amplitude decreased to {self.audioControl.current_amplitude}")

    def increase_wavelength(self, e=None):
        self.audioControl.current_frequency *= 1.5  # Increase frequency to decrease wavelength
        print(f"Wavelength increased, frequency adjusted to {self.audioControl.current_frequency} Hz")
        logging.info(f"Wavelength increased, frequency adjusted to {self.audioControl.current_frequency} Hz")

    def decrease_wavelength(self, e=None):
        self.audioControl.current_frequency /= 1.5  # Decrease frequency to increase wavelength
        print(f"Wavelength decreased, frequency adjusted to {self.audioControl.current_frequency} Hz")
        logging.info(f"Wavelength decreased, frequency adjusted to {self.audioControl.current_frequency} Hz")

    def set_square_wave(self, e=None):
        self.audioControl.current_wave_form = '1'
        print("Waveform set to Square Wave")
        logging.info("Waveform set to Square Wave")

    def set_sine_wave(self, e=None):
        self.audioControl.current_wave_form = '2'
        print("Waveform set to Sine Wave")
        logging.info("Waveform set to Sine Wave")

    def set_sawtooth_wave(self, e=None):
        self.audioControl.current_wave_form = '3'
        print("Waveform set to Sawtooth Wave")
        logging.info("Waveform set to Sawtooth Wave")

    def set_triangle_wave(self, e=None):
        self.audioControl.current_wave_form = '4'
        print("Waveform set to Triangle Wave")
        logging.info("Waveform set to Triangle Wave")

    def set_crossing_waves(self, e=None):
        self.audioControl.current_wave_form = '5'
        print("Waveform set to Two Crossing Waves")
        logging.info("Waveform set to Two Crossing Waves")
