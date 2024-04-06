# core packages
import nltk
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
import spacy

nlp = spacy.load('en_core_web_lg')

nltk.download('averaged_perceptron_tagger')
import streamlit as st
import streamlit.components.v1 as stc
from ui_template import HTML_BANNER, HTML_BANNER_SKEWED, HTML_WRAPPER, HTML_STICKER

# EDA packages
import pandas as pd
import neattext as nt
import neattext.functions as nfx
from collections import Counter

# Data viz packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# NLP packages
import wordcloud
from wordcloud import WordCloud
import nltk
import spacy
from spacy import displacy

# Text Viz packages
from tagvisualizer import TagVisualizer  
from yellowbrick.text import PosTagVisualizer

# Function to summarize text
def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summarized_text = ' '.join(str(sentence) for sentence in summary)
    return summarized_text

# Function to plot word cloud
def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    plt.imshow(mywordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

# Function to plot tag cloud
def plot_tagcloud(docx):
    tags = docx.split()
    tag_freq = Counter(tags)
    tag_cloud = wordcloud.WordCloud(
        max_words=100,
        background_color='white',
        width=500,
        height=500,
    ).generate_from_frequencies(tag_freq)
    plt.imshow(tag_cloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

# Function to plot Mendelhall Curve
def plot_mendelhall_curve(docx):
    word_length = [len(token) for token in docx.split()]
    word_length_counts = Counter(word_length)
    sorted_word_length_count = sorted(dict(word_length_counts).items())
    x, y = zip(*sorted_word_length_count)
    fig = plt.figure(figsize=(20, 10))
    plt.title("Plot of Word Length Distribution")
    plt.suptitle("Mendelhall Curve")
    plt.plot(x, y, color="blue")
    plt.xlabel("Word Length")
    plt.ylabel("Frequency")
    plt.annotate("Average word length: 5", xy=(5, 0.2), xytext=(5, 0.1),
                arrowprops=dict(facecolor="black", edgecolor="black", shrink=0.05))
    plt.annotate("Median word length: 6", xy=(9, 0.15), xytext=(9, 0.1),
                arrowprops=dict(facecolor="black", edgecolor="black", shrink=0.05))
    st.pyplot(fig)

# Function to get most common tokens
def get_most_common_tokens(docx, num=10):
    word_freq = Counter(docx.split())
    most_common_tokens = word_freq.most_common(num)
    return dict(most_common_tokens)

# Function to generate tags
def generate_tags(docx):
    tagged_docx = [[nltk.pos_tag(nltk.word_tokenize(i))] for i in docx.split('.')]
    return tagged_docx

# Function to plot most common tokens
def plot_most_common_tokens(docx, num=10):
    word_freq = Counter(docx.split())
    most_common_tokens = word_freq.most_common(num)
    x, y = zip(*most_common_tokens)
    fig = plt.figure(figsize=(20, 10))
    plt.bar(x, y)
    plt.title("Plot of Most Common Tokens")
    plt.show()
    st.pyplot(fig)

# Function to plot POS tags
def plot_pos_tags(tagged_docx):
    pos_visualizer = PosTagVisualizer()
    pos_visualizer.fit(tagged_docx)
    pos_visualizer.show()
    st.pyplot()

# Main function
def main():
    st.title("TextSight")
    menu = ["Home", "DropFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Home")
        raw_text = st.text_area("Enter Text Here")
        viz_task = ["Basic", "WordCloud","Tag cloud",
                    "Mendelhall Curve", "Pos Tagger", "NER","Text Summarization"]
        viz_choice = st.sidebar.selectbox("Choice", viz_task)
        if st.button("Process"):
            if viz_choice == "WordCloud":
                plot_wordcloud(raw_text)
            elif viz_choice == "Pos Tagger":
                tagged_docx = generate_tags(raw_text)
                plot_pos_tags(tagged_docx)
                t = TagVisualizer(raw_text)
                stc.html(t.visualize_tags())
            elif viz_choice == "Mendelhall Curve":
                plot_mendelhall_curve(raw_text)
            elif viz_choice == "NER":
                doc = nlp(raw_text)
                html = displacy.render(doc, style="ent")
                stc.html(html, scrolling=True)
            elif viz_choice == "Text Summarization":
                summarized_text = summarize_text(raw_text)
                st.write(summarized_text)
            elif viz_choice == "Tag cloud":
                plot_tagcloud(raw_text)
            else:
                st.info("Text Visualizer")
                processed_text = nfx.remove_stopwords(raw_text)
                word_desc = nt.TextFrame(raw_text).word_stats()
                st.info("Text Description")
                st.write(word_desc)
                st.info("Most Common Tokens")
                most_common_tokens = get_most_common_tokens(processed_text)
                token_df = pd.DataFrame(
                    most_common_tokens.items(), columns=['Tokens', 'Counts'])
                st.dataframe(token_df)
                plot_most_common_tokens(processed_text)

    elif choice == "DropFiles":
        st.subheader("Drag and Drop Files")
        raw_text_file = st.file_uploader("Upload Text Files", type=['txt'])
        viz_task = ["Basic", "WordCloud","Tag cloud",
                    "Mendelhall Curve", "Pos Tagger", "NER", "Text Summarization"]
        viz_choice = st.sidebar.selectbox("Choice", viz_task)
        if st.button("Visualize"):
            if raw_text_file is not None:
                file_text = raw_text_file.read()
                raw_text = file_text.decode('utf-8')
                st.write(raw_text)
                if viz_choice == "WordCloud":
                    plot_wordcloud(raw_text)
                elif viz_choice == "Pos Tagger":
                    tagged_docx = generate_tags(raw_text)
                    plot_pos_tags(tagged_docx)
                    t = TagVisualizer(raw_text)
                    stc.html(t.visualize_tags())
                elif viz_choice == "Mendelhall Curve":
                    plot_mendelhall_curve(raw_text)
                elif viz_choice == "NER":
                    doc = nlp(raw_text)
                    html = displacy.render(doc, style="ent")
                    stc.html(html, scrolling=True)
                elif viz_choice == "Text Summarization":
                    summarized_text = summarize_text(raw_text)
                    st.write(summarized_text)
                elif viz_choice == "Tag cloud":
                    plot_tagcloud(raw_text)
                else:
                    st.info("Text Visualizer")
                    processed_text = nfx.remove_stopwords(raw_text)
                    word_desc = nt.TextFrame(raw_text).word_stats()
                    st.info("Text Description")
                    st.write(word_desc)
                    st.info("Most Common Tokens")
                    most_common_tokens = get_most_common_tokens(processed_text)
                    token_df = pd.DataFrame(
                        most_common_tokens.items(), columns=['Tokens', 'Counts'])
                    st.dataframe(token_df)
                    plot_most_common_tokens(processed_text)
    else:
        st.subheader("About App")
        stc.html(HTML_STICKER, width=800, height=600)

if __name__ == '__main__':
    main()
