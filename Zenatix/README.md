# IoT Temperature Monitoring System

## Overview

This project simulates an IoT-based temperature monitoring system using MQTT for data transmission, where an IoT device reads temperature data and publishes it to the cloud. The project consists of three main components:

1. **Publisher**: Simulates or reads actual temperature data and publishes it to an MQTT broker.
2. **Subscriber**: Subscribes to the temperature topic, checks for threshold violations, and raises an alarm if necessary.
3. **Server**: Provides an HTTP API to access the latest temperature data.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iot_temperature_monitor.git
   cd iot_temperature_monitor
