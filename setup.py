import sys
import os
from cx_Freeze import setup, Executable

files = ['assets','book_files','books_db.db']

exe = Executable(script = "app.py", base="Win32GUI")

setup (
    name="Books Management",
    version="1.0",
    description="application for managing you digital books",
    author="Aukan",
    options={'build_exe': {'include_files': files}},
    executables=[exe]
    
)