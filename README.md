# SystemView Keylogger

SystemView is a keylogger software designed to capture keystrokes and monitor user activities on Windows machines. Currently, the software captures keystrokes and snapshots at regular intervals, and sends the captured data securely via email to a Command-and-Control (C2) server. There are many planned future features to extend its functionality.

## Current Features

### Keylogger Functionality
- **Keystroke Capture**: The software records each keystroke made by the user along with a timestamp. All keystrokes are stored securely in an SQLite database for later review.
  
### Snapshot Capture
- **Snapshot Capture**: The software captures a snapshot of the user’s screen every 5 seconds. This periodic capture helps admins monitor user activity visually.
  
### Data Storage
- **SQLite Database**: Keystrokes and other data are stored in a local SQLite database to ensure easy retrieval and management.

### Data Upload via Email
- **ZIP File Creation**: The captured keystrokes and snapshots are compressed into a ZIP file.
- **Scheduled Email Upload**: The software is configured to send the compressed ZIP file to a Command-and-Control (C2) server via email on a scheduled basis. This ensures that admins can monitor the user’s activities remotely and securely.
  
### Data Management and Scheduling
- **Email Scheduling**: The software sends the ZIP file containing the captured keystrokes and snapshots at scheduled intervals (e.g., every hour or every day). This feature allows the administrator to collect data without manually retrieving it.

## Planned Future Features

While the current version of SystemView focuses on keylogging and snapshot capturing, we are planning to add several powerful features to expand its functionality. We welcome contributions from developers who are interested in helping us implement these features. Here’s a list of features that will be added in future updates:

### 1. **Live Preview & Remote Control**
- **Live Preview**: Admins will be able to view the user’s screen in real-time to monitor their activities.
- **Remote Control**: Admins can control the user’s machine remotely, performing tasks like clicking, typing, and navigating.

### 2. **Screen Recording**
- Admins will have the ability to record the user’s screen, capturing everything happening on the user’s desktop during the session.

### 3. **File Management**
- **Download User Files**: Admins will be able to download files from the user’s machine, gaining access to their data remotely.
- **Data Collection**: The system will be able to collect and store files, history, and other relevant data from the user's machine.

### 4. **Advanced History & Activity Management**
- **Program Usage History**: Track which programs the user has been using and how much time was spent on each program.
- **Browser History**: Collect and store the user’s browser history to track their internet usage.
- **Cookies**: Gather all cookies stored by the user on their browser for further analysis.

### 5. **Admin Control**
- **Start/Stop Features**: Admins will have the ability to start or stop specific features of the software, including keylogging, screen recording, and file collection.

### 6. **System Protection**
- The software will be designed to run on startup and cannot be easily copied, cut, renamed, or deleted by the user. This will prevent tampering with the monitoring process.

### 7. **Blocking Executable Files**
- **No Executables Allowed**: We plan to implement a feature that restricts the user from running any `.exe` files on their machine, ensuring that the user cannot execute unauthorized programs or malware.

## Contribution

We encourage contributions from developers who are interested in expanding the capabilities of this project. If you're interested in helping us implement the planned features, feel free to fork the repository, submit a pull request, or open an issue to discuss any new ideas.

To contribute, follow these steps:
1. Fork this repository.
2. Create a new branch.
3. Implement the feature or fix the bug.
4. Submit a pull request with a description of the changes.

### Future Contributors

We believe the planned features will significantly enhance the functionality of this keylogger. Developers who are familiar with Python, system monitoring, and security tools are especially welcome to help us implement the following planned additions:

- Live Preview & Remote Control (requires knowledge of remote desktop technologies).
- Screen Recording (integration with screen capture libraries).
- File Management and Remote Access (working with file transfer protocols).
- Activity Tracking (program usage and browser history).
- System Protection and Security Features (locking down the software to prevent user tampering).

### Acknowledgements

We would like to thank the open-source community for the many libraries and tools that make this project possible. Special thanks to contributors who will help us bring these features to life.

---

## Disclaimer

This software is currently being developed for educational and research purposes only. Unauthorized monitoring, keylogging, or remote control is illegal and unethical. Users should always obtain permission before deploying any monitoring software. The creators of this tool are not responsible for any misuse or legal consequences resulting from the use of this software.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
