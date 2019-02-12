import matplotlib.pyplot as plt

def vocabulary(corpus):
    sentences = corpus.split(" , ")
    words = []
    for s in sentences:
        words += s.split(" ")
    return words


def bigram_count(sentence):
    counts_all = []
    counts_word = []

    for i in sentence:
        for j in sentence:
            bigram = str(i + " " + j)
            counts_word += [corpus.count(bigram)]
        counts_all.append(counts_word)
        counts_word = []

    return counts_all


def bigram_smooth_count(sentence):
    counts_all = []
    counts_word = []

    for i in sentence:
        for j in sentence:
            bigram = str(i + " " + j)
            counts_word += [corpus.count(bigram) + 1]
        counts_all.append(counts_word)
        counts_word = []

    return counts_all


def bigram_probability(sentence):
    probability_all = []
    probability_word = []

    for i in sentence:
        for j in sentence:
            bigram = str(i + " " + j)
            probability_word += [round(corpus.count(bigram) / corpus.count(i), 5)]
        probability_all.append(probability_word)
        probability_word = []

    return probability_all


def bigram_smooth_probability(sentence):
    probability_all = []
    probability_word = []

    for i in sentence:
        for j in sentence:
            bigram = str(i + " " + j)
            probability_word += [round((corpus.count(bigram) + 1) / (corpus.count(i) + voc_size), 5)]
        probability_all.append(probability_word)
        probability_word = []

    return probability_all


def create_table(row, column, celltext):
    fig, ax = plt.subplots(figsize=(65, 35))
    ax.axis('off')
    table00 = ax.table(cellText=celltext, colWidths=([0.01] * len(column)),
                       rowLabels=row, colLabels=column, cellLoc='center',
                       loc='center')
    table00.set_fontsize(40)
    table00.scale(6, 8)
    return fig


def prob_calculate(s,probabilities):
    prob = 1/voc_size
    for i in range(len(s) - 1):
        prob = prob*probabilities[i][i + 1]
    return prob


input_file = open("Corpus.txt")
corpus = input_file.read().replace("\n", " ")

voc_size = len(set(vocabulary(corpus)))

S1 = "The chairman made the decision to bring in a new financial planner ."
S2 = "The profit of the company was going down last year said by the chief executive ."

s1_words = S1.split(" ")
s2_words = S2.split(" ")

# bigram counts(without smoothing & with add-one smoothing) - 4 tables

s1_count = bigram_count(s1_words)
fig1 = create_table(s1_words, s1_words, s1_count)
# fig1.savefig('table1.jpg')

s1_smooth_count = bigram_smooth_count(s1_words)
fig2 = create_table(s1_words, s1_words, s1_smooth_count)
# fig2.savefig('table2.jpg')

s2_count = bigram_count(s2_words)
fig3 = create_table(s2_words, s2_words, s2_count)
# fig3.savefig('table3.jpg')

s2_smooth_count = bigram_smooth_count(s2_words)
fig4 = create_table(s2_words, s2_words, s2_smooth_count)
# fig4.savefig('table4.jpg')

# bigram probabilities(without smoothing & with add-one smoothing) - 4 tables

s1_probabilities = bigram_probability(s1_words)
fig5 = create_table(s1_words, s1_words, s1_probabilities)
# fig5.savefig('table5.jpg')

s1_smooth_probabilities = bigram_smooth_probability(s1_words)
fig6 = create_table(s1_words, s1_words, s1_smooth_probabilities)
# fig6.savefig('table6.jpg')

s2_probabilities = bigram_probability(s2_words)
fig7 = create_table(s2_words, s2_words, s2_probabilities)
# fig7.savefig('table7.jpg')

s2_smooth_probabilities = bigram_smooth_probability(s2_words)
fig8 = create_table(s2_words, s2_words, s2_smooth_probabilities)
# fig8.savefig('table8.jpg')

# probabilities of sentences - 4 probabilities

s1_prob = prob_calculate(s1_words,s1_probabilities)
print("probability of S1(without smoothing):", s1_prob)

s1_smooth_prob = prob_calculate(s1_words,s1_smooth_probabilities)
print("probability of S1(with add-one smoothing):", s1_smooth_prob)

s2_prob = prob_calculate(s2_words,s2_probabilities)
print("probability of S2(without smoothing):", s2_prob)

s2_smooth_prob = prob_calculate(s2_words,s2_smooth_probabilities)
print("probability of S2(with add-one smoothing):", s2_smooth_prob)