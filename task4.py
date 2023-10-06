# task 4
# Voice Recorder Submitted by Bisma Sheikh

import tkinter as tk
import pyaudio
import wave
import os


class VoiceRecorder:
    def __init__(self, master):
        self.master = master
        self.frames = []
        self.is_recording = False
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.p = pyaudio.PyAudio()

        self.record_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack(pady=10)

    def start_recording(self):
        self.is_recording = True
        self.frames = []
        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.fs,
                                  frames_per_buffer=self.chunk,
                                  input=True)
        print("Recording...")
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
            self.master.update()

    def stop_recording(self):
        self.is_recording = False
        print("Recording stopped.")
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        self.save_recording()

    def save_recording(self):
        file_name = "recording.wav"
        wave_file = wave.open(file_name, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.p.get_sample_size(self.sample_format))
        wave_file.setframerate(self.fs)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()
        print(f"Recording saved as {file_name}")

        # Optional: Open the saved recording
        os.system(f"start {file_name}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Voice Recorder")
    app = VoiceRecorder(root)
    root.mainloop()
