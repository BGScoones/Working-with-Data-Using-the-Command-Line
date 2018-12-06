import pandas as pd

def load_data():
    data = pd.read_csv("/home/dq/scripts/hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
    # The names keyword adds column names to the DataFrame.
    return data
    
if __name__ == "__main__":
    data = load_data()