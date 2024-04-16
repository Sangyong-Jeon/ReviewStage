from interpark_scraping import *
import pandas as pd
if __name__ == "__main__":
    info = pd.read_csv("../data/infodata/info.csv", encoding="utf-8")

    for i in info.iterrows():
        if i[1]["title"] in ["브론테", "영웅", "오즈"]:
            continue
        print(i[1]["title"], i[1]["type"], i[1]["key"])
        interpark_scraping(i[1]["title"], i[1]["type"], i[1]["key"])
