from fpdf import FPDF

braille = {
    ' ': '⠀',   # space bar to dot-0
    '-': '⠤',
    ',': '⠂',
    ';': '⠆',
    ':': '⠒',
    '!': '⠖',
    '¡': '⠖',
    '?': '⠢',
    '¿': '⠢',
    '.': '⠄',
    '(': '⠣',
    ')': '⠜',
    '*': '',
    '&': '⠯',
    '#': '⠩',
    '"': '⠦',
    "'": '⠦',
    '0': '⠚',
    '1': '⠁',
    '2': '⠃',
    '3': '⠉',
    '4': '⠙',
    '5': '⠑',
    '6': '⠋',
    '7': '⠛',
    '8': '⠓',
    '9': '⠊',
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'ñ': '⠻',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'z': '⠵',
    'á': '⠷',
    'é': '⠮',
    'í': '⠌',
    'ó': '⠬',
    'ú': '⠾',
    'ü': '⠳'
}

ascii = {
    ' ': ' ',   # space bar to space bar
    '⠀': ' '   # dot-0 to space bar
}

for i, j in braille.items():
    ascii[j] = i

def convert(character):
    return braille[character] if braille[character] else '?'

def read(character):
    return ascii[character] if ascii[character] else '?'


def to_braille(text):
    braille_text = ''
    for i in text:
        braille_text += convert(i) if i.islower() else '⠨' + convert(i.lower())
    return braille_text

def to_text(code):
    ascii_text = ''
    for i in code:
        ascii_text += read(i)
    return ascii_text

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.add_font('Symbol', '', 'seguisym.ttf', uni=True)
pdf.set_font('Symbol', '', 32)
pdf.cell(40, 10, to_braille('Abraham'))
pdf.output('tuto1.pdf', 'F')

