# mini-search-engine-based-on-tf-idf
A mini search engine for wikipedia dump.

Steps followed:
- parsing the dataset
- making mini index files 
- merging the index file into global index file using external merge sort. Making a secondary index containing the offset
  in globbal index file
- given a query. finding top relevant documents based on tf-idf model.
