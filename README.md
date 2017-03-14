SVG2Solid.py is a script that reads an SVG file and extrudes all paths to
the specified thickness. Usage:

1. Open FreeCAD
2. In the python console, paste the script
3. In the python console, type in a call to extrudeSVG() with your SVG file and thickness, something like: `extrudeSVG(u"/path/to/file/design.svg", 4)`
4. Edit the resulting objects as required.

Tested with FreeCAD 0.16.
