# Read data with python
    import pandas as pd
    data = pd.read_excel("file_name", index_col=0)
The column name is presented as "qubit1_index-qubit2_index" where "qubit1" and "qubit2" are the corresponding qubits to perfrom two-qubit CZ gate.