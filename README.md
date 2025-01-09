# Keylogger Detection Tool

This Python script is designed to assist in the detection of keyloggers by monitoring system activities. It lists all running processes along with their network connections and loaded modules, which can be manually inspected for suspicious behavior.

## Features

- **Process Listing**: Displays all running processes with their PID, name, and username.
- **Loaded Modules**: Lists all modules loaded by each process.
- **Network Connections**: Shows active network connections for each process.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. **Install Python**:
   - Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install `psutil`**:
   - Install the `psutil` library using pip:
     ```bash
     pip install psutil
     ```

## Usage

1. **Run the Script**:
   - Execute the script with administrative privileges to ensure access to all processes:
     ```bash
     sudo python keylogger_detection.py
     ```

2. **Review Output**:
   - The script will print details of all running processes, including their loaded modules and network connections. Manually inspect this output for any suspicious activity.

## Example Output

```
Listing all running processes with network connections and loaded modules.

Process: python3 (PID: 1234)
User: user
Loaded Modules:
  /usr/lib/python3.8/lib-dynload/_heapq.cpython-38-x86_64-linux-gnu.so
  /usr/lib/python3.8/lib-dynload/array.cpython-38-x86_64-linux-gnu.so
Network Connections:
  127.0.0.1:12345 -> 127.0.0.1:54321
----------------------------------------
Process: chrome (PID: 5678)
User: user
Loaded Modules:
  /opt/google/chrome/chrome
  /usr/lib/x86_64-linux-gnu/libnss3.so
Network Connections:
  192.168.1.2:443 -> 192.168.1.3:12345
----------------------------------------
```

## Limitations

- **Manual Inspection**: The script does not automatically detect keyloggers. It provides information that must be manually reviewed.
- **Permissions**: Some processes may not be accessible without elevated privileges.
- **Performance**: The script may cause system overhead when listing all processes and their details.

## Enhancements

- **Automated Anomaly Detection**: Implement algorithms to detect unusual patterns in process behavior.
- **Logging**: Save the output to a file for later analysis.
- **User Interface**: Develop a graphical interface for easier interaction.

## Disclaimer

This script is intended for educational purposes only. Ensure you have permission to monitor the system you are testing. The author is not responsible for any misuse of this tool.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository or contact the author directly.

---
