
import fontforge

font = fontforge.open('Erathian.sfd')

font.generate('Erathian.otf')
font.generate('Erathian.ttf')
font.generate('Erathian.woff')
font.generate('Erathian.woff2')

fontMin = fontforge.open('Erathian-min.sfd')

fontMin.generate('Erathian-min.otf')
fontMin.generate('Erathian-min.ttf')
fontMin.generate('Erathian-min.woff')
fontMin.generate('Erathian-min.woff2')