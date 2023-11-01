import os
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AutoReloader(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".py"):
            print(f"Changes detected in {event.src_path}. Reloading...")
            self.restart_script()

    def restart_script(self):
        try:
            process.terminate()
        except NameError:
            pass
        process = subprocess.Popen([sys.executable, self.script])


if __name__ == "__main__":
    script = "PPM.py"  # Nome do seu arquivo principal (PPM.py)
    event_handler = AutoReloader(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    print(f"Watching for changes in {os.getcwd()}. Press Ctrl+C to exit.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
