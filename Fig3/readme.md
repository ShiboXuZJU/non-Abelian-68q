# Read data with python
    import pandas as pd
    data = pd.read_excel("file_name", index_col=0)
# NOTE
## Fig3c
Some experimental data in Fig3c.xlsx contain "and" in "index_name" which means experiments described in "index_name" share the same experimental data.

For example, "|00> and CX|00> and CXCX|00> -ic1c2" means measuring "-ic1c2" ($\langle-ic_1c_2\rangle$) in different logical state "|00>", "CX|00>" and "CXCX|00>" have the same experimental circuit and thus have the same experimental data.