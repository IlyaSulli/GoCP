# Dev Log
## 17th March
- Started work on project, building Graph-of-Code for Python instead of Java.
- Started to install BigCloneEval but realised it was Java only so switching to SemanticCloneBench which has been manually validated (https://ieeexplore.ieee.org/document/9047643)
- Factored code to have main function which allows you to assign data and results directories
- main.py file looks at each data python file and looks for two of the same function names in it. It then extracts each and puts them in variables
- Started work on goc (Graph-of-Code) file. Parses function into AST tree and looks for operation nodes and variable nodes
## 18th March
- Finished GoC:
     1. Parse AST
     2. Walk and collect non-terminal nodes
     3. Build edge list from parent-child relationships
     4. Weight the edges by frequency
     5. Return the constructed graph
- Updated the file log to use a progress bar to reduce information overload
- Started work on generating features set from constructed tree in goc.py . I am working on phase 1: node feature extraction
- Tested the program and am getting 1000/1000 errors. Working on a fix
- Found the fix: The iterations for metric Eigenvector Centrality had a maximum of 100 iterations. This was increased to 1000 to account for large graphs
- Additional errors were caused by python 2 in the dataset. This was fixed by creating a preprocessing stage that attempts to convert the files to python 3
- Running additional checks found that preprocessing was taking significant time so the current implementation needs to be looked at in the future. (Currently 37s)
- Updated features.py to have phase 2: graph-level features
- Updated features.py to have phase 3: creating fixed-size stats
- Fixed the pre-processing slow-down by using a ProcessPoolExecutor, allowing processes to run simultaneously. Now takes 10 seconds to do inital steps
- Created the classifer (uses scikit-learn). Current stats are 
    - "Average : Precision=0.5958  Recall=0.5957  F1=0.5955"
- Added additional feature vectors to help the model tell how far apart the metrics are. Current stats are 
    - "Average: Precision=0.6399  Recall=0.6282  F1=0.6326"
- Implemented TF-IDF as the baseline test
- Tested the program and found that the baseline beats it with TF-IDF having an:
    - "Average : Precision=0.8308  Recall=0.8197  F1=0.8249"
- The problem is caused by a small training set and a large number of features. A bigger dataset is needed. Looked into  "Datasets:PoolC/1-fold-clone-detection-600k-5fold" on HuggingFace which contains 600,000 entries which would help a lot for this (uses datasets)
- Attempted run of 100,000 pairs. Current sats are:
    - Average : Precision=0.7327  Recall=0.7841  F1=0.7575
    - TFIDF failed "numpy._core._exceptions._ArrayMemoryError: Unable to allocate 704. KiB for an array with shape (90060,) and data type float64"
- Working on fix for TFIDF by increasing max_features to 5000
- Working on fix to improve repetetive training tests by storing the processed pairs
- Added progress bar to baseline to help with large datasets
- Added --no-goc argument to allow you to just run the baseline. Added --reprocess argument to force reload the processed clone pairs just in case the data is altered slightly
- Loading files from cache was loading half quickly but the rest was being lNow uses Pickle cache to load files even quicker.
- Fixed progress bar for baseline
- Tested baseline. Results in: Average : Precision=0.9101  Recall=0.8829  F1=0.8963
- Updated classifier to include similarity feature and feature scaling
- Tested GoS. Results in: Average : Precision=0.7326  Recall=0.7914  F1=0.7608