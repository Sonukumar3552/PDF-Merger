# PDF-Merger
A simple desktop PDF toolbox built with Python and Tkinter. Features PDF merging, PDF to image conversion, and image to PDF conversion in a clean GUI.
# PDF Toolbox (Python + Tkinter)

A simple desktop **PDF toolbox** built with Python and Tkinter.

##  Features

-  Merge multiple PDF files into a single PDF  
-  Convert **PDF ➜ Images** (each page as PNG)  
-  Convert **Images ➜ PDF** (combine images into one PDF)  
- Simple and clean GUI using `tkinter`  
- Works offline on Windows

##  Tech Stack

- Python 3
- Tkinter (GUI)
- PyPDF2
- Pillow (PIL)
- PyMuPDF (`fitz`)

##  How to Run

```bash
pip install PyPDF2 pillow pymupdf
python pdf_toolbox.py
 Build EXE (Windows)
bash
Copy code
python -m PyInstaller --onefile --noconsole pdf_toolbox.py
The generated .exe will be in the dist/ folder.

sql
Copy code

Then:

```powershell
git add README.md
git commit -m "Add README with project details"
git push
