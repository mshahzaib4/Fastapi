from fastapi import FastAPI
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse


app = FastAPI()

df = sns.load_dataset("titanic")
df.drop(columns=["deck", "embark_town", "alive"], inplace=True)
df.dropna(inplace=True)

survival_rate = df.groupby("class")["survived"].mean().reset_index()

@app.get("/")
async def read_root():
    return {"Titanic Dataset": "Welcome to the Titanic dataset API!"}

@app.get("/survival_rate")
async def get_survival_rate():
    return {"Survival Rate": survival_rate.to_dict(orient="records")}

@app.bar_plot("/survival_rate_plot")
async def bar_plot():
    sns.barplot(x="class", y="survived", data=survival_rate)
    plt.title("Survival Rate by Class")
    plt.xlabel("Class")
    plt.ylabel("Survival Rate")
    plt.savefig("survival_rate_plot.png")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return StreamingResponse(buf, media_type="image/png")