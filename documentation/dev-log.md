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
- Completed phase 2 and 3
- Tested the program and am getting 1000/1000 errors. Working on a fix
- Found the fix: The iterations for metric Eigenvector Centrality had a maximum of 100 iterations. This was increased to 1000 to account for large graphs
- Additional errors were caused by python 2 in the dataset. This was fixed by creating a preprocessing stage that attempts to convert the files to python 3 