# Read data with python
    import pandas as pd
    data = pd.read_excel("file_name", index_col=0)
The column name is presented as "prefix-qubit1_index-qubit2_index-...". "Prefix" is the type of the stabilizer such as "e", "m" and "D". "Qubit_index" represents an element qubit of the stabilizer.

# NOTE
## Fig2b
The first line experimental data in Fig2b right is same with Fig2a (ground state). The following experimental data is recorded in Fig2b.xlsx with 4 sheets named "generate e", "surround 1 twist", "surround 2 twists" and "surround 3 twists", respectively