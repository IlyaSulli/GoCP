# Dev Log
## 17th March
- Started work on project, building Graph-of-Code for Python instead of Java.
- Started to install BigCloneEval but realised it was Java only so switching to SemanticCloneBench which has been manually validated (https://ieeexplore.ieee.org/document/9047643)
- Factored code to have main function which allows you to assign data and results directories
- main.py file looks at each data python file and looks for two of the same function names in it. It then extracts each and puts them in variables
- Started work on goc (Graph-of-Code) file. Parses function into AST tree and looks for operation nodes and variable nodes 