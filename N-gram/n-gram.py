import matplotlib.pyplot as plt
import sys

def tokenize(corpus):
    sentences = corpus.split(" , ")
    words = []
    for s in sentences:
        words += s.split(" ")
    return words


def count_dict(corpus_words):
    i = 0
    dic = {}
    while i < (len(corpus_words) - 1):
        bigram = corpus_words[i] + " " + corpus_words[i + 1]
        if bigram not in dic:
            dic[bigram] = 1
        else:
            dic[bigram] += 1
        i += 1
    return dic


def probability_dict(corpus_words, count_dic):
    i = 0
    dic = {}
    while i < (len(corpus_words) - 1):
        bigram = corpus_words[i] + " " + corpus_words[i + 1]
        dic[bigram] = round(count_dic[bigram] / corpus_words.count(corpus_words[i]), 5)
        i += 1
    return dic


def probability_smooth_dict(corpus_words, count_dic):
    i = 0
    dic = {}
    while i < (len(corpus_words) - 1):
        bigram = corpus_words[i] + " " + corpus_words[i + 1]
        dic[bigram] = round((count_dic[bigram] + 1) / (corpus_words.count(corpus_words[i]) + voc_size), 5)
        i += 1
    return dic


def bigram_count(words, dic):
    counts_all = []
    counts_word = []

    for i in words:
        for j in words:
            bigram = i + " " + j
            if bigram in dic:
                counts_word += [dic[bigram]]
            else:
                counts_word += [0]
        counts_all.append(counts_word)
        counts_word = []

    return counts_all


def bigram_smooth_count(words, dic):
    counts_all = []
    counts_word = []

    for i in words:
        for j in words:
            bigram = i + " " + j
            if bigram in dic:
                counts_word += [dic[bigram] + 1]
            else:
                counts_word += [1]
        counts_all.append(counts_word)
        counts_word = []

    return counts_all


def bigram_probability(sentence, dic):
    probability_all = []
    probability_word = []

    for i in sentence:
        for j in sentence:
            bigram = i + " " + j
            if bigram in dic:
                probability_word += [dic[bigram]]
            else:
                probability_word += [0.0]
        probability_all.append(probability_word)
        probability_word = []

    return probability_all


def bigram_smooth_probability(sentence, dic):
    probability_all = []
    probability_word = []

    for i in sentence:
        for j in sentence:
            bigram = i + " " + j
            if bigram in dic:
                probability_word += [dic[bigram]]
            else:
                probability_word += [round(1 / (words.count(i) + voc_size), 5)]
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


def prob_calculate(s_unique, prob_dic):
    prob = 1 / voc_size
    for i in range(len(s_unique) - 1):
        bigram = s_unique[i] + " " + s_unique[i + 1]
        if bigram in prob_dic:
            prob = prob * prob_dic[bigram]
        else:
            prob = 0.0

    return prob


def prob_calculate_smooth(s_unique, prob_dic):
    prob = 1 / voc_size
    for i in range(len(s_unique) - 1):
        bigram = s_unique[i] + " " + s_unique[i + 1]
        if bigram in prob_dic:
            prob = prob * prob_dic[bigram]
        else:
            prob = prob * round(1/(words.count(s_unique[i])+voc_size), 5)

    return prob


input_file = open(sys.argv[1])
corpus = input_file.read().replace("\n", " ").lower()
words = tokenize(corpus)
voc_size = len(set(words))

bigram_dict = count_dict(words)
prob_dict = probability_dict(words, bigram_dict)
prob_smooth_dict = probability_smooth_dict(words, bigram_dict)

# S1 = "The chairman made the decision to bring in a new financial planner ."
# S2 = "The profit of the company was going down last year said by the chief executive ."

S1 = sys.argv[2]
S2 = sys.argv[3]

s1_words = S1.lower().split(" ")
s2_words = S2.lower().split(" ")
s1_unique = sorted(set(s1_words), key=s1_words.index)
s2_unique = sorted(set(s2_words), key=s2_words.index)

# bigram counts(without smoothing & with add-one smoothing) - 4 tables

s1_count = bigram_count(s1_unique, bigram_dict)
fig1 = create_table(s1_unique, s1_unique, s1_count)
fig1.savefig('table1.jpg')

s1_smooth_count = bigram_smooth_count(s1_unique, bigram_dict)
fig2 = create_table(s1_unique, s1_unique, s1_smooth_count)
fig2.savefig('table2.jpg')

s2_count = bigram_count(s2_unique, bigram_dict)
fig3 = create_table(s2_unique, s2_unique, s2_count)
fig3.savefig('table3.jpg')

s2_smooth_count = bigram_smooth_count(s2_unique, bigram_dict)
fig4 = create_table(s2_unique, s2_unique, s2_smooth_count)
fig4.savefig('table4.jpg')

# bigram probabilities(without smoothing & with add-one smoothing) - 4 tables

s1_probabilities = bigram_probability(s1_unique, prob_dict)
fig5 = create_table(s1_unique, s1_unique, s1_probabilities)
fig5.savefig('table5.jpg')

s1_smooth_probabilities = bigram_smooth_probability(s1_unique, prob_smooth_dict)
fig6 = create_table(s1_unique, s1_unique, s1_smooth_probabilities)
fig6.savefig('table6.jpg')

s2_probabilities = bigram_probability(s2_unique, prob_dict)
fig7 = create_table(s2_unique, s2_unique, s2_probabilities)
fig7.savefig('table7.jpg')

s2_smooth_probabilities = bigram_smooth_probability(s2_unique, prob_smooth_dict)
fig8 = create_table(s2_unique, s2_unique, s2_smooth_probabilities)
fig8.savefig('table8.jpg')

# probabilities of sentences - 4 probabilities

s1_prob = prob_calculate(s1_words, prob_dict)
print("probability of S1(without smoothing) = ", s1_prob)

s1_smooth_prob = prob_calculate_smooth(s1_words, prob_smooth_dict)
print("probability of S1(with add-one smoothing):", s1_smooth_prob)

s2_prob = prob_calculate(s2_words, prob_dict)
print("probability of S2(without smoothing) = ", s2_prob)

s2_smooth_prob = prob_calculate_smooth(s2_words, prob_smooth_dict)
print("probability of S2(with add-one smoothing):", s2_smooth_prob)

