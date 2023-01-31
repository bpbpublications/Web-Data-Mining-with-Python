dataset = [
    ["Milk", "Eggs", "Bread", "Butter"],
    ["Milk", "Butter", "Eggs", "Apple"],
    ["Milk", "Eggs", "Bread"],
    ["Bread", "Butter"],
    ["Eggs", "Apple"],
]
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)
from mlxtend.frequent_patterns import apriori

frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)
from mlxtend.frequent_patterns import association_rules
rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.8)
