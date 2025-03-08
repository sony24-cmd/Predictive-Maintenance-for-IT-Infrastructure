import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Sample Data Generation (Replace with your actual data source)
np.random.seed(42)
time_index = pd.date_range('2023-01-01', periods=1000, freq='H')
cpu_usage = np.random.normal(50, 10, 1000)
memory_usage = np.random.normal(60, 15, 1000)
network_traffic = np.random.normal(100, 20, 1000)
database_latency = np.random.normal(5, 1, 1000)
df = pd.DataFrame({
    'timestamp': time_index,
    'cpu_usage': cpu_usage,
    'memory_usage': memory_usage,
    'network_traffic': network_traffic,
    'database_latency': database_latency
})
df.set_index('timestamp', inplace=True)

# Add Anomaly Detection (using a simplified threshold example for visualization)
df['cpu_anomaly'] = df['cpu_usage'].apply(lambda x: 1 if abs(x - df['cpu_usage'].mean()) > 2 * df['cpu_usage'].std() else 0)
df['latency_anomaly'] = df['database_latency'].apply(lambda x: 1 if abs(x - df['database_latency'].mean()) > 2 * df['database_latency'].std() else 0)

# 1. Matplotlib: Time Series with Anomalies
def plot_time_series_matplotlib(df, column, anomaly_column):
    """Plots time series with anomalies using Matplotlib."""
    anomalies = df[df[anomaly_column] == 1]
    plt.figure(figsize=(12, 6))
    plt.plot(df[column], label=column)
    plt.scatter(anomalies.index, anomalies[column], color='red', label='Anomaly')
    plt.title(f'{column} Time Series with Anomalies (Matplotlib)')
    plt.legend()
    plt.show()

plot_time_series_matplotlib(df, 'cpu_usage', 'cpu_anomaly')

# 2. Seaborn: Distribution and Correlation
def plot_distribution_seaborn(df, column):
    """Plots distribution using Seaborn."""
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'{column} Distribution (Seaborn)')
    plt.show()

plot_distribution_seaborn(df, 'network_traffic')

def plot_correlation_seaborn(df, col1, col2):
    """Plots correlation using Seaborn."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=col1, y=col2, data=df)
    plt.title(f'{col1} vs {col2} (Seaborn)')
    plt.show()

plot_correlation_seaborn(df, 'cpu_usage', 'memory_usage')

# 3. Plotly: Interactive Time Series and Scatter Plots
def plot_time_series_plotly(df, column, anomaly_column):
    """Plots interactive time series with anomalies using Plotly."""
    fig = px.line(df, x=df.index, y=column, title=f'{column} Time Series (Plotly)')
    anomalies = df[df[anomaly_column] == 1]
    fig.add_trace(go.Scatter(x=anomalies.index, y=anomalies[column], mode='markers', marker=dict(color='red'), name='Anomaly'))
    fig.show()

plot_time_series_plotly(df, 'database_latency', 'latency_anomaly')

def plot_scatter_plotly(df, col1, col2):
    """Plots interactive scatter plot using Plotly."""
    fig = px.scatter(df, x=col1, y=col2, title=f'{col1} vs {col2} (Plotly)')
    fig.show()

plot_scatter_plotly(df, 'network_traffic', 'cpu_usage')

# 4. Plotly: Interactive Dashboard (Example)
def create_dashboard_plotly(df):
    """Creates a simple interactive dashboard using Plotly."""
    fig_cpu = px.line(df, x=df.index, y='cpu_usage', title='CPU Usage')
    fig_memory = px.line(df, x=df.index, y='memory_usage', title='Memory Usage')
    fig_network = px.line(df, x=df.index, y='network_traffic', title='Network Traffic')
    fig_latency = px.line(df, x=df.index, y='database_latency', title='Database Latency')

    from plotly.subplots import make_subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=('CPU Usage', 'Memory Usage', 'Network Traffic', 'Database Latency'))

    fig.add_trace(fig_cpu.data[0], row=1, col=1)
    fig.add_trace(fig_memory.data[0], row=1, col=2)
    fig.add_trace(fig_network.data[0], row=2, col=1)
    fig.add_trace(fig_latency.data[0], row=2, col=2)

    fig.update_layout(height=800, width=1200, title_text="IT Infrastructure Dashboard")
    fig.show()

create_dashboard_plotly(df)