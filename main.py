from fpdf import FPDF
import json

braille = {
    # ' ': '⠀',   # space bar to dot-0
    ' ': ' ',
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
    '#': '⠼',
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
    'y': '⠽',
    'z': '⠵',
    'á': '⠷',
    'é': '⠮',
    'í': '⠌',
    'ó': '⠬',
    'ú': '⠾',
    'ü': '⠳',
    '\n': '\n'
}


ascii = {
    ' ': ' ',   # space bar to space bar
    '⠀': ' '   # dot-0 to space bar
}

for i, j in braille.items():
    ascii[j] = i


def convert(character):
    return braille[character] if braille.get(character) else '?'


def read(character):
    return ascii[character] if ascii.get(character) else '?'


def to_braille(text):
    braille_text = ''
    for i in text:
        braille_text += '⠨' + convert(i.lower()) if i.isupper() else convert(i)
    return braille_text


def to_text(code):
    ascii_text = ''
    for i in code:
        ascii_text += read(i)
    return ascii_text


title = 'Zoogotá'


class PDF(FPDF):
    def header(self):
        self.set_font('Symbol', '', 25)
        # Arial bold 15
        # self.set_font('Arial', 'B', 15)
        # Calcular ancho del texto (title) y establecer posición
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colores del marco, fondo y texto
        # self.set_draw_color(0, 80, 180)
        # self.set_fill_color(230, 230, 0)
        # self.set_text_color(220, 50, 50)
        # Grosor del marco (1 mm)
        # self.set_line_width(1)
        # Titulo
        self.cell(w, 9, to_braille(title), 0, 1, 'C', 0)
        # Salto de línea
        self.ln(10)

    def footer(self):
        # Posición a 1.5 cm desde abajo
        # self.set_y(-15)
        self.set_y(-90)
        # Arial italic 8
        # self.set_font('Arial', 'I', 8)
        self.set_font('Symbol', '', 25)
        # Color de texto en gris
        # self.set_text_color(128)
        # Numero de pagina
        # self.cell(0, 10, to_braille(f'page #{self.page_no()}'), 0, 0, 'C')
        self.cell(0, 10, to_braille(f'Manuel Espitia Benavides'), 0, 0, 'R')
        self.ln(10)
        self.cell(0, 10, to_braille(f'#28 años'), 0, 0, 'R')
        self.ln(10)
        self.cell(0, 10, to_braille(f'Chapinero'), 0, 0, 'R')

    def chapter_title(self, num, label):
        self.set_font('Symbol', '', 25)
        # Arial 12
        # self.set_font('Arial', '', 12)
        # Color de fondo
        # self.set_fill_color(200, 220, 255)
        # Titulo
        # self.cell(0, 6, to_braille(f'chapter #{num} : {label}'), 0, 1, 'L', 0)
        # Salto de línea
        self.ln(4)

    def chapter_body(self, name):
        # Leer archivo de texto
        # with open(name, 'r') as f:
        #     txt = f.read()
        # Times 12
        # self.set_font('Times', '', 12)
        self.set_font('Symbol', '', 25)

        # Emitir texto justificado
        self.multi_cell(0, 10, to_braille(name), 0, 'J')
        # Salto de línea
        # self.ln()
        # Mención en italic -cursiva-
        # self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, c_title, name):
        self.add_page()
        self.chapter_title(num, c_title)
        self.chapter_body(name)


with open("braille.json") as file:
    data = json.load(file)

pdf = PDF('P', 'mm', 'Letter')
pdf.add_font('Symbol', '', 'seguisym.ttf', uni=True)
pdf.set_title(data["title"])
pdf.set_author(data["author"])
pdf.print_chapter(0, data["chapters"][0]["title"], data["chapters"][0]["content"])
a = to_braille(data["chapters"][0]["content"])
pdf.add_page()
pdf.output('braille.pdf', 'F')

