#!/usr/bin/env python3
"""
Convert MTUS text files to professionally formatted PDFs
Fixed version with proper text wrapping
"""

import os
import sys
import re
from pathlib import Path

from fpdf import FPDF


class MTUSPDF(FPDF):
    def __init__(self):
        super().__init__(unit='mm', format='Letter')
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(20, 20, 20)  # left, top, right
        self.content_width = self.w - self.l_margin - self.r_margin
        
    def header(self):
        if self.page_no() > 1:
            self.set_y(12)
            self.set_font('helvetica', 'I', 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, 'MTUS Constitutional Analysis Project', align='C')
            self.ln(3)
            self.set_draw_color(180, 180, 180)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        
    def footer(self):
        self.set_y(-12)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, f'Page {self.page_no()}', align='C')
        
    def add_title_page(self, title, subtitle=None):
        self.add_page()
        self.set_y(60)
        
        # Main title
        self.set_font('helvetica', 'B', 20)
        self.set_text_color(0, 51, 102)
        
        # Center text wrapping for title
        self.set_x(self.l_margin)
        self.multi_cell(0, 10, title, align='C')
            
        if subtitle:
            self.ln(8)
            self.set_font('helvetica', 'I', 12)
            self.set_text_color(80, 80, 80)
            self.set_x(self.l_margin)
            self.multi_cell(0, 7, subtitle, align='C')
                
        self.ln(30)
        
        # Decorative line
        self.set_draw_color(0, 51, 102)
        self.set_line_width(0.5)
        line_y = self.get_y()
        center_x = self.w / 2
        self.line(center_x - 40, line_y, center_x + 40, line_y)
        
        self.ln(25)
        self.set_font('helvetica', '', 10)
        self.set_text_color(100, 100, 100)
        self.set_x(self.l_margin)
        self.cell(0, 8, 'MTUS Constitutional Analysis Project', align='C')
        self.ln(6)
        self.set_x(self.l_margin)
        self.cell(0, 8, 'Personal Research Initiative', align='C')
        self.ln(6)
        self.set_x(self.l_margin)
        self.cell(0, 8, 'February 2026', align='C')


def clean_markdown(text):
    """Remove markdown formatting"""
    # Remove bold
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    # Remove italic
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    return text


