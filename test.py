# Manually define a set of stop words
stop_words = ['a', 'in', 'the', 'and', 'is', 'on', 'with', 'for', 'to', 'an']

# Define a function to clean the text (lowercase and remove punctuation)
def clean_text(text):
    clean_text = ""  # Start with an empty string
    for char in text:
        # Keep only letters and spaces (remove punctuation)
        if char.isalnum() or char == " ":
            clean_text += char.lower()
    return clean_text

# Define a function to remove stop words
def remove_stop_words(word_list):
    filtered_words = []  # List to hold words that are not stop words
    
    # Loop through each word
    for word in word_list:
        if word not in stop_words:  # Only keep the word if it's not in the stop words list
            filtered_words.append(word)  # Add the word to the filtered list
    
    return filtered_words

# Example text to analyze
text = "A feather was found in the livingroom and it was a mystery."

# Process the text
cleaned_text = clean_text(text)  # Clean the text
word_list = cleaned_text.split()  # Split the cleaned text into individual words

# Remove stop words
filtered_words = remove_stop_words(word_list)

# Output the result
print(clean_text)
print("\n")
print(cleaned_text)
print('\n')
print(word_list)
print("Filtered words:", filtered_words)
