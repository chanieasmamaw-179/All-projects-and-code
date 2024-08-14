from collections import Counter

def get_words(text):
    split_words = text.split()
    lower_word = [word.lower() for word in split_words]
    return lower_word

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
    
    play_text = """Climate change and weather dynamic is the cross-cutting issue all over the world. For developing
    countries, especially for East Saharan African countries including Ethiopia, the backbone of the economy depends
    on agriculture and accurate weather information is demanding. Most of the weather information is obtained from
    traditional surface meteorology stations. The weather information obtained from this station is not accurate
    enough, had recording bias, and lacked a digital data center. The main objective of this research is to estimate
     and retrieve atmospheric parameters such as precipitable water vapour (PWV) using ground-based GPS and remote
     sensing techniques such as GPS Radio Occultation (RO) for accurate weather studies and forecasting. The specific
     objective of this work was to estimate the regional vertical Total Electron Content (vTEC) densities, using a
     linear combination of L1 and L2 carrier phases for higher-order time delays at different thin-shell layers of
     the ionosphere over GPS stations in Ethiopia. Besides this, we estimate the GPS zenith delays to characterize
      the error of the neutral troposphere. During this research, we collected raw observational datasets using
      ground-based GPS from 2012 to 2015 and applied formulas to process GPS observed data through GPS Analysis
      (GAMIT/GLOBK) software."""
    

    words_list = get_words(play_text)
    freq_dict = words_frequency(words_list)

    top_50_words = top_n_words(freq_dict, 50)
    print("Top 50 most frequent words:")
    for word, count in top_50_words:
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()
