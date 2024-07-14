import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

users_df = pd.read_csv(
    "ml-100k/u.user",
    sep="|",
    names=["user_id", "age", "gender", "occupation", "zip_code"],
)

items_df = pd.read_csv(
    "ml-100k/u.item",
    sep="|",
    names=[
        "item_id",
        "movie_title",
        "release_date",
        "video_release_date",
        "IMDb_URL",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ],
    encoding="latin-1",
)

ratings_df = pd.read_csv(
    "ml-100k/u.data",
    sep="\t",
    names=["user_id", "item_id", "rating", "timestamp"],
)

items_genre_df = items_df[
    [
        "item_id",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ]
]

items_genre_df = pd.melt(
    items_genre_df, id_vars=["item_id"], var_name="genre", value_name="Value"
)
items_genre_df = items_genre_df[items_genre_df["Value"] == 1]
items_genre_df.drop(columns=["Value"], inplace=True)

genre_encoder = LabelEncoder()

items_genre_df["genre_id"] = genre_encoder.fit_transform(items_genre_df["genre"])

genre_df = items_genre_df[["genre_id", "genre"]].drop_duplicates()


items_genre_df.drop(columns=["genre"], inplace=True)

items_df.drop(
    columns=[
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
        "IMDb_URL",
        "video_release_date",
    ],
    inplace=True,
)

user_items_df = ratings_df.drop(columns=["timestamp"])

print(items_df)
print(users_df)
print(genre_df)
print(items_genre_df)
print(user_items_df)


folder_path = "neo4j_csv"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

items_df.to_csv(os.path.join(folder_path, "items.csv"), index=False)
users_df.to_csv(os.path.join(folder_path, "users.csv"), index=False)
genre_df.to_csv(os.path.join(folder_path, "genre.csv"), index=False)
items_genre_df.to_csv(os.path.join(folder_path, "items_genre.csv"), index=False)
user_items_df.to_csv(os.path.join(folder_path, "user_items.csv"), index=False)
