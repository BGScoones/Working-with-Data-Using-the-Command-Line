import read

data = read.load_data() 

import pandas as pd

if __name__ == "__main__":
    domain_count = data["url"].value_counts()
    for domain, row in domain_count[:99].items():
        print("{0}: {1}".format(domain, row))
    # One issue with the above code is that subdomains are counted as unique domains, rather than as the parent domain.
    # I have been unable to find a consistent solution.
    # One approach is to remove the portion of the url prior to the first ".", if the number of "." is 2 or greater.
    # However, this renders domain names such as bbc.co.uk simply co.uk, and so is unsuccessful.
    # The only solution I can think of is to create a list of all unique domains with "." count >= 2, and then use a regex to filter these domains out.
