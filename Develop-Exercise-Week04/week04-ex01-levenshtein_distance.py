def load_vocab ( file_path ):
    with open ( file_path , 'r') as f:
        lines = f.readlines()
        words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab ( file_path ='./vocab.txt')

def levenshtein_distance(token1: str, token2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.
    
    Args:
    token1 (str): First string
    token2 (str): Second string
    
    Returns:
    int: Levenshtein distance
    """
    m, n = len(token1), len(token2)
    distances = [[i + j for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if token1[i-1] == token2[j-1] else 1
            distances[i][j] = min(distances[i-1][j] + 1,      # deletion
                                  distances[i][j-1] + 1,      # insertion
                                  distances[i-1][j-1] + cost) # substitution

    return distances[m][n]

import streamlit as st

def main():
    # Danh sách từ vựng mẫu
    st.title("Word Correction using Levenshtein Distance")
    vocabs = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
  

    word = st.text_input('Word: ')

    if st.button("Compute"):
        if word:
            # compute levenshtein distance
            leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}

            # sorted by distance
            sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
            correct_word = list(sorted_distances.keys())[0]

            st.write(f"Correct word: {correct_word}")

            col1, col2 = st.columns(2)
        
            with col1:
                st.write("Vocabulary:")
                st.write(vocabs)
        
            with col2:
                st.write("Distances:")
                st.write(sorted_distances)
        else:
            st.warning("Please enter a word.")

if __name__ == "__main__":
    main() # Không cần gọi main() trong Streamlit