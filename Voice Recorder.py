import tkinter as tk
from tkinter import ttk
import pyaudio
import os
import wave

class VoiceRecorder:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder")
        master.geometry("400x200")
        self.create_widgets()
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False

    def create_widgets(self):
        self.record_button = ttk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_recording, state="disabled")
        self.stop_button.pack()

        self.save_button = ttk.Button(self.master, text="Save", command=self.save_recording, state="disabled")
        self.save_button.pack()

    def start_recording(self):
        if not self.recording:
            self.frames = []
            self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                                          frames_per_buffer=1024)
            self.record_button.config(state="disabled")
            self.stop_button.config(state="active")
            self.save_button.config(state="disabled")
            self.recording = True
            print("Recording...")

    def stop_recording(self):
        if self.recording:
            self.stream.stop_stream()
            self.stream.close()
            self.record_button.config(state="active")
            self.stop_button.config(state="disabled")
            self.save_button.config(state="active")
            self.recording = False
            print("Recording stopped")

    def save_recording(self):
        if len(self.frames) > 0:
            save_path = "recordings"
            os.makedirs(save_path, exist_ok=True)
            filename = os.path.join(save_path, "recording.wav")

            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b"".join(self.frames))
            wf.close()
            print(f"Recording saved as {filename}")
            self.frames = []


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorder(root)
    root.mainloop()




