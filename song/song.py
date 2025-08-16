import time

def delayed_typing(sentences, letter_delay, word_delay, sentence_delays):
    for sentence, sentence_delay in zip(sentences, sentence_delays):
        words = sentence.split()  

        for word in words:
            for letter in word:
                print(letter, end="", flush=True)  
                time.sleep(letter_delay) 

            print(" ", end="", flush=True)  
            time.sleep(word_delay)  

        print("\n")  
        time.sleep(sentence_delay) 


sentences = [
    "Your morning eyes,",
    "I could stare like watching stars",
    "I could walk "
    "you by,",
    "and I'll tell without a thought",
    "You'd be mine,",
    "would you mind",
    "if I took your hand tonight?",
    "Know you're all that I want this life",
    "I'll imagine we fell in love",
    "I'll nap under moonlight skies with you",  
    "I think I'll picture us,",  
    "you with the waves",  
    "The ocean's colors on your face",  
    "I'll leave my heart with your air",  
    "So let me fly with you",  
    "Will you be forever with me?"  
]


letter_delay = 0.1  
word_delay = 0.2 


sentence_delays = [0.17, 0.15, 0.1, 0.15, 0.16, 0.1, 0.1, 3, 0, 0.2, 0.2, 0.2, 0.3, 0.4, 0.2, 0.5]  


special_lines = [
    "I'll imagine we fell in love",
    "I'll nap under moonlight skies with you",
    "I think I'll picture us,",
    "you with the waves",
    "The ocean's colors on your face"
    
    
]


for idx, sentence in enumerate(sentences):
    if sentence in special_lines:
        letter_delay = 0.05
    else:
        letter_delay = 0.1
    delayed_typing([sentence], letter_delay, word_delay, [sentence_delays[idx]])
