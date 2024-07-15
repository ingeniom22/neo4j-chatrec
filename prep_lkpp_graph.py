import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ppk_encoder = LabelEncoder()

lkpp_reviews_df = pd.read_csv("lkpp_dataset_clean.csv", sep=";")
lkpp_reviews_df["ppk_id"] = ppk_encoder.fit_transform(lkpp_reviews_df["ppk_id"])
# lkpp_reviews_df.drop(columns=["Sum", "Rescalling"], inplace=True)
lkpp_reviews_df = lkpp_reviews_df[
    [
        "ppk_id",
        "company_id",
        "timestamp",
        "Rescalling",
        "category",
    ]
]

company_df = pd.read_json("company_identity.jsonl", lines=True)

print(lkpp_reviews_df.head())
print(company_df.head())

lkpp_reviews_df.to_csv("neo4j_lkpp/ppk_company.csv", index=False)
company_df.to_csv("neo4j_lkpp/companies.csv", index=False)
