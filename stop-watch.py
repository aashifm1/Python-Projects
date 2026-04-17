import tkinter as tk

class stopwatch:
    def __init__(self,root):
        self.root=root
        self.root.title("Stopwatch") # Title name
        self.running=False
        self.seconds=0
        self.label = tk.Label(root, text="00:00:00", font=("Arial", 40))
        self.label.pack(pady=20)
        
        # Buttons
        self.start_btn = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        self.reset_btn = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.running:
            self.seconds += 0.1
            m, s = divmod(int(self.seconds), 60)
            h, m = divmod(m, 60)
            self.label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = stopwatch(root)

    root.mainloop()
