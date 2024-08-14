# Romeo and Juliet project (Author/(s): Asmamaw Yehun (PhD) software Engineering student at Masterschool, Berlin. 2024:
# chanieasmamaw@yahoo.com or yehunchanieasmamaw@gmail.com
"""
We got an urgent mission: we must find the most common words in the play Romeo and Juliet.
Luckily, we have here the full play available for you, so all you have to do is to write the Python code.
Specification
After you run your code in the terminal, your code should find the top 50 most frequent words.
The code should print the words from the most frequent to the least frequent, along with the number of times that the
 word appeared in the play:
"""
from collections import Counter

def get_words(words):
    my_words_list = []
    split_words = words.split()
    my_words_list.extend(split_words)
    return my_words_list

def words_frequency(words_list):
    word_freq = {}
    for word in words_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
def top_n_words(freq_dict, n):
    # Count frequencies using Counter
    freq_counter = Counter(freq_dict)
    # Get the top n most common words
    top_n = freq_counter.most_common(n)
    return top_n
def main():
    input_text = "Climate change and weather dynamic is the cross-cutting issue all over the world. For developing countries, especially for East Saharan African countries including Ethiopia, the backbone of the economy depends on agriculture and accurate weather information is demanding. Most of the weather information is obtained from traditional surface meteorology stations. The weather information obtained from this station is not accurate enough, had recording bias, and lacked a digital data center. The main objective of this research is to estimate and retrieve atmospheric parameters such as precipitable water vapour (PWV) using ground-based GPS and remote sensing techniques such as GPS Radio Occultation (RO) for accurate weather studies and forecasting. The specific objective of this work was to estimate the regional vertical Total Electron Content (vTEC) densities, using a linear combination of L1 and L2 carrier phases for higher-order time delays at different thin-shell layers of the ionosphere over GPS stations in Ethiopia. Besides this, we estimate the GPS zenith delays to characterize the error of the neutral troposphere. During this research, we collected raw observational datasets using ground-based GPS from 2012 to 2015 and applied formulas to process GPS observed data through GPS Analysis (GAMIT/GLOBK) software."

    words_list = get_words(input_text)
    freq_dict = words_frequency(words_list)

    top_50_words = top_n_words(freq_dict, 50)
    print("Top 50 most frequent words:")
    for word, count in top_50_words:
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()
