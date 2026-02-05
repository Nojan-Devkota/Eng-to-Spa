# English-to-Spanish Translator Project

This project focuses on building a neural translation model to bridge the gap between English and Spanish communication. While the current model provides a solid baseline, it is currently limited by the simplicity and scope of the initial training data.

## ⚠️ Current Limitations & Drawbacks

The primary hurdle in the model's current performance is the **simplicity of the dataset**. Because the training data consists largely of short, direct sentences, the model faces the following challenges:

* **Contextual Blindness:** The model struggles with words that have multiple meanings depending on the context, as the current data does not provide enough surrounding information.
* **Structural Rigidity:** It performs well on simple Subject-Verb-Object sentences but fails to maintain grammatical integrity in long, multi-clause, or complex sentences.
* **Lack of Idiomatic Understanding:** Natural speech often uses idioms or cultural expressions that are currently absent from the data, leading to "robotic" or overly literal translations.
* **Formal vs. Informal Nuance:** The data does not sufficiently distinguish between formal (*usted*) and informal (*tú*) Spanish, often defaulting to a single form regardless of the social context.

## 🚀 Solutions: How to Improve the Model

To evolve this project into a robust, real-world translation tool, the following data-centric improvements are planned:

### 1. Data Diversification
We need to move beyond simple imperatives and greetings. The next phase involves integrating datasets like **Europarl** or **UN Corpora**, which contain complex political, legal, and social discourse. This will teach the model to handle varied sentence lengths and sophisticated vocabulary.

### 2. Integration of Real-World Narratives
By including data from literature, news articles, and subtitles, the model can learn:
* **Natural Flow:** How sentences connect in a paragraph.
* **Slang and Idioms:** How to translate common phrases that don't have a literal equivalent.

### 3. Subject-Specific Fine-Tuning
Training on niche datasets (Medical, Technical, or Legal) will allow the model to provide accurate translations for specialized fields where precision is critical.

### 4. Synthetic Data Augmentation
Using "Back-Translation" techniques—where we translate Spanish back into English to create new training pairs—can help the model see more varied ways to express the same thought, reducing the risk of it memorizing specific, rigid patterns.

## Data Source
The current training corpus is derived from the **Tatoeba Project** (via ManyThings.org).