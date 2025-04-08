# Temperature Converter with a Python Script

## User Documentation

### Overview

The `if1_video_extra` project provides a Python-based tool to convert temperatures from Celsius to Fahrenheit. This guide will help you set up and run the converter on your local machine.

### Prerequisites

Before you begin, make sure the following are installed:

- **Python 3.x**
- **FFmpeg**

### Installation Steps

1. Install Python 3.x

   - Windows: Download from [python.org](https://www.python.org/downloads/windows/)
   - macOS: Download from [python.org](https://www.python.org/downloads/mac-osx/)

   After downloading, run the installer and follow the on-screen instructions. Make sure to tick the box that says "Add Python to PATH" during installation.

### 🔧 How to Use This Converter

- Open a terminal or command prompt.
- Navigate to the folder where you saved the file.
- Run the script by typing:

```bash
python3 temp.py
```

You should have the following dialogue:

```text
Enter temperature in Celsius: 0
0.0°C is equal to 32.00°F
```

## Technical Documentation

### Project Structure

```
if1_video_extra/
├── temp.py           # Main script for temperature conversion
├── test_temp.py      # Unit tests for the conversion function
├── requirements.txt  # (empty or not needed for now)
```

### temp.py

This script defines and runs a Celsius-to-Fahrenheit converter. It includes:

- A function `celsius_to_far(celsius_temp)` that uses the formula:
  ```
  Fahrenheit = Celsius × 9/5 + 32
  ```
- A prompt for user input using `input()`
- Conversion of that input into a float
- Error handling using `try/except` to catch invalid (non-numeric) inputs

### test_temp.py

This file contains unit tests for the converter function using the `unittest` module. It includes tests for:

- Valid numeric conversions
- Edge cases like 0°C
- Exception handling for invalid input types (if added later)

### Dependencies

- The script uses only Python’s built-in libraries: `unittest` and `input()`.
- No external packages or installations are required.