# 🧠 Topic Modelling with BERTopic: Political Speech Analysis

## 📌 Overview

This project applies **BERTopic**, a state-of-the-art transformer-based topic modelling technique, to uncover patterns in political speeches. Unlike traditional models like LDA that rely on bag-of-words, BERTopic captures the semantic richness of text through language model embeddings, dimensionality reduction, clustering, and term scoring.

🔍 We analyse speeches to:
- Preprocess and clean political texts.
- Extract dominant themes.
- Explore how topics evolve over time.

🔧 **Modular architecture** includes:
1. **Embeddings** – via [Sentence Transformers](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)
2. **Dimensionality Reduction** – UMAP/PCA
3. **Clustering** – HDBSCAN / K-Means
4. **Vectorisation** – Count/Online Vectoriser
5. **c-TF-IDF** – for topic-term weighting
6. **Topic Representation** – KeyBERT or LLM-based

---

## 📚 Dataset

We utilise the "Empoliticon: Political Speeches – Context & Emotion" dataset by Efat et al. (2023), which comprises 2,010 transcripts from global leaders. This MVP focuses on **556 Russian leader speeches**, with plans to integrate a dropdown selection for other countries using Streamlit.

---

## 🛠️ Workflow

### 1. 🔄 Data Preparation
- Cleaning and formatting of transcripts.
- Timestamp normalisation for temporal analysis.

### 2. 🧱 BERTopic Model
- Embeddings from `msmarco-distilbert-cos-v5`.
- Custom vectoriser config and clustering via HDBSCAN.
- Topic generation with semantic-rich embeddings.

### 3. 🔍 Topic Exploration
- Top terms per topic.
- Interactive and temporal visualisations.
- Topic similarity and overlap insights.

### 4. 🧠 Interpretation
- Clear topic clusters.
- Temporal trend patterns (e.g., peaks in political concern).

---

## 📊 Key Visualisations

### 📌 Term Representation per Topic
 Visualised using bar charts of `c-TF-IDF` scores.


[Term Visualisation](images/1_Barchart_topic_visualisation.html)

---

## Concept clarification



---

### 🗺️ Intertopic Distance Map
> pyLDAvis-style 2D scatterplot of topic similarity.
![Distance Map](../images/2_BIntertopic_Distance_Map.html)

- **Position**: Similar topics cluster together.
- **Size**: Reflects topic frequency.

---

### 🔥 Topic Similarity (Heatmap)
> Hover to explore related clusters.
![Heatmap](../images/3_Heatmap_topic_visualisation.html)

---

### 🌳 Topic Hierarchy
> Understand topic structure and optimal `nr_topics` setting.
![Hierarchy](../images/4_Hierarchical_Topic_Visualisation.html)

---

### ⏳ Topics Over Time
> Track topic frequency trends over years.
![Over Time](../images/5_Topics_over_time_visualisation.html)

- **Y-axis** = how many documents linked to a topic per year.
- Detect peaks, declines, and political focus shifts.

---

### 🧬 Token Distribution Visualisation
> Examine BERTopic’s token-level certainty for a document.
![Token Distribution](../images/6_token_distribution_visualisation.html)

---

## 🧾 Results Interpretation

- Topics show semantic clarity and minimal overlap.
- Time-based topic trends mirror historical political changes.
- Hierarchical view reveals sub-topics and theme consolidation.

---

## ✅ Conclusion

**BERTopic** is a powerful, customisable NLP tool that excels in:
- Understanding long and short texts semantically.
- Producing interpretable topic clusters.
- Providing rich, interactive visualisations.

This project serves as a solid template for applying BERTopic to political data—and can be extended to domains like finance, news, or customer feedback.

---

## 🔭 Future Improvements

- Integrate dropdown menu (via Streamlit) to filter speeches by country.
- Enable search by keyword to explore speech clusters.
- Automate topic name generation using LLM summarisation.
- Enable live topic tracking with updated speech datasets.

---

## 🧪 Tech Stack

