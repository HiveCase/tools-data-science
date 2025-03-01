import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_text_file(file_path):
    """Reads the content of a text file."""
    with open(file_path, 'r') as f:
        return f.read()

def calculate_similarity(file1_path, file2_path):
    """Calculates cosine similarity between two text files."""
    text1 = read_text_file(file1_path)
    text2 = read_text_file(file2_path)

    # Vectorize the text
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    # Convert to percentage
    similarity_percentage = round(similarity[0][0] * 100, 2)

    return similarity_percentage

# Specify file paths
file1 = "path/to/your/file1.txt"
file2 = "path/to/your/file2.txt"

# Calculate and print similarity
similarity = calculate_similarity(file1, file2)
print(f"The content similarity between the documents is: {similarity}%")
