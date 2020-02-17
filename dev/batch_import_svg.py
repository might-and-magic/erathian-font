# Batch Import SVG Individual Glyph Files into FontForge's Font File
# For Windows users, run C:\Program Files (x86)\FontForgeBuilds\fontforge-console.bat, navigate to the folder using 'cd <FOLDER_PATH>' and execute the Python script by using `ffpython batch_import_svg.py`

import fontforge
from pathlib import Path

font = fontforge.open('erathian.sfd')
# font = fontforge.font() # new font

svgFilePaths = list(Path('SVG').glob('**/*.svg'))

for p in svgFilePaths:
	dec = p.stem.split(" ", 1)[0]
	glyph = font.createChar(int(dec))
	glyph.importOutlines(str(p))

#font.generate('erathian.ttf')
font.save('erathian-output.sfd')
