# J. Nathan Farmer, Sachinder Katoch, Rohit Kothari
#
# Step 2b: Run this file to remove the most and least common words in the index.

import json
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # This function loads the index from index.json
    with open('data/index.json', 'r') as read_file:
        idx = json.load(read_file)

    # Zipf Distribution
    token_count = []
    for key, value in idx.items():
            token_count.append([key, len(value)])

    token_df = pd.DataFrame(token_count, columns=['WORD','COUNT'])
    sorted_tokens = token_df.sort_values(by=['COUNT'], ascending=False)

    # Analyze word counts
    #num_bins = 200
    #fig, ax = plt.subplots()
    # the histogram of the data
    #_, _, _ = ax.hist(sorted_tokens['COUNT'], num_bins, density=1)
    #ax.set_xlabel('Word Count')
    #ax.set_ylabel('Probability Density')
    #ax.set_title('Histogram of Word Counts')
    # Tweak spacing to prevent clipping of ylabel
    #fig.tight_layout()
    #plt.show()

    remove_words = sorted_tokens[(sorted_tokens['COUNT'] == 1) | (sorted_tokens['COUNT'] > 1000)]['WORD'].values
    total_to_remove = len(remove_words)
    i=0
    for key in list(idx):
        if key in remove_words:
            del idx[key]
        i+=1
        if i % 1000 == 0:
            print(i, 'of', total_to_remove, 'complete')

    with open('data/zipf_index.json','w') as write_file:
        json.dump(idx, write_file)