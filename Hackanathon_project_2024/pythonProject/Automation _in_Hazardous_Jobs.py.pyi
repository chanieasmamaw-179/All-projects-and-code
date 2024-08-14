import time

class HazardousJobAutomation:
    def __init__(self):
        self.temperature_sensor = None
        self.gas_sensor = None
        self.machine_status = "OFF"

    def start_machine(self):
        print("Starting machine...")
        time.sleep(2)  # Simulate startup time
        self.machine_status = "ON"
        print("Machine is now ON")

    def stop_machine(self):
        print("Stopping machine...")
        time.sleep(1)  # Simulate shutdown time
        self.machine_status = "OFF"
        print("Machine is now OFF")

    def monitor_environment(self):
        if self.machine_status == "ON":
            self.temperature_sensor = self.measure_temperature()
            self.gas_sensor = self.detect_gas()
            print(f"Temperature: {self.temperature_sensor} °C")
            print(f"Gas level: {self.gas_sensor}")

    def measure_temperature(self):
        # Simulate temperature measurement (replace with actual sensor reading)
        return round(25 + (time.time() % 10), 2)

    def detect_gas(self):
        # Simulate gas detection (replace with actual sensor reading)
        if time.time() % 5 < 2:
            return "Safe"
        else:
            return "Dangerous"

# Example usage
if __name__ == "__main__":
    automation_system = HazardousJobAutomation()

    automation_system.start_machine()

    for _ in range(5):
        automation_system.monitor_environment()
        time.sleep(3)  # Simulate monitoring interval

    automation_system.stop_machine()
