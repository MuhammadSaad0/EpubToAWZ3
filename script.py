import subprocess
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 convert.py <input_file.epub>")
    sys.exit(1)

input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print(f"Error: '{input_file}' does not exist.")
    sys.exit(1)

base, _ = os.path.splitext(input_file)
output_file = base + ".azw3"

try:
    subprocess.run(["ebook-convert", input_file, output_file], check=True)
    print(f"Converted: {input_file} → {output_file}")
except subprocess.CalledProcessError as e:
    print("Conversion failed.")
    sys.exit(1)
