import io

from lark import Lark
from lark.exceptions import LarkError

from errors.ShellError import ShellError
from files.files_io import read_from_file


class LarkParserLoader:
    @staticmethod
    def create_parser(grammar_file) -> Lark:
        out, err = io.StringIO(), io.StringIO()
        success = read_from_file(grammar_file, out, err)
        if success:
            try:
                return Lark(out.getvalue(), parser='earley')
            except LarkError as e:
                raise ShellError('[Parser] Error while creating parser: %s' % str(e))
        else:
            raise ShellError('[Parser] Cannot load grammar file %s' % grammar_file)
