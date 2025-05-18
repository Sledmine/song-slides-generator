from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.dml.color import RGBColor

def parse_chord_lyrics_file(filename):
    slides = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f if line.strip()]
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                chords = lines[i]
                lyrics = lines[i + 1]
                slides.append((chords, lyrics))
    return slides

def create_ppt(slides, output_file="output.pptx"):
    prs = Presentation()
    blank_slide_layout = prs.slide_layouts[6]  # blank

    for chords, lyrics in slides:
        slide = prs.slides.add_slide(blank_slide_layout)
        left = Inches(1)
        top = Inches(2)
        width = Inches(8)
        height = Inches(1)

        textbox = slide.shapes.add_textbox(left, top, width, height)
        tf = textbox.text_frame
        p = tf.paragraphs[0]

        run = p.add_run()
        run.text = chords + "\n"
        run.font.bold = True
        run.font.size = Pt(24)
        run.font.color.rgb = RGBColor(0x42, 0x24, 0xE9)  # blue

        run2 = p.add_run()
        run2.text = lyrics
        run2.font.size = Pt(24)

    prs.save(output_file)
    print(f"Presentation saved as {output_file}")

# Usage:
slides = parse_chord_lyrics_file("song.txt")
create_ppt(slides)
