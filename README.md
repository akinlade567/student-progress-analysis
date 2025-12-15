# student-progress-analysis
This Python script, mymain.py, implements a comprehensive student data management and analysis tool, fulfilling the requirements for the Python Fundamentals Project 1 (GSE301). It showcases practical application of Python's core data structures, control flow mechanisms, and advanced features like pattern matching.
Data Organization and Structure
Initialization: The script begins by defining foundational student attributes (name, matric number, age, CGPA, etc.) using various Python data types: string, int, float, boolean, list, and dictionary.

Bulk Storage: Data for a minimum of five mock students are stored efficiently using a List of Dictionaries, where each dictionary represents a complete student profile.

Specialized Structures: A Set is generated to ensure a collection of unique course codes for the department, and a Tuple is used for fixed department details.

Core Processing and Logic
Grading System: A dual-function system is established to process scores:

Grade Assignment: Uses standard IF-ELIF-ELSE branching to convert numerical scores into letter grades (A-F).

Feedback Generation: Leverages the modern MATCH CASE statement to provide specific qualitative feedback based on the assigned letter grade.

Input Handling: A robust function employs TRY EXCEPT to manage potential errors during user input, ensuring that age and CGPA inputs are numeric and fall within valid ranges before casting them to their correct types (int and float).

Data Analysis Features
List Manipulation: Demonstrates advanced list handling through slicing (e.g., retrieving the top three scores, the final five scores using negative indexing, and selecting every other score using step indexing).

Group Analysis (Sets): Utilizes set operations (union, intersection, difference) to easily identify relationships between different student groups, such as finding students who both passed a specific course and qualified for academic merit.

User Interface and Management
Console Menu: The script features an interactive console menu driven by a persistent while loop and controlled by MATCH CASE, allowing users to perform management tasks seamlessly.

Graduation Eligibility Check: A dedicated function uses logical operators (and) to verify complex graduation criteria (minimum CGPA, no outstanding courses, and active status) and returns a detailed status message.

Advanced Concepts (Optional Tasks)
Nested Data Aggregation: Processes a nested dictionary containing students and their course scores to calculate the average score for each student and identify high-performing students who exceeded a minimum threshold in all subjects.

Type Identification: Includes a function that uses MATCH CASE to perform type pattern matching, accurately identifying the input data type (int, str, list, dict, etc.) and returning a formatted descriptive summary.
