from os import mkdir
from pathlib import Path
from ssg.parsers import Parser

class Site():
    
    def __init__(self, source, dest, parsers = None) -> None:
        self.parsers = parsers or []
        self.source = Path(source)
        self.dest = Path(dest)
    

    def create_dir(self, path):
        directory = self.dest/ path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
            

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    
    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print(NotImplemented)