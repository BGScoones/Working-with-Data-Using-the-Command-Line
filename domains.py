import read

data = read.load_data() 

import pandas as pd

if __name__ == "__main__":
    domain_count = data["url"].value_counts()
    for domain, row in domain_count[:99].items():
        print("{0}: {1}".format(domain, row))