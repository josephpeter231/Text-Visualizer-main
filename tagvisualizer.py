import nltk


class TagVisualizer(object):
    """docstring for TagVisualizer"""

    def __init__(self, text):
        super(TagVisualizer, self).__init__()
        self.text = text
        self.TAGS = {
            'NN': 'green',
            'NNS': 'green',
            'NNP': 'green',
            'NNPS': 'green',
            'VB': 'blue',
            'VBD': 'blue',
            'VBG': 'blue',
            'VBN': 'blue',
            'VBP': 'blue',
            'VBZ': 'blue',
            'JJ': 'red',
            'JJR': 'red',
            'JJS': 'red',
            'RB': 'cyan',
            'RBR': 'cyan',
            'RBS': 'cyan',
            'IN': 'darkwhite',
            'POS': 'daryellow',
            'PRP$': 'magenta',
            'PRP$': 'magenta',
            'DET': 'white',
            'CC': 'white',
            'CD': 'white',
            'WDT': 'white',
            'WP': 'white',
            'WP$': 'white',
            'WRB': 'white',
            'EX': 'yellow',
            'FW': 'yellow',
            'LS': 'yellow',
            'MD': 'yellow',
            'PDT': 'yellow',
            'RP': 'yellow',
            'SYM': 'yellow',
            'TO': 'yellow',
            'None': 'off'
        }

    def generate_tags(self):
        # tokens= nltk.word_tokenize(docx)
        tagged_tokens = [[nltk.pos_tag(nltk.word_tokenize(i))]for i in self.text.split('.')]
        return tagged_tokens

    def visualize_tags(self):
        colored_text = []
        tagged_docx = self.generate_tags()
        for i in tagged_docx[0][0]:
            if i[1] in self.TAGS.keys():
                token = i[0]
                # print(token)
                color_for_tag = self.TAGS.get(i[1])
                result = '<span style="color:{}">{}</span>'.format(
                    color_for_tag, token)
                colored_text.append(result)
        result = ' '.join(colored_text)
        # print(result)
        return result