def convert_txt_to_pdf(input_file, output_file):
    """Convert a text/markdown file to PDF"""
    print(f"Converting: {input_file.name}")
    
    pdf = MTUSPDF()
    
    # Read content
    content = input_file.read_text(encoding='utf-8', errors='ignore')
    # Remove problematic Unicode characters but keep basic ASCII
    content = content.encode('ascii', 'ignore').decode('ascii')
    lines = content.split('\n')
    
    # Extract title from first heading
    title = "MTUS Analysis Document"
    subtitle = None
    
    for line in lines[:20]:
        if line.startswith('# '):
            title = clean_markdown(line[2:].strip())
            break
        elif line.startswith('## ') and not subtitle:
            subtitle = clean_markdown(line[3:].strip())
            
    # Add title page
    pdf.add_title_page(title, subtitle)
    
    # Add content pages
    pdf.add_page()
    
    in_bullet_list = False
    bullet_items = []
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Skip empty lines at start of content page
        if i == 0 and not line.strip():
            i += 1
            continue
            
        # Horizontal rule
        if line.strip() == '---':
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.ln(4)
            pdf.set_draw_color(150, 150, 150)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue
            
        # Headers - use multi_cell with width=0 for full width
        if line.startswith('# '):
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.set_font('helvetica', 'B', 16)
            pdf.set_text_color(0, 51, 102)
            pdf.ln(6)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 8, clean_markdown(line[2:].strip()))
            pdf.ln(2)
            i += 1
            continue
            
        if line.startswith('## '):
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.set_font('helvetica', 'B', 13)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(5)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 7, clean_markdown(line[3:].strip()))
            pdf.ln(2)
            i += 1
            continue
            
        if line.startswith('### '):
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.set_font('helvetica', 'B', 11)
            pdf.set_text_color(40, 40, 40)
            pdf.ln(4)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 6, clean_markdown(line[4:].strip()))
            pdf.ln(2)
            i += 1
            continue
            
        if line.startswith('#### '):
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.set_font('helvetica', 'B', 10)
            pdf.set_text_color(60, 60, 60)
            pdf.ln(3)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 5, clean_markdown(line[5:].strip()))
            pdf.ln(1)
            i += 1
            continue
            
        # Handle bullet points
        stripped = line.strip()
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_bullet_list:
                in_bullet_list = True
            bullet_items.append(stripped[2:])
            i += 1
            continue
        elif in_bullet_list and stripped.startswith('  ') and stripped:
            # Continuation of bullet
            bullet_items[-1] += ' ' + stripped.strip()
            i += 1
            continue
        elif in_bullet_list and stripped and not stripped.startswith('- ') and not stripped.startswith('* '):
            # End of bullet list
            render_bullet_list(pdf, bullet_items)
            bullet_items = []
            in_bullet_list = False
            
        # Handle empty lines
        if not stripped:
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            pdf.ln(3)
            i += 1
            continue
            
        # Skip table separator lines
        if stripped.startswith('|') and '---' in stripped:
            i += 1
            continue
            
        # Handle table rows
        if stripped.startswith('|'):
            if in_bullet_list:
                render_bullet_list(pdf, bullet_items)
                bullet_items = []
                in_bullet_list = False
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if cells:
                pdf.set_font('helvetica', '', 9)
                pdf.set_text_color(0, 0, 0)
                table_text = '  |  '.join(clean_markdown(c) for c in cells if c)
                pdf.set_x(pdf.l_margin)
                pdf.multi_cell(0, 5, table_text)
            i += 1
            continue
            
        # Regular paragraph
        if in_bullet_list:
            render_bullet_list(pdf, bullet_items)
            bullet_items = []
            in_bullet_list = False
            
        pdf.set_font('helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        
        cleaned = clean_markdown(line)
        if cleaned.strip():
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 5, cleaned)
            
        i += 1
        
    # Render any remaining bullets
    if in_bullet_list:
        render_bullet_list(pdf, bullet_items)
        
    # Add disclaimer page at end
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 14)
    pdf.set_text_color(180, 0, 0)
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, 'LEGAL DISCLAIMER', align='C')
    pdf.ln(12)
    
    pdf.set_font('helvetica', '', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_x(pdf.l_margin)
    disclaimer = """This document contains personal opinions, analysis, and commentary only. Nothing herein constitutes legal advice, factual allegations, or definitive claims about any person, organization, or government entity.

The content is for informational and educational purposes only. Consult a qualified attorney for legal advice specific to your situation.

This research was conducted using AI-assisted tools. While every effort has been made to ensure accuracy, AI systems can make errors. The author welcomes corrections and fact-checking.

All statements regarding ACOEM, MTUS, or other organizations are expressions of opinion and analytical commentary, not statements of objective fact. No false statements of fact are made about any person or organization.

This document is protected under the First Amendment and California Code of Civil Procedure Section 425.16 (anti-SLAPP statute).

Copyright 2026 MTUS Constitutional Analysis Project. Personal Research Initiative."""
    
    pdf.multi_cell(0, 5, disclaimer)
    
    # Save PDF
    pdf.output(str(output_file))
    print(f"  Created: {output_file}")
    return True


def render_bullet_list(pdf, items):
    """Render a list of bullet points"""
    pdf.set_font('helvetica', '', 10)
    pdf.set_text_color(0, 0, 0)
    
    for item in items:
        cleaned = clean_markdown(item)
        # Draw bullet
        pdf.set_x(pdf.l_margin + 5)
        pdf.cell(4, 5, '-', new_x="RIGHT")
        # Content with wrap - use 0 width for auto to right margin
        pdf.multi_cell(0, 5, cleaned)
        pdf.ln(1)


def main():
    docs_dir = Path('/home/d/.openclaw/workspace/mtus-advocacy-site/docs')
    
    # Files to convert
    files_to_convert = [
        'MTUS_CONSTITUTIONAL_VIOLATION_MASTER_REPORT.txt',
        'MTUS_14TH_AMENDMENT_LEGAL_ARGUMENTS.txt',
        'MTUS_MASTER_EXECUTIVE_SUMMARY_ALL_17_GUIDELINES.txt',
        'ACOEM-Cervical-and-Thoracic-Spine-Guideline.txt',
        'Shoulder-Disorders-Guideline.txt',
        'Elbow-Disorders-Guideline.txt',
        'Hand-Wrist-Forearm-Disorders-Guideline.txt',
        'SUPPLEMENTAL_CASE_LAW_ANALYSIS.txt',
        'SECOND_SUPPLEMENTAL_CASE_LAW_ANALYSIS.txt',
        'ADA_TIER1_CASE_LAW_ANALYSIS.txt',
        'COPYRIGHT_COMPLIANCE_NOTICE.txt',
    ]
    
    success_count = 0
    
    for filename in files_to_convert:
        input_path = docs_dir / filename
        if input_path.exists():
            output_path = docs_dir / filename.replace('.txt', '.pdf')
            try:
                if convert_txt_to_pdf(input_path, output_path):
                    success_count += 1
            except Exception as e:
                print(f"  Error converting {filename}: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"  Not found: {filename}")
            
    print(f"\n✓ Successfully created {success_count} PDFs")
    return success_count


if __name__ == '__main__':
    main()
