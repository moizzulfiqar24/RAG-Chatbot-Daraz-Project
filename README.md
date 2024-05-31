# RAG-Based Project for eCommerce Platform

This repository houses the implementation of a RAG (Retriever-Augmented Generation) based project aimed at enhancing eCommerce platforms through sophisticated text analytics. Developed as part of the Intro to Text Analytics course, the project is segmented into three pivotal phases:

1. **Data Collection:** Executed through detailed multi-stage scraping of the Daraz eCommerce website.
2. **Retriever Phase:** Involves preprocessing and cleaning the scraped data, followed by the development of an advanced retriever for efficient information filtering based on user queries.
3. **LLM Phase:** Utilizes large language models (LLMs) to generate natural language responses derived from the information retrieved in the previous phase.

## Repository Structure

- `Data/` - Contains only the raw data files, which were collected via detailed scraping of the Daraz website.
- `Evaluation/` - Scripts and metrics for evaluating the quality of the retriever and the outputs of the LLMs.
- `LLM Chats/` - Scripts used for interfacing with LLMs to produce responses to user queries.
- `chromaDB9/` - A vector database repository used for retrieving documents relevant to user queries.
- `Retriever.ipynb` - A Jupyter notebook containing the retriever code.

## Setup and Installation

Ensure the following prerequisites are installed to run the code in this repository:

- Libraries: `sentence_transformers`, `numpy`, `torch`, `gensim`, `langchain`, `spacy`, `pandas`, `re`

## Usage

Modify the `query` and `searchType` in `Retriever.ipynb` to suit your query needs and run the notebook cells sequentially to observe the retriever's outputs for different types of queries.

## Retriever Details

The retriever module is designed to handle various query types by adjusting the `searchType` and `query`. Example configurations:

```python
searchType = "Product"
query = "Can you list watches between Rs. 1000 and Rs. 2000?"
```

Advanced techniques like sentence embeddings and vector databases (chromaDB) are utilized to efficiently retrieve relevant information.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your suggestions for improvements or bug fixes.

## Acknowledgments

- Special thanks to Dr. Sajjad Haider, Professor in the Department of Computer Science at IBA Karachi, for his invaluable guidance and support throughout the development of this project.