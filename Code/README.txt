--------// Raspberry Pi Rubik's Cube Solver //----------

Below are the instructions on using the Rubik's Cube Solving Robot. 
The motors should be connected to their corresponding drivers which in turn should be connected to the correct GPIO pins.

From Top to Bottom (Breadboard Oriented with 24V Power in Top Right) the drivers correspond as:
1st Driver - Up Motor (Yellow Face)   - Step Pin: 27, Direction Pin: 22
2nd Driver - Back Motor (Orange Face) - Step Pin: 23, Direction Pin: 24
3rd Driver - Right Motor (Green Face) - Step Pin: 12, Direction Pin: 16
4th Driver - Left Motor (Blue Face)   - Step Pin: 5,  Direction Pin: 6
5th Driver - Front Motor (Red Face)   - Step Pin: 19, Direction Pin: 26
6th Driver - Down Motor (White Face)  - Step Pin: 20, Direction Pin: 21


INSTRUCTIONS.
1 - Unzip files into chosen folder
2 - Open 2 Tabs in Terminal.
3 - In both tabs, Navigate to Directory of the unzipped Python Files.
4 - In first terminal tab, Run 'Python ClientGui.py' and wait for it to open.
5 - Set HOST to 'localhost' and set PORT to '8080'
6 - Input net of cube into the GUI
7 - In second terminal tab, Run 'Python RubiksSolver.py'
8 - Wait until terminal reads 'Waiting for Solved String...'
9 - Turn on power to the Motors.
10 - In GUI click 'Solve' button.
11 - Wait until all motors stop moving.
12 - Cube is Solved :)


Cían Winder
cian.winder.2022@mumail.ie
cjiwinder2@gmail.com
21424916