import tkinter as tk
import time
import threading
import sys
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller as KeyboardController

class MicroScroll:
    def __init__(self):
        self.scrolling = False
        self.scroll_interval = 0.5  # 2 scrolls/segundo
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = KeyboardController()
        
        # Ventana mini
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.geometry("30x30+100+100")
        self.root.configure(bg='black')
        
        try:
            self.root.attributes('-transparentcolor', 'black')
        except:
            pass
        
        self.offset_x = 0
        self.offset_y = 0
        
        # Canvas circular
        self.canvas = tk.Canvas(
            self.root,
            width=30,
            height=30,
            bg='black',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Círculo
        self.circle = self.canvas.create_oval(
            2, 2, 28, 28,
            fill='#2a2a2a',
            outline='#00ff00',
            width=2
        )
        
        # Punto central
        self.dot = self.canvas.create_oval(
            12, 12, 18, 18,
            fill='#ff0000',
            outline=''
        )
        
        # Bindings
        self.canvas.bind('<Button-1>', self.on_left_click)
        self.canvas.bind('<Button-3>', lambda e: self.close())
        self.canvas.bind('<B1-Motion>', self.drag_window)
        
        self.setup_keyboard()
        
    def on_left_click(self, event):
        self.offset_x = event.x_root - self.root.winfo_x()
        self.offset_y = event.y_root - self.root.winfo_y()
        self.toggle()
        
    def drag_window(self, event):
        x = event.x_root - self.offset_x
        y = event.y_root - self.offset_y
        self.root.geometry(f'+{x}+{y}')
        
    def setup_keyboard(self):
        def on_press(key):
            try:
                # Solo la tecla C para toggle
                if hasattr(key, 'char') and key.char == 'c':
                    self.toggle()
            except:
                pass
        
        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()
    
    def close(self):
        self.scrolling = False
        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass
        sys.exit(0)
        
    def toggle(self):
        self.scrolling = not self.scrolling
        if self.scrolling:
            self.canvas.itemconfig(self.circle, fill='#1a4a1a', outline='#00ff00')
            self.canvas.itemconfig(self.dot, fill='#00ff00')
            threading.Thread(target=self.scroll_loop, daemon=True).start()
        else:
            self.canvas.itemconfig(self.circle, fill='#2a2a2a', outline='#00ff00')
            self.canvas.itemconfig(self.dot, fill='#ff0000')
            
    def scroll_loop(self):
        up = True
        while self.scrolling:
            self.keyboard_controller.press(Key.shift)
            self.mouse_controller.scroll(0, 1 if up else -1)
            self.keyboard_controller.release(Key.shift)
            
            up = not up
            time.sleep(self.scroll_interval)
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MicroScroll().run()