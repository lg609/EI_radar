import sys
import os

if len(sys.argv) < 3:
    print("Usage: python doocs_wechat_converter.py <input.md> <output.html>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    final_html = f"<html><body><pre>{md_text}</pre></body></html>"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Successfully converted {input_file} to {output_file}")
except Exception as e:
    print(f"Error: {e}")
