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
 
The selected terms for individual topics can be visualised effectively through the generation of bar charts, which leverage the ```c-TF-IDF``` scores for each topic representation. This approach facilitates the acquisition of insights from the relative ```c-TF-IDF``` scores, both between and within topics. Furthermore, it enables a direct comparison of distinct topic representations.

<img width="1000" height="500" alt="Image" src="https://github.com/user-attachments/assets/dd1e5d3a-ccd2-4711-8696-b02213061f50" />


### 🗺️ Intertopic Distance Map

The Intertopic Distance Map serves to illustrate topic similarity and overlap within a two-dimensional space, aiding in the identification of related thematic clusters.

<img width="650" height="650" alt="Image" src="https://github.com/user-attachments/assets/912aaaa8-cabb-457c-80cb-259a19557e1f" />
  
  #### 📌 What you see:
  - A 2D scatterplot where each circle is a topic.
  - Position: Topics that are closer together are more similar.
  - Size: Shows the relative frequency (how many documents were assigned to that topic).

  #### ✅ Why it helps:
  - Helps you visually assess redundancy.
  - E.g., if two topics are close, they may be merged or refined.
  - You can spot dominant themes (large, far-apart topics = strong themes).

### 🔥 Topic Similarity (Heatmap)

This feature displays clusters of similar topics, offering optional reordering to enhance readability. Hovering over the graphical representation provides immediate insights into the degree of similarity between topics.

<img width="800" height="800" alt="Image" src="https://github.com/user-attachments/assets/44f37756-f786-4d26-9d72-d577c584326e" />


### 🌳 Topic Hierarchy

To comprehend the potential hierarchical structure of topics generated during the topic modelling phase, a dedicated hierarchy graph is created. By visualising this hierarchical order, it becomes possible to select an appropriate ```nr_topics``` value more effectively when reducing the total number of topics.

<img width="1000" height="380" alt="Image" src="https://github.com/user-attachments/assets/504b5f39-67c9-4db3-be5e-aa491a679a61" />

Hovering over the black circles within the graph reveals the topic representation at that specific hierarchical level. These representations are crucial for understanding the effect of merging certain topics, indicating where mergers might be logically coherent or, conversely, illogical. Furthermore, this visualisation clarifies which sub-topics are contained within broader thematic groupings.

### ⏳ Topics Over Time

Displays how frequently topics appear across specified time intervals, revealing trends.

<img width="1250" height="450" alt="Image" src="https://github.com/user-attachments/assets/aba7e7b8-0e7f-475a-8d58-7561d5c39afd" />

- **Y-axis** = how many documents linked to a topic per year.
- Detect peaks, declines, and political focus shifts.

### 🧬 Token Distribution Visualisation

The distribution of topic probabilities indicates BERTopic's confidence that specific topics are present within a document, rather than reflecting the frequency of those topics across the document. It primarily quantifies the model's certainty regarding a topic's relevance to a given text. The identified subjects exhibit clear definition and distinct separation. This is further corroborated by the intertopic distance map, which indicates minimal, if any, substantial overlap between themes.

---

## 🧠 Topic Insights & Interpretation

### 📊 **Topic Word Scores**
Each topic group together the most relevant keywords extracted from political speeches. Some key themes:

- **Topic 0**: Chechnya and regional conflict (e.g. *chechnya*, *republic*, *caucasus*).
- **Topic 1**: Military and security (*military*, *armed*, *defence*).
- **Topic 2**: War narratives and national memory (*war*, *victory*, *veterans*).
- **Topic 3**: Economy and business (*business*, *companies*, *investment*).
- **Topic 4**: Political institutions (*duma*, *elections*, *united*).
- **Topic 5**: Regional governance (*local*, *federal*, *regions*).
- **Topic 6**: Public services and fiscal policy (*budget*, *tax*, *development*).
- **Topic 7**: Geopolitical orientation (*region*, *far east*, *district*).

This suggests the speeches cover a broad spectrum — from domestic governance to foreign affairs and national identity.

### 🌐 **Hierarchical Clustering**
The dendrogram reveals how topics cluster based on semantic similarity:

- **Cluster 1**: Topics 0 (Chechnya) and 1 (Military) show a close relationship — indicating overlapping narratives around conflict and security.
- **Cluster 2**: Topics 4 (Politics), 5 (Local governance), and 6 (Budget) are grouped — reflecting domestic administrative focus.
- **Cluster 3**: Topics 3 (Business) and 7 (Geopolitics) cluster together, possibly highlighting economic development in regional contexts.
- **Cluster 4**: Topic 2 (War) is relatively distinct but still shares some distance with broader nationalist themes.

These patterns reveal how Russian political discourse intertwines themes of national identity, military strength, economic policy, and governance.

### ⏳ Topics Over Time

The chart below illustrates the evolution of the frequency of specific topics from 2000 to 2020.

**Key Observations:**
- 🟠 **Elections & Politics** (Topic 4) peaked around 2003–2005 and again in 2008–2010 — aligning with major electoral cycles.
- 🟡 **Chechnya & Conflict** (Topic 0) was dominant in the early 2000s, reflecting heightened discourse around regional instability.
- 🟢 **War & Memory** (Topic 2) shows a strong resurgence post-2005 and 2020 — possibly tied to commemorative anniversaries.
- 🔵 **Military & Security** (Topic 1) and 🟢 **Business & Economy** (Topic 3) remained relatively steady, showing ongoing attention to defence and development.

📌 **Insight**: Shifts in topic prominence reveal how national priorities and narratives have changed over time, often influenced by elections, anniversaries, and external events.

---

## ✅ Conclusion

**BERTopic** is a powerful, customisable NLP tool that excels in:
- Understanding long and short texts semantically.
- Producing interpretable topic clusters.
- Providing rich, interactive visualisations.

This project serves as a solid template for applying BERTopic to political data and can be extended to domains like finance, news, or customer feedback.

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

```bash
├── notebooks/
├── data/
├── images/
├── src/
     └── modules
├── README.md
└── requirements.txt
```

---

## 👨‍💻 Author

Developed with ❤️ by **Alberto AJ**, AI/ML Engineer  
📌 [GitHub](https://github.com/AlbertoGhub) • [LinkedIn](https://www.linkedin.com/in/engineeralbertoac/)

---

## 📚 References

- Koráb, P. (2024). *Topic Modelling with BERTopic in Python*.  
- Gong, D. (2025). *BERTopic: Transformer-Based Topic Modelling*.  
- Grootendorst, M. (2023). *BERTopic Documentation*.  
- Efat et al. (2023). *Empoliticon Dataset*.
