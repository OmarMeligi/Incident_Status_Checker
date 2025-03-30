# Checker
# Incident and Event Status Management Scripts

## Overview
This project consists of two scripts designed to generate and manage incident and event records in CSV format. The first script (Python) generates three different files containing incident details, event mappings, and event statuses. The second script (Bash) checks and updates event statuses based on incident statuses.

## Features
- **Python Script:**
  - Generates three CSV files:
    1. `Tickets_Status.csv` - Contains incident numbers, statuses, and descriptions.
    2. `incident_Event.csv` - Maps incidents to unique event IDs.
    3. `Events_Status.csv` - Stores event statuses linked to event IDs.
  - Randomly assigns statuses (`Open` or `Closed`).
  - Ensures consistency by maintaining the same incident numbers across files.

- **Bash Script:**
  - Validates the existence of incidents and events.
  - Checks if an incident is `Closed` and updates the corresponding event status accordingly.
  - Creates a backup before modifying event statuses.
  - Provides clear debugging messages to track status changes.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Ensure you have **Python 3** installed for the Python script.
3. Ensure you have a Bash-compatible terminal for the Bash script.

## Usage
### **Step 1: Run the Python Script to Generate CSV Files**
```bash
python3 generate_data.py
```
- The script will prompt for filenames and generate:
  - `Tickets_Status.csv`
  - `incident_Event.csv`
  - `Events_Status.csv`
- It will also display the generated data in the terminal.

### **Step 2: Run the Bash Script to Validate and Update Events**
```bash
bash checker.sh
```
- Enter an **Incident Number** when prompted.
- The script will:
  - Check if the incident exists.
  - Validate the status of the related event.
  - Update the event status if necessary.

## Example Workflow
1. Run `generate_data.py` → Creates and fills CSV files.
2. Run `checker.sh` → Verifies and updates event statuses.

## Notes
- Ensure the CSV files are in the same directory as the scripts.
- The Bash script modifies `Events_Status.csv`, so a backup is created automatically.
- If the incident status is `Closed` but the event status isn’t updated, the script corrects it.

## Future Improvements
- Add logging for better tracking.
- Implement a GUI for easier interaction.
- Expand status categories beyond `Open` and `Closed`.

## License
This project is open-source and free to use.

