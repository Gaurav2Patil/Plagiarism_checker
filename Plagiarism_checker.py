import tkinter as tk
from tkinter import scrolledtext, Button, Label
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# Tokenization, stemming, and stop words removal
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    words = word_tokenize(text.lower())
    words = [stemmer.stem(word) for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

def calculate_similarity():
    input_doc1 = doc1_widget.get("1.0", "end-1c")
    input_doc2 = doc2_widget.get("1.0", "end-1c")
    
    preprocessed_doc1 = preprocess(input_doc1)
    preprocessed_doc2 = preprocess(input_doc2)
    
    corpus = [preprocessed_doc1, preprocessed_doc2]
    
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
    similarity_score = cosine_similarities[0][1]
    
    similarity_label.config(text=f"Plagirism Score: {similarity_score:.2%}")

def clear_input():
    doc1_widget.delete("1.0", tk.END)
    doc2_widget.delete("1.0", tk.END)
    similarity_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Document Similarity Checker")

# Create and place widgets
doc1_label = Label(root, text="Enter Document 1:")
doc1_label.pack()

doc1_widget = scrolledtext.ScrolledText(root, height=5, width=50)
doc1_widget.pack()

doc2_label = Label(root, text="Enter Document 2:")
doc2_label.pack()

doc2_widget = scrolledtext.ScrolledText(root, height=5, width=50)
doc2_widget.pack()

check_button = Button(root, text="Check Plagiarism", command=calculate_similarity)
check_button.pack()

clear_button = Button(root, text="Clear Input", command=clear_input)
clear_button.pack()

similarity_label = Label(root, text="")
similarity_label.pack()

if __name__ == "__main__":
    # Start the main loop
    root.mainloop()
