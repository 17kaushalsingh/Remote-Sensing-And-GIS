import json
import sys
from pathlib import Path
import nbconvert
import markdown


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      color: #1f2937;
      background: #ffffff;
    }}
    img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 16px auto;
    }}
    pre, code {{
      background: #f3f4f6;
    }}
    pre {{
      padding: 12px;
      overflow-x: auto;
      border-radius: 8px;
    }}
    code {{
      padding: 2px 4px;
      border-radius: 4px;
    }}
    h1, h2, h3, h4, h5, h6 {{
      color: #111827;
    }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""

def ipynb_to_html(ipynb_path, output_path=None):
    """Convert Jupyter notebook to HTML file."""
    
    ipynb_file = Path(ipynb_path)
    
    if not ipynb_file.exists():
        print(f"Error: File {ipynb_path} not found")
        sys.exit(1)
    
    if output_path is None:
        output_path = ipynb_file.with_suffix('.html')
    
    try:
        # Try using nbconvert if available
        exporter = nbconvert.HTMLExporter()
        body, _ = exporter.from_filename(ipynb_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)
        
        print(f"Successfully converted {ipynb_path} to {output_path}")
        
    except ImportError:
        print("Error: nbconvert not installed. Install with: pip install nbconvert")
        sys.exit(1)


def md_to_html(md_path, output_path=None):
    """Convert Markdown file to HTML file."""

    md_file = Path(md_path)

    if not md_file.exists():
        print(f"Error: File {md_path} not found")
        sys.exit(1)

    if output_path is None:
        output_path = md_file.with_suffix('.html')

    text = md_file.read_text(encoding='utf-8')
    body = markdown.markdown(
        text,
        extensions=['extra', 'tables', 'fenced_code']
    )
    html = HTML_TEMPLATE.format(title=md_file.stem, body=body)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Successfully converted {md_path} to {output_path}")


def convert_to_html(input_path, output_path=None):
    input_file = Path(input_path)
    suffix = input_file.suffix.lower()

    if suffix == '.ipynb':
        ipynb_to_html(input_path, output_path)
    elif suffix == '.md':
        md_to_html(input_path, output_path)
    else:
        print(f"Error: Unsupported file type {suffix}. Use .ipynb or .md")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_to_html.py <input.ipynb|input.md> [output.html]")
        sys.exit(1)
    
    notebook_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_to_html(notebook_file, output_file)
