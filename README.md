# Hiker-Rescue-Information-System
The Hiker Rescue Information System (HRIS) is a Python-based console application designed to help park rangers and rescue teams manage, filter, and view detailed records of hiker rescue missions on various trails. It supports:
Viewing a complete list of hiking trails
Viewing details of a specific trail
Viewing all rescue missions
Filtering rescue missions by multiple criteria
This project is structured to demonstrate core concepts in object-oriented programming, file I/O, and user interaction using Python and CSV data.
**Features**
**Menu Options**__
**View all trails**
Displays a formatted list of all available trails including location, elevation, difficulty, and natural features.
View a trail
Enter a trail name to view detailed info including station coordinates and features.
View all rescue missions
Displays all hiker rescue incidents from the provided CSV data.
View filtered rescue mission stats
Allows multi-field filtering using:
Incident ID
Hiker's First and Last Name (prefix search supported)
Trail Name (prefix search supported)
Criticality Level
Status (prefix search supported)

**📂 Files**
File Name	Description
HRIS.py	Main Python program
Hiker-Rescues.csv	CSV file containing rescue mission data

**🔧 Requirements**
Python 3.x installed
Hiker-Rescues-.csv in the same folder as your .py file

✨ Filtering Tips
Prefix Matching: You can enter partial names (e.g., Le to match Lee, Leon, etc.)
Case Insensitive: All text input is matched case-insensitively.
Optional Fields: Press Enter to skip any field during filtering.

🛠️ Implementation Highlights
Uses csv.reader() for loading rescue data
Uses multi-field filtering with .startswith() for flexible user input
Displays results in a clean, formatted console table
Safely handles blank or invalid inputs (e.g., empty criticality field)
