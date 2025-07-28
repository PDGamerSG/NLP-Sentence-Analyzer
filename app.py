import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk import pos_tag,word_tokenize,pos_tag_sents
st.header("NLP Sentence Analyzer")
st.write("Enter a sentence to find stopwords and meaningful words:")
sentence = st.text_input(
    "Input your sentence:",
    placeholder="e.g. You are a handsome boy",
)
if sentence:
    if(len(sentence)>0):
        sentences = nltk.sent_tokenize(sentence)
        words = nltk.word_tokenize(sentences[0])
        words1 = nltk.word_tokenize(sentences[0])
    else:
        st.warning("Waiting for input :)")
else:
      st.stop()
tag = pos_tag_sents([sentence.split()])

length = len(tag[0])
list1 = []
for i in range(length):
        my_list = list(tag[0][i])
        list1 += my_list
list2 = ['CC','Conjuction','CD','Digits','EX','Existential','FW','Foreign Word','IN',' Preposition', 'JJ','Adjective', 'JJR', 'Adjective','JJS','Adjective','LS', 'List Marker','MD','Modal','NN','Noun','NNS','Plural Noun', 'NNP','Proper Noun', 'NNPS', 'Proper Noun', 'PDT', 'Predeterminer','POS','Possessive ending','PRP$','Possessive Pronoun','RB','Adverb','RBR','Comparative Adverb','RBS','Superlative Adverb','RP','Particle','TO', 'To', 'UH','Interjection','VB', 'Base Verb','VBD','Past Tense Verb','VBG','Present Tense Verb','VBN','Past Tense Verb','VBP','Present Tense Verb','VBZ','3rd Person Verb','WDT','Determiner', 'WP','Pronoun', 'WP$','Possessive','WRB','WH Adverb','DT','Determiner']

for i in range(1,len(list1),2):
                for j in range(len(list2)-1):
                        if(list1[i] == list2[j]):
                                list1[i] = list2[j+1]
                                break

n = int(len(list1)/2)
for i in range(n):
    st.markdown(f"- `{list1[2*i]}` → `{list1[2*i+1]}`")

#STOPWORDS IN THE SENTENCES
for i in range(len(sentences)):
    j=0
    while j<(len(words)):
        if words[j] in set(stopwords.words('ENGLISH')):
            del words[j]
        else:
            j+=1

normal = []
for word in words1:
    if word not in words:
        normal.append(word)

st.divider()
st.header("What Are Stopwords?")
st.markdown(
    """
    **Stopwords** are common words (like *the*, *is*, *in*, *and*) that are often taken out of text preprocessing because they don't add much or any meaning..
    """
)
st.divider()

st.subheader("Stopwords in Your Sentence")
if normal:
    st.markdown(f"**{len(normal)} stopwords found in the sentence:**")
    st.markdown(", ".join([f"`{word}`" for word in normal]))
else:
    st.info("No stopwords found in the given sentence")

st.divider()

st.subheader("Useful Words from Your Sentence")
if words:
    st.markdown(f"**{len(words)} important words found:**")
    st.markdown(", ".join([f"`{word}`" for word in words]))
else:
    st.warning("No useful words found.")
