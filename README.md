# Emergency Dispatcher Console App

This is a Python console-based application to help emergency coordinators manage incidents and allocate resources smartly and fairly.

## Features

- Log and view emergency incidents
- Track available resources (ambulance, fire trucks, etc.)
- Allocate resources based on priority
- Reallocate from low-priority to high-priority incidents
- Timestamped logs for tracking

## Run the App

```bash
python main.py
```

## Run Unit Tests

```bash
python -m unittest discover tests
```

## Project Structure

- `incident.py` – Handles incident data
- `resources.py` – Manages resource objects
- `dispatcher.py` – Core logic for assigning/reallocating
- `main.py` – Console interface
- `tests/` – Unit tests for classes
