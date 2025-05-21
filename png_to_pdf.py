#!/usr/bin/env python3
"""
png2pdf.py  –  Combine all PNG files in a folder into one PDF.

Usage:
    python png2pdf.py /path/to/folder output.pdf
"""

import sys
from pathlib import Path
from PIL import Image   # pip install pillow

def pngs_to_pdf(src_dir: Path, pdf_path: Path) -> None:
    # Collect *.png files, alphabetically
    png_paths = sorted(src_dir.glob("*.png"))
    if not png_paths:
        raise FileNotFoundError(f"No PNG files found in {src_dir}")

    # Open images and ensure RGB mode (PDF doesn't support RGBA)
    images = [Image.open(p).convert("RGB") for p in png_paths]

    # Write multi-page PDF
    images[0].save(
        pdf_path,
        save_all=True,
        append_images=images[1:],
        resolution=300,   # adjust DPI if needed
    )
    print(f"✅  Created {pdf_path} from {len(images)} PNG files.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python png2pdf.py <png_folder> <output.pdf>")
    src = Path(sys.argv[1]).expanduser().resolve()
    dst = Path(sys.argv[2]).expanduser().resolve()
    pngs_to_pdf(src, dst)

python /Users/lee/GitHub/image2PDF/png_to_pdf.py /Users/lee/Downloads/HitachiDT_Proposal /Users/lee/Downloads/HitachiDT_Proposal.pdf
