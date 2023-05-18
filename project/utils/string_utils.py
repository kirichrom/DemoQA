class StringUtils:

    @staticmethod
    def parse_text_from_labels(labels_text_list: list) -> list:
        temp = []
        for text in labels_text_list:
            temp.append(text.split(':')[1])
        return temp

    @staticmethod
    def remove_new_line_symbols(labels_text_list: list) -> list:
        temp = []
        for text in labels_text_list:
            temp.append(text.replace('\n', ' '))
        return temp

