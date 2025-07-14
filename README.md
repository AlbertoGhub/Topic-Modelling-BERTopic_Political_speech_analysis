# Topic-Modelling-BERTopic_Political_speech_analysis

FIRST COMMENT
For the moment and for simplicity, only the Russian analysis would be taken into account. In the future, the other parties, will be taken into account. Also, just for future analysis, I will turn the Date column into an actual date format (current one in Object format).

To do that, I will use the `pd.to_datetime()` function from the pandas library to convert the 'Date' column into a datetime format. This will allow for easier manipulation and analysis of the date data. Furthermore, I will manualy remove time from the date, as it is not needed for the analysis.

Second comment

# Topic Generation

***To add to the README file:***  

As written in the BERTopic’s documentation (make it a link - 'how to deal with topic outliers' https://maartengr.github.io/BERTopic/faq.html#how-do-i-reduce-topic-outliers ): Removing stop words as a preprocessing step is not advised as the transformer-based embedding models that we use need the full context to create accurate embeddings.

We use ```CountVectorizer``` in this case, only for the Bigram (and Trigram models in future improvements), as it is more suitable for these types of models. The ```CountVectorizer``` will be used to create a vocabulary of words that will be used to generate the topics. However, we will not use it to remove stop words, as it is not advised to do so. Instead, we will use the ```BERTopic``` model in combination with ```SentenceTransformer``` to generate the topics.

```BERTopic``` uses sentence transformer models as its first building block, converting sentences into dense vector representations (i.e. embeddings) that capture semantic meanings. These models are based on transformer architectures like BERT and are specifically trained to produce high-quality sentence embeddings. We then compute the semantic similarity between sentences using cosine distance between the embeddings. Common models include:

- ***all-MiniLM-L6-v2:*** lightweight, fast, good general performance
- ***BAAI/bge-base-en-v1.5:*** larger model with strong semantic understanding hence gives much slower training and inference speed.
There are a massive range of pre-trained sentence transformers for you to choose from on the “Sentence Transformer - https://www.sbert.net/docs/sentence_transformer/pretrained_models.html” website and 'Huggingface model hub - https://huggingface.co/models'. 

```Bertopic``` has a built-in parameter called ```n_gram_range``` to define the n-gram as well. Nevertheless, by using the `CountVectorizer` we can define the n-gram range more precisely and have more control (customization options) when fine-tuning the model. The `ngram_range` parameter in `CountVectorizer` allows us to specify the range of n-grams to be extracted from the text data. This is particularly useful for capturing phrases or combinations of words that may carry significant meaning in the context of the topics being analyzed.

# For the n-Gram, Here is an clarification:

## 📚 Understanding `ngram_range=(X, Y)` in `CountVectorizer`

The `ngram_range` parameter controls **how many words the model looks at together** when converting text into tokens.

> 🧠 It does **not** split text into “word + what follows.” Instead, it defines the **size of grouped word sequences (n-grams)**.

---

### 💡 Breakdown

| n-gram type | What it extracts                | Example (from `"climate change policy"`)            |
|-------------|----------------------------------|-----------------------------------------------------|
| `(1, 1)`    | Unigrams (single words)          | `"climate"`, `"change"`, `"policy"`                |
| `(2, 2)`    | Bigrams (2-word phrases)         | `"climate change"`, `"change policy"`              |
| `(3, 3)`    | Trigrams (3-word phrases)        | `"climate change policy"`                          |
| `(1, 3)`    | All n-grams from 1 to 3 words    | `"climate"`, `"climate change"`, `"climate change policy"` |

---

### ✅ Summary

- **The first number** in the range = minimum number of words per phrase.
- **The second number** = maximum number of words per phrase.
- This is about **grouping neighbouring words**, not predicting what comes next.

Thrid Comment

Note that the ```nr_topics``` is set to 7 for generating 6 topics. The remaining topic is used to keep the outliers.

On the other hand, after generating topics and their probabilities, we can access the frequent topics that were generated:

-1 refers to all outliers and should typically be ignored. Next, let's take a look at the most frequent topic that was generated, topic 0:

Forth Comment - Explanation

🔍 Understanding topic_model.get_topic(topic_id) in BERTopic
The method topic_model.get_topic(topic_id) returns a ranked list of keywords (or keyphrases) associated with a given topic. For example:

```bash
topic_model.get_topic(0)
```

Will return output like:

```bash
[
  ('state duma', 0.0058),
  ('russian federation', 0.0047),
  ('united russia', 0.0040),
  ...
]
```

📌 What this means:
The first item ('state duma') has the highest probability and is considered the most representative term of the topic.

The list is ranked by probability, showing how relevant each word is within that topic.

These probabilities are based on class-based TF-IDF (c-TF-IDF) scores — a method used by BERTopic to identify terms that are uniquely important for a specific topic compared to the entire corpus.

✅ Summary:
Ranks terms by importance for a given topic.

Probabilities reflect how strongly each term contributes to the topic.

Useful for labelling or interpreting the semantic meaning of topics.