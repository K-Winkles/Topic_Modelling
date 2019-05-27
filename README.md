# Topic_Modelling
LDA and NMF applied to two different data sets. 

The two datasets in question are:
1. Wikipedia Data - to be extracted with SQLite.
2. Stratpoint website articles - to be extracted using Scrapy. 

Task overview:
Apply LDA and NMF to both datasets and compare the results of a large dataset (say 100K entries) versus a smaller dataset (1K).

1. Data Extraction
      Web scraping for the first data set and database access for the second data set will have to be learned for this task. 
2. Data Analysis
      Latent Dirichlet Allocation and Non-negative Matrix Factorization are easy to apply with scikit-learn. More effort goes into actually extracting the data.
3. Data Visualization
      This will be in table form since the results are meant to describe probability distributions.
