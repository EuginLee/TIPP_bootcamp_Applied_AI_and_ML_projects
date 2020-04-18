# Natural Language Processing: topic modelling using LDA and NMF
Topic modeling is a frequently used text-mining tool for discovery of hidden semantic structures in a text body.
The "topics" produced by topic modeling techniques are clusters of similar words.  
  
For this project, we use news articles document and attempt to identify topics/themes in the corpus. 
    
  
We explore 2 methods here:  
1) LDA (Latent Dirichlet Allocation) method: select no. of topics, and allow the technique to map related words towards the topics. Probabilistic method.    
2) NMF (Non-Negative Matrix) method: same idea but uses a matrix factorisation method.


Optimisation: we optimised the number of topic by retrieving the max log likelihood and min perplexity. 
Visualisation: pyLDAvis

- Jupyter notebook: NLP_git.ipynb  
- News article Dataset: dataset folder
