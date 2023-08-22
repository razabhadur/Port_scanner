# Port_scanner
# Port Scanner Tool

Welcome to the Port Scanner Tool project repository. This tool is designed to help you scan for open ports on a target host, allowing you to identify potential vulnerabilities and security risks.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contribution](#contribution)
- [Disclaimer](#disclaimer)
- [License](#license)

## Features

- **Port Scanning:** The tool employs asynchronous port scanning to quickly check for open ports on a specified target host.

- **Customizable Range:** You can define a range of ports to scan, allowing you to focus on specific ports or a broader spectrum.

- **Concurrent Scans:** The tool uses asynchronous programming to scan multiple ports concurrently, improving the scan speed.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository to your local machine.

   ```sh
   git clone https://github.com/your-username/port-scanner.git
Navigate to the project directory.
cd port-scanner
Install the required packages (if not already installed).

pip install asyncio
Usage
Run the port_scanner.py script using a Python interpreter.
python port_scanner.py
Follow the on-screen prompts to input the target IP address, start port, and end port to scan.

The tool will perform asynchronous port scans and display the open ports, if any.

Contribution
Contributions to this project are welcome! If you have ideas for improvements, found a bug, or want to add new features, feel free to submit pull requests.

Disclaimer
Please use this tool responsibly and only on systems you have explicit permission to scan. Unauthorized port scanning can be considered a violation of ethics and legality.

License
This project is licensed under the MIT License.
