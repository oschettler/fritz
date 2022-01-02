'''
The Fritz programming language.
(c) 2022 Olav Schettler

License: MIT.
'''
import statements
import sys

class Token:
    def __init__(self, type, pos, text, info=None):
        self.type = type
        self.pos = pos
        self.text = text
        self.info = info


class Lexer:
    def __init__(self, file):
        self.pos = 0
        self.line_number = 1
        self.column_number = 1
        self.indent = 0
        self.file = file
        self.end_of_file = False
        self.current_char = ''
        self.mode = 'markdown'


    def error(self, message):
        print(f'Error (line {self.line_number}, column {self.column_number}): {message}.')
        sys.exit()


    def next(self):
        self.current_char =  self.file.read(1)
        if self.current_char == '':
            self.end_of_file = True
            return False
        
        self.pos += 1
        self.column_number += 1
        if self.current_char == '\n':
            self.line_number += 1
            self.column_number = 1
            self.indent = 0
        elif self.current_char == '\t':
            if self.indent >= 0:
                self.error('Please indent with space, not tab')
        elif self.current_char == ' ':
            if self.indent >= 0:
                self.indent += 1 
        return True


    def token(self):
        self.next()

        if self.mode == 'markdown':
            if self.indent == 0:
                if self.current_char == '#':
                    return self.read_markdown_headline()
                else:
                    return self.read_markdown_paragraph()

            else:
                return Token('md:unknown', self.pos, '')


    def read_markdown_headline(self):
        pos = self.pos
        text = '#'
        level = 1
        while self.next():
            if self.current_char != '#':
                break
            level += 1
            text += self.current_char

        if self.end_of_file:
            return Token('eof', pos, text)
        elif self.current_char == '\n':
            return Token('md:paragraph', pos, text)
        else:
            text += self.current_char

        while self.next():
            if self.current_char == '\n':
                return Token('md:headline', pos, text, level)
            text += self.current_char

        return Token('md:headline', pos, text, level)


    def read_markdown_paragraph(self):
        pos = self.pos
        text = self.current_char
        newlines_seen = 0

        while self.next():
            if self.current_char == '\n':
                newlines_seen += 1
            else:
                if newlines_seen > 1:
                    return Token('md:paragraph', pos, text)
                else:
                    newlines_seen = 0
            text += self.current_char

        return Token('md:paragraph', pos, text)


class Parser:
    def __init__(self, file):
        self.lexer = Lexer(file)


    def run(self):
        print("Parsing...")
        program = self.parse_markdown()
        print("Running...")
        for statement in program:
            statement.run()
        print("Done.")
    

    def parse_markdown(self):
        print(" - markdown")
        program = []
        while True:
            token = self.lexer.token()
            if token.type == 'eof':
                return program

            if token.type == 'md:headline':
                program.append(statements.MarkdownHeadline(token))
            elif token.type == 'md:paragraph':
                program.append(statements.MarkdownParagraph(token))
            else:
                self.lexer.error(f'Unknown token {token.type} with text "{token.text}"')

def main():
    if len(sys.argv) != 2:
        sys.exit("Please pass script to execute")
    Parser(open(sys.argv[1])).run()
