import eel

from tkinter import Tk
import tkinter.filedialog
import os
import datetime
import time
import traceback

from sklearn.linear_model import LogisticRegression
import pandas as pd

# Set web files folder
eel.init("web")


@eel.expose
def run_ml(filepath):
    try:
        train_df = pd.read_excel(filepath, sheet_name="train")
        model = LogisticRegression()
        model.fit(train_df.drop("target", axis=1), train_df["target"])
        predict_df = pd.read_excel(filepath, sheet_name="predict")
        with pd.ExcelWriter(filepath, mode="a") as writer:
            pd.DataFrame({"predict": model.predict(predict_df)}).to_excel(
                writer, sheet_name="output", index=False
            )

        return "true"
    except Exception as e:
        return "".join(traceback.TracebackException.from_exception(e).format())


@eel.expose
def ask_file():
    # file_flags consists of tuple of tuples, i.e. (("jpeg files", "*.jpg"), ("all files", "*.*))
    try:
        root = Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        file_path = tkinter.filedialog.askopenfile(
            initialdir=os.path.expanduser("~/Desktop"),
            title="Select File",
            filetypes=[("テキストファイル", "*.xlsx")],
        )
        return file_path.name
    except:
        return None


eel.start("index.html", size=(600, 400))  # Start
