import time
import random
import threading
from datetime import datetime

# --- Hypothetical Data Sources and Libraries ---
class InfrastructureData:
    def get_server_metrics(self, server_id):
        return {
            "cpu_usage": random.uniform(10, 95),
            "memory_usage": random.uniform(20, 90),
            "disk_io": random.uniform(5, 80),
            "network_traffic": random.uniform(100, 1000),
        }

    def get_database_metrics(self, db_cluster_id):
        return {
            "query_latency": random.uniform(1, 100),
            "active_connections": random.randint(50, 500),
        }

class AnomalyDetector:
    def detect_cpu_anomaly(self, cpu_usage):
        if cpu_usage > 90:
            return "High CPU Usage Alert", 95, "high"
        return None

    def detect_latency_anomaly(self, latency):
        if latency > 80:
            return "High Latency Alert", 90, "critical"
        return None

    def predict_disk_failure(self, disk_io):
        if disk_io > 70:
            if random.random() < 0.2:  # 20% chance of prediction.
                return "Predicted Disk Failure", 98, "critical"
        return None

# --- Visualization (Simplified) ---
class Visualization:
    def __init__(self):
        self.server_status = {}  # Initialize as a dictionary
        self.db_status = {}  # Initialize for database statuses
        self.alerts = []  # Initialize alerts as an empty list

    def update_server_status(self, server_id, status):
        self.server_status[server_id] = status

    def update_db_status(self, db_id, metrics):
        latency = metrics["query_latency"]
        if latency > 80:
            status = "red"
        elif latency > 60:
            status = "yellow"
        else:
            status = "green"
        self.db_status[db_id] = status
        print(f"DB {db_id} status: {status}")

    def add_alert(self, message, severity, timestamp):
        self.alerts.append({"message": message, "severity": severity, "timestamp": timestamp})

# --- Customizable Dashboard (Simplified) ---
class Dashboard:
    def __init__(self, visualization):
        self.visualization = visualization
        self.widgets = []  # Store widgets in a list
    
    def add_widget(self, widget):
        self.widgets.append(widget)
        print(f"Widget '{widget}' added to the dashboard.")

    def display(self):
        print("\n--- Dashboard View ---")
        print(f"Server Status: {self.visualization.server_status}")
        print(f"DB Status: {self.visualization.db_status}")
        print(f"Alerts: {self.visualization.alerts}\n")

# --- Main Program ---
def main():
    data_source = InfrastructureData()
    anomaly_detector = AnomalyDetector()
    visualization = Visualization()
    dashboard = Dashboard(visualization)

    dashboard.add_widget("server_status")
    dashboard.add_widget("db_status")
    dashboard.add_widget("alerts")

    servers = ["SRV-001", "SRV-002", "SRV-003"]
    databases = ["DB-Cluster-01", "DB-Cluster-02"]

    def monitor():
        while True:
            for server in servers:
                metrics = data_source.get_server_metrics(server)
                visualization.update_server_status(server, metrics)

                anomaly = anomaly_detector.detect_cpu_anomaly(metrics["cpu_usage"])
                prediction = anomaly_detector.predict_disk_failure(metrics["disk_io"])

                if anomaly:
                    visualization.add_alert(anomaly[0], anomaly[2], datetime.now())
                if prediction:
                    visualization.add_alert(prediction[0], prediction[2], datetime.now())

            for db in databases:
                metrics = data_source.get_database_metrics(db)
                visualization.update_db_status(db, metrics)

                anomaly = anomaly_detector.detect_latency_anomaly(metrics["query_latency"])
                if anomaly:
                    visualization.add_alert(anomaly[0], anomaly[2], datetime.now())

            dashboard.display()
            time.sleep(2)

    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.daemon = True  # Allow program to exit even if thread is running
    monitor_thread.start()

    try:
        while True:
            time.sleep(1)  # Keeps main thread alive.
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
