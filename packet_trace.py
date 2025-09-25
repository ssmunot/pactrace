import time
import threading

class PacketTraceJob:
    def __init__(self, node_name, port, file_size, buffer_size, host_address, rolling, num_traces):
        self.node_name = node_name
        self.port = port
        self.file_size = file_size
        self.buffer_size = buffer_size
        self.host_address = host_address
        self.rolling = rolling
        self.num_traces = num_traces
        self.is_running = False
        self.thread = None

    def _run_trace(self):
        self.is_running = True
        # Simulate the process...
        try:
            for _ in range(30):  # Simulate running
                if not self.is_running:
                    break
                time.sleep(1)
        finally:
            self.is_running = False

    def start(self):
        self.thread = threading.Thread(target=self._run_trace)
        self.thread.start()

    def stop(self):
        self.is_running = False
        # Wait for the thread to stop
        if self.thread:
            self.thread.join()
