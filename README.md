# Topic Modelling with BERTopic: Political Speech Analysis

## Overview

Topic modelling with BERTopic represents a state-of-the-art, transformer-based method for uncovering meaningful themes within large text corpora, such as political speeches or financial news. Unlike classical approaches like Latent Dirichlet Allocation (LDA), which rely on the bag-of-words assumption and often fail to capture semantic relationships between words, BERTopic leverages pre-trained language models to produce semantically rich embeddings. These embeddings are subsequently reduced in dimensionality and clustered to form coherent, interpretable topics. This embedding-based approach consistently outperforms many traditional and modern topic models across diverse datasets and domains.

### BERTopic's architecture consists of six modular components:

1. **Embeddings:** Transform text into semantic vector representations using sentence-transformer models.
2. **Dimensionality Reduction:** Compress high-dimensional embeddings into a lower-dimensional space (using techniques like UMAP or PCA) while preserving relationships.
3. **Clustering:** Group similar documents into distinct topics using algorithms such as HDBSCAN or K-Means.
4. **Vectorizers:** Convert text into numerical features for topic analysis, e.g., count vectorizer or online vectorizer.
5. **c-TF-IDF:** Compute term importance scores within and across topics to identify key terms.
6. **Representation Model:** Use semantic similarity between candidate keywords and document embeddings to select the most representative topic keywords, sometimes leveraging LLMs or KeyBERT.

This modular design allows flexible customisation tailored to different use cases such as survey analysis, document tagging, and content organisation, making BERTopic a powerful and cost-effective unsupervised learning tool in NLP.

## Project Summary

This project demonstrates how to apply BERTopic to political speech transcripts to extract meaningful topics and track their evolution over time. It covers data preprocessing, model building, topic visualisation, and interpretation of results.

### About the Dataset

This project utilises the Empoliticon: Political Speeches – Context & Emotion dataset. Released under the Attribution 4.0 International License, this dataset forms part of the Efat et al. (2023) study and comprises 2,010 transcripts of political speeches delivered by presidents and prime ministers from the USA, UK, China, and Russia. To maintain focus and coherence, this initial version (MVP) concentrates on a subset of 556 speeches from Russian leaders. Future iterations aim to introduce an interactive dropdown feature alongside the Streamlit library to select speeches from other countries, thereby broadening the analysis scope.

## How to Use

This project's methodology follows a structured approach, broken down into the following key stages:

1. **Data Preparation**  
   - The textual corpus undergoes thorough cleansing and preprocessing.
   - Timestamps are standardised to ensure consistency, facilitating robust temporal analysis.

2. **BERTopic Model Construction**  
   - Pre-trained semantic embedding models, such as those available via the SentenceTransformer library, are leveraged to generate context-rich document embeddings.
     - A comprehensive array of suitable models is accessible from both the [Sentence Transformers](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) website and the [Hugging Face model hub](https://huggingface.co/models), enabling their loading and utilisation with minimal code to encode textual sequences into high-dimensional numerical embeddings.
     - For this project, the ```msmarco-distilbert-cos-v5``` model was specifically chosen due to its enhanced semantic capabilities, aiming for greater accuracy. This stage offers considerable flexibility, allowing for the testing and selection of various models to tailor the results to specific analytical objectives.
   - Vectorizer parameters are carefully configured to optimise the distinctiveness of the generated topics.
   - Dimensionality reduction techniques and clustering algorithms are subsequently applied.

3. **Topic Exploration**  
   - Visualisations are employed to display top terms and exemplary documents associated with each identified topic.
   - Analytical tools, including intertopic distance maps, heatmaps, and temporal topic trend visualisations, are utilised for deeper insights.

4. **Results Interpretation**  
   - Insights are derived from examining topic overlaps and identifying distinct thematic groupings.
   - The evolution of topic prevalence over different years is rigorously analysed.
---

## Key Visualisations

- **Term Visualisation:**
The selected terms for individual topics can be visualised effectively through the generation of bar charts, which leverage the ```c-TF-IDF``` scores for each topic representation. This approach facilitates the acquisition of insights from the relative c-TF-IDF scores, both between and within topics. Furthermore, it enables a direct comparison of distinct topic representations.

- **Intertopic Distance Map:**  
  Visualises topic similarity and overlap in a 2D space, helping identify related topics.

- **Topic Heatmap:**  
  Shows topic similarity clusters with optional reordering for better readability.

- **Topics Over Time:**  
  Displays how frequently topics appear across specified time intervals, revealing trends.

Source: [BERTopic - Visualisations](https://maartengr.github.io/BERTopic/getting_started/visualization/visualization.html)









