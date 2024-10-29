file_path = "/Users/anudeepchennupati/Desktop/test.java" 

class LanguageSyntax:
    def __init__(self, language_name, single_line_comment_symbols, multi_line_comment_symbols, import_symbols=None, variable_symbols=None):
        self.language_name = language_name
        self.single_line_comment_symbols = single_line_comment_symbols
        self.multi_line_comment_symbols = multi_line_comment_symbols  # List of tuples (start, end)
        self.import_symbols = import_symbols
        self.variable_symbols = variable_symbols

class LineCounter:
    def __init__(self, language_syntax):
        self.language_syntax = language_syntax

    def count_lines(self, file_path):
        blank_lines = 0
        comment_lines = 0
        code_lines = 0
        total_lines = 0
        in_multi_line_comment = False

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                stripped_line = line.strip()

                if not stripped_line:
                    blank_lines += 1
                    continue

                if in_multi_line_comment:
                    comment_lines += 1
                    # Check if the multi-line comment ends on this line
                    for start_symbol, end_symbol in self.language_syntax.multi_line_comment_symbols:
                        if end_symbol in stripped_line:
                            in_multi_line_comment = False
                            break
                    continue

                # Check for multi-line comment start
                multi_comment_started = False
                for start_symbol, end_symbol in self.language_syntax.multi_line_comment_symbols:
                    if stripped_line.startswith(start_symbol):
                        comment_lines += 1
                        if not stripped_line.endswith(end_symbol) or stripped_line == start_symbol:
                            in_multi_line_comment = True
                        multi_comment_started = True
                        break
                if multi_comment_started:
                    continue

                if any(stripped_line.startswith(symbol) for symbol in self.language_syntax.single_line_comment_symbols):
                    comment_lines += 1
                    continue
                code_lines += 1

        print(f"Blank: {blank_lines}")
        print(f"Comments: {comment_lines}")
        print(f"Code: {code_lines}\n")
        print(f"Total: {total_lines}")

if __name__ == '__main__':
    java_syntax = LanguageSyntax('Java', ['//'], [('/*', '*/')])
    counter = LineCounter(java_syntax)
    result = counter.count_lines(file_path)
    print(result)
