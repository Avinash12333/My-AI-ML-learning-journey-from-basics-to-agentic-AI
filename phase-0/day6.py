import numpy as np

# =========================
# Exercise 1 — Basic Probability
# =========================
# Probability = favorable outcomes / total outcomes
# P(A or B) = P(A) + P(B) when mutually exclusive
# P(not A) = 1 - P(A)

def exercise1():
    total = 5 + 3 + 2  # 10 balls
    p_red   = 5 / total  # 0.5
    p_blue  = 3 / total  # 0.3
    p_green = 2 / total  # 0.2

    print("Exercise 1:")
    print("P(red):", p_red)
    print("P(blue):", p_blue)
    print("P(green):", p_green)
    print("P(red or blue):", p_red + p_blue)  # 0.8
    print("P(not green):", 1 - p_green)        # 0.8
    print()

exercise1()

# =========================
# Exercise 2 — Conditional Probability + Bayes
# =========================
# P(pass) = P(pass|study)*P(study) + P(pass|not study)*P(not study)
# P(study|pass) = P(pass|study) * P(study) / P(pass)  ← Bayes theorem

def exercise2():
    p_study             = 0.6
    p_not_study         = 0.4
    p_pass_given_study  = 0.9
    p_pass_given_not    = 0.3

    # Total probability rule
    p_pass = (p_pass_given_study * p_study) + (p_pass_given_not * p_not_study)

    # Bayes theorem
    p_study_given_pass = (p_pass_given_study * p_study) / p_pass

    print("Exercise 2:")
    print("P(pass):", p_pass)               # 0.66
    print("P(study | pass):", p_study_given_pass)  # ~0.818
    print()

exercise2()

# =========================
# Exercise 3 — Medical Test (Bayes)
# =========================
# Key insight: even a 99% accurate test can be misleading
# when the disease is very rare (1% of population)
# Result: P(disease | positive) ≈ 0.50 — not 99%!
# This is the BASE RATE FALLACY — always consider the prior!

def exercise3():
    p_disease    = 0.01
    p_no_disease = 0.99

    p_pos_given_disease = 0.99
    p_pos_given_no      = 0.01

    # Total probability of testing positive
    p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_no * p_no_disease)

    # Bayes theorem
    p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos

    print("Exercise 3:")
    print("P(positive):", p_pos)                        # ~0.0198
    print("P(disease | positive):", p_disease_given_pos)  # ~0.50
    print("Surprised? Most people guess 99%!")
    print()

exercise3()

# =========================
# Exercise 4 — Spam Filter
# =========================
# Bayes theorem applied to spam detection
# P(spam | "free") = P("free" | spam) * P(spam) / P("free")

def exercise4():
    p_spam     = 0.4
    p_not_spam = 0.6

    p_free_given_spam = 0.8
    p_free_given_not  = 0.1

    # Total probability of seeing "free"
    p_free = (p_free_given_spam * p_spam) + (p_free_given_not * p_not_spam)

    # Bayes theorem
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free

    print("Exercise 4:")
    print("P(free):", p_free)                      # 0.38
    print("P(spam | 'free'):", p_spam_given_free)  # ~0.842
    print()

exercise4()

# =========================
# Exercise 5 — Naive Bayes from Scratch
# =========================
# Naive Bayes assumes all words are independent (the "naive" assumption)
# Despite this unrealistic assumption it works very well for text
# Laplace smoothing adds 1 to avoid zero probabilities for unseen words

def exercise5():
    data = [
        ("free money now",          "spam"),
        ("click here free",         "spam"),
        ("meeting at noon",         "ham"),
        ("project deadline tomorrow", "ham")
    ]

    classes     = ["spam", "ham"]
    word_counts = {"spam": {}, "ham": {}}
    class_counts= {"spam": 0,  "ham": 0}
    vocab       = set()

    # Training — count words per class
    for text, label in data:
        class_counts[label] += 1
        for word in text.split():
            vocab.add(word)
            word_counts[label][word] = word_counts[label].get(word, 0) + 1

    total_words = {c: sum(word_counts[c].values()) for c in classes}

    # Classification
    def classify(text):
        words = text.split()
        probs = {}
        for c in classes:
            # Start with prior probability
            prob = class_counts[c] / len(data)
            for word in words:
                # Laplace smoothing: add 1 to numerator, vocab size to denominator
                count = word_counts[c].get(word, 0) + 1
                prob *= count / (total_words[c] + len(vocab))
            probs[c] = prob
        return max(probs, key=probs.get)

    print("Exercise 5:")
    print("'free meeting' →", classify("free meeting"))    # spam
    print("'project meeting' →", classify("project meeting"))  # ham
    print()

exercise5()