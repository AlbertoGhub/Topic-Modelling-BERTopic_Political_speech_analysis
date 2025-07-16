# Notes from testing.

I found out that removing stopwords can help in defining topics in a better way.
The documentation says "when using LLM for semantic topics, dont remove stopwords", now the next steps is keep on testing bigger LLMs and fine-tune them.

# OLD CODE VERSION:

# # Create a list of speeches
# docs = r_df['Text_of_Speech'].tolist()

# # Define vectorizer (For the Bigram model - pair of words)
# vectorizer_model = CountVectorizer(ngram_range = (2, 2))

# # VERSION WITH A PRETRAINED MODEL (to fine-tune the model, we can test other pre-models)

# # emb_minilm = SentenceTransformer("all-MiniLM-L6-v2") # This is a smaller model that is faster and requires less memory

# # # Build BERTopic model
# # topic_model = BERTopic(
# #     top_n_words         = 10,
# #     n_gram_range        = (2,2),
# ##     nr_topics           = n_topics,
# #     embedding_model     = emb_minilm,
# #     vectorizer_model    = vectorizer_model,
# #     umap_model          = UMAP(random_state = 1)
# # )

# # VERSION WITH A COUNTVECTORIZER

# Remove english stopwords with a vectorizer
standard_stopwords = list(stopwords.words('english'))

# # Test 1
# additional_stopwords = ['let', 'us','like','say','would','also',
#                         'th','need','afternoon','ladies','gentleman',
#                         'foremost','colleagues','friends','years',
#                         'ago','last','year']

# # Test 2
additional_stopwords = [
    'people', 'government', 'country', 'nation', 'state', 'public', 'citizen',
    'citizens', 'parliament', 'house', 'chamber', 'minister', 'leaders',
    'leader', 'party', 'parties', 'political', 'politics', 'policy', 'policies',
    'economy', 'economic', 'social', 'national', 'international', 'global',
    'community', 'communities', 'system', 'systems', 'reform', 'future',
    'today', 'tomorrow', 'yesterday', 'time', 'years', 'year', 'day', 'days',
    'new', 'old', 'great', 'good', 'bad', 'well', 'better', 'best', 'more',
    'less', 'much', 'many', 'all', 'any', 'some', 'no', 'every', 'each',
    'these', 'those', 'this', 'that', 'here', 'there', 'now', 'then', 'also',
    'just', 'only', 'very', 'really', 'even', 'indeed', 'however', 'therefore',
    'furthermore', 'moreover', 'thus', 'so', 'and', 'but', 'or', 'if', 'because',
    'as', 'while', 'when', 'where', 'how', 'what', 'which', 'who', 'whom',
    'whose', 'why', 'we', 'us', 'our', 'ours', 'they', 'them', 'their', 'theirs',
    'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'you', 'your', 'yours',
    'i', 'me', 'my', 'mine', 'myself', 'ourselves', 'themselves', 'himself',
    'herself', 'itself', 'can', 'will', 'would', 'should', 'could', 'may', 'might',
    'must', 'have', 'has', 'had', 'do', 'does', 'did', 'being', 'been', 'is', 'am',
    'are', 'was', 'were', 'from', 'with', 'about', 'across', 'after', 'against',
    'along', 'among', 'around', 'at', 'before', 'behind', 'below', 'beneath',
    'beside', 'between', 'beyond', 'by', 'down', 'during', 'except', 'for', 'from',
    'in', 'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out',
    'outside', 'over', 'past', 'round', 'through', 'to', 'toward', 'towards',
    'under', 'underneath', 'until', 'up', 'upon', 'with', 'within', 'without',
    'about', 'above', 'below', 'across', 'already', 'always', 'another', 'anywhere',
    'around', 'become', 'becomes', 'certain', 'clearly', 'come', 'comes', 'consider',
    'considering', 'continue', 'continues', 'definitely', 'despite', 'develop',
    'developed', 'developing', 'different', 'doing', 'done', 'during', 'effect',
    'effective', 'effectively', 'either', 'else', 'ensure', 'ensuring', 'example',
    'examples', 'experience', 'experiences', 'fact', 'facts', 'feel', 'feeling',
    'finally', 'first', 'follow', 'following', 'force', 'forces', 'found',
    'general', 'generally', 'give', 'given', 'goes', 'going', 'gone', 'growth',
    'happens', 'high', 'hold', 'holds', 'home', 'hope', 'important', 'include',
    'includes', 'including', 'increase', 'increased', 'indeed', 'inside',
    'instead', 'interest', 'into', 'issue', 'issues', 'keep', 'keeps', 'known',
    'large', 'larger', 'least', 'left', 'level', 'levels', 'life', 'little',
    'long', 'look', 'looks', 'made', 'make', 'makes', 'making', 'means', 'member',
    'members', 'moment', 'most', 'name', 'need', 'needs', 'never', 'next', 'once',
    'order', 'part', 'particularly', 'place', 'places', 'point', 'points', 'power',
    'present', 'presented', 'problem', 'problems', 'process', 'processes',
    'provide', 'provided', 'provides', 'rather', 'reach', 'reaches', 'reason',
    'reasons', 'recent', 'recently', 'represent', 'represents', 'require',
    'requires', 'rest', 'right', 'run', 'runs', 'say', 'says', 'second', 'see',
    'seem', 'seems', 'seen', 'sense', 'set', 'sets', 'should', 'show', 'shows',
    'side', 'since', 'small', 'solution', 'solutions', 'something', 'sometimes',
    'start', 'starts', 'still', 'strong', 'sure', 'take', 'takes', 'telling',
    'terms', 'thank', 'thanks', 'think', 'thinking', 'thought', 'thoughts',
    'through', 'told', 'total', 'towards', 'true', 'truth', 'try', 'trying',
    'type', 'types', 'understand', 'understanding', 'unit', 'units', 'until',
    'use', 'used', 'uses', 'usually', 'value', 'values', 'various', 'want',
    'wants', 'way', 'ways', 'whether', 'whole', 'why', 'wide', 'wish', 'word',
    'words', 'work', 'works', 'world', 'would', 'yet', 'across', 'along', 'around',
    'away', 'back', 'come', 'down', 'forward', 'in', 'off', 'on', 'out', 'over',
    'round', 'through', 'up', 'well', 'whatsoever'
]

full_stopwords = standard_stopwords + additional_stopwords

# vectorizer_model = CountVectorizer(ngram_range  = (2, 2),
#                                    stop_words   = full_stopwords)

# # Generate a bigram topic model with 10 top terms and 8 topics
# topic_model = BERTopic(top_n_words          = 10,
#                           n_gram_range      = (2,2),
#                         #   nr_topics         = n_topics, # Number of topics to be generated
#                           vectorizer_model  = vectorizer_model,
#                           umap_model        = UMAP(random_state=1),
#                           verbose           = True)  


# # Fit model
# topics, probabilities = topic_model.fit_transform(docs)