- 🐍 Python (BERTopic, pandas, UMAP, HDBSCAN)
- 🤗 Hugging Face Models
- 📊 Plotly, Matplotlib
- 🧱 Sentence-Transformers

---

## 📁 Project Structure

```plaintext
├── notebooks/
├── data/
├── images/
├── app.py
├── README.md
└── requirements.txt


---

## 👨‍💻 Author

Developed with ❤️ by **Alberto AJ**, AI/ML Engineer  
📌 [GitHub](https://github.com/AlbertoGhub) • [LinkedIn](https://www.linkedin.com/in/albertoavendano)

---

## 📚 References

- Koráb, P. (2024). *Topic Modelling with BERTopic in Python*.  
- Gong, D. (2025). *BERTopic: Transformer-Based Topic Modelling*.  
- Grootendorst, M. (2023). *BERTopic Documentation*.  
- Efat et al. (2023). *Empoliticon Dataset*.




--------------------


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

---

## Project Summary

This project demonstrates how to apply BERTopic to political speech transcripts to extract meaningful topics and track their evolution over time. It covers data preprocessing, model building, topic visualisation, and interpretation of results.

### About the Dataset

This project utilises the Empoliticon: Political Speeches – Context & Emotion dataset. Released under the Attribution 4.0 International License, this dataset forms part of the Efat et al. (2023) study and comprises 2,010 transcripts of political speeches delivered by presidents and prime ministers from the USA, UK, China, and Russia. To maintain focus and coherence, this initial version (MVP) concentrates on a subset of 556 speeches from Russian leaders. Future iterations aim to introduce an interactive dropdown feature alongside the Streamlit library to select speeches from other countries, thereby broadening the analysis scope.

---


## How to Use

This project's methodology follows a structured approach, broken down into the following key stages:

1. **Data Preparation**  
   - The textual corpus undergoes thorough cleansing and preprocessing.
   - Timestamps are standardised to ensure consistency, facilitating robust temporal analysis.

2. **BERTopic Model Construction**  
   - Pre-trained semantic embedding models, such as those available via the SentenceTransformer library, are leveraged to generate context-rich document embeddings.
     - A comprehensive array of suitable models is accessible from both the [Sentence Transformers](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html) website and the [Hugging Face model hub](https://huggingface.co/models), enabling their loading and utilisation with minimal code to encode textual sequences into high-dimensional numerical embeddings.
     - For this project, the 
msmarco-distilbert-cos-v5
 model was specifically chosen due to its enhanced semantic capabilities, aiming for greater accuracy. This stage offers considerable flexibility, allowing for the testing and selection of various models to tailor the results to specific analytical objectives.
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

- **Term Visualisation:** The selected terms for individual topics can be visualised effectively through the generation of bar charts, which leverage the 
c-TF-IDF
 scores for each topic representation. This approach facilitates the acquisition of insights from the relative c-TF-IDF scores, both between and within topics. Furthermore, it enables a direct comparison of distinct topic representations.

    NEEDS TO BE CHECKED

    ![Term Visualisation](../images/1_Barchart_topic_visualisation.html)

- **Intertopic Distance Map:**  Visualises topic similarity and overlap in a 2D space, helping identify related topics.
    ### 🔍 What it does:
    This generates the Intertopic Distance Map using pyLDAvis-style visualisation.

    TO BE CHECKED

    ![Intertopic Distance Map](../images/2_BIntertopic_Distance_Map.html)

    ### 📌 What you see:
    - A 2D scatterplot where each circle is a topic.
    - Position: Topics that are closer together are more similar.
    - Size: Shows the relative frequency (how many documents were assigned to that topic).

    ### ✅ Why it helps:
    - Helps you visually assess redundancy.
    - E.g., if two topics are close, they may be merged or refined.
    - You can spot dominant themes (large, far-apart topics = strong themes).


    This interactive visualisation typically includes features such as a slider, allowing for the selection of a specific topic, which is then highlighted (e.g., in red). Hovering over any topic bubble provides additional general information, including its size (prevalence) and corresponding key terms.

- **Topic Similarity Visualisation (Heatmap):** This feature displays clusters of similar topics, offering optional reordering to enhance readability. Hovering over the graphical representation provides immediate insights into the degree of similarity between topics.

    ![Heatmap]("../images/3_Heatmap_topic_visualisation.html")

- **Topic Hierarchy:** The hierarchy graph is generated to provide the potential hierarchical structure of topics, to help in the selection of an appropriate 
nr_topics
 value during topic reduction (if needed).

    ![Hierarchy]("../images/4_Hierarchical_Topic_Visualisation.html")
    
    Hovering over the nodes within the graph reveals topic representations at each hierarchical level. This functionality clarifies the implications of topic merging, indicating logical consolidations, and highlights sub-topics contained within broader themes.

- **Topics Over Time:**  Displays how frequently topics appear across specified time intervals, revealing trends.
  
  ![TopicsOverTime]("../images/5_Topics_over_time_visualisation.html")
  
  ### Understanding Frequency on the Y-Axis: 
  The frequency on the y-axis in the Topics over Time graph, generated by 
topic_model.visualize_topics_over_time()
, quantifies how often a particular topic appears in documents within a given time period. More precisely, this is determined by:
  
    - ***Document Assignment:*** For each defined time interval (e.g., year, month, or quarter), BERTopic assesses how many documents are primarily assigned to each specific topic.
    
    - ***Counting Occurrences:*** It then tallies the number of times each topic is the dominant theme across all documents published or created within that particular time window.
    
    - ***Visual Representation:*** This count (or sometimes a normalised proportion, depending on the model's configuration) is subsequently plotted on the y-axis, illustrating the topic's prevalence during that period.

    #### Practical Example: 📈

    Consider a dataset spanning from 2010 to 2024:

    - If, in 2012, Topic 3 is the primary theme in 42 documents, its frequency for that year would be 42.
    - Conversely, if in 2015, Topic 3 appears in only 12 documents, its frequency would be 12 for that year.
    - Consequently, the line representing Topic 3 on the graph would show a higher point in 2012 and a lower point in 2015, visually reflecting its changing prevalence over time.

    Consequently, the line representing Topic 3 on the graph would show a higher point in 2012 and a lower point in 2015, visually reflecting its changing prevalence over time.

- **Topic Probability Distribution:** This visualisation allows for the scrutiny of individual token contributions to specific topics, providing insights into their defining characteristics.

  ![TopicDistribution]("../images/6_token_distribution_visualisation.html")
  
  The distribution of topic probabilities indicates BERTopic's confidence that specific topics are present within a document, rather than reflecting the frequency of those topics across the document. It primarily quantifies the model's certainty regarding a topic's relevance to a given text.

The identified subjects exhibit clear definition and distinct separation. This is further corroborated by the intertopic distance map, which indicates minimal, if any, substantial overlap between themes.

Source: [BERTopic - Visualisations](https://maartengr.github.io/BERTopic/getting_started/visualization/visualization.html)



## Results Interpretation


## Conclusion

BERTopic offers an advanced and flexible approach to topic modelling, combining transformer embeddings with traditional NLP techniques. It excels in capturing semantic relationships, handling short and long texts, and providing insightful visualizations to support qualitative analysis of text corpora.

This project provides a practical template for using BERTopic on political speech data but is adaptable to various domains including finance, social media, and customer feedback.

---

## References

- Koráb, Petr. "Topic Modelling with BERTopic in Python." *Medium*, Apr 1, 2024.  
- Gong, Destin. "BERTopic: Transformer-Based Topic Modeling." *Medium*, May 8, 2025.  
- Grootendorst, Maarten. *BERTopic Documentation*.  
- Chagnon, [2024], *Academic Application of BERTopic*.

---

🧪 Technology Used

📁 Project Structure

🚀 Future Improvements

👨‍💻 Author

👨‍💻 Author Developed with ❤️ by Alberto AJ, AI/ML Engineer

📌 Visit my GitHub • LinkedIn
