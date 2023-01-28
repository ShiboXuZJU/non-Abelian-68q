# Read data with python
    import pandas as pd
    data = pd.read_excel("file_name", index_col=0)
The column name is presented as "prefix-qubit1_index-qubit2_index-...". "Prefix" is the type of the stabilizer. "Qubit_index" represents an element qubit of the stabilizer.
