from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd

df = pd.DataFrame(
    [
        [1.4, "one", "common"], [1.5, "one", "common"], [1.6, "one", "vip"], [1.5, "one", "vip"], [1.6, "one", "vip"],
        [1.7, "one", "vip"],
        [0.1, "two", "lamb"], [0.2, "two", "lamb"], [0.3, "two", "lamb"], [0.4, "two", "lamb"], [0.5, "two", "lamb"],
        [0.6, "two", "common"]
    ],
    columns=["rate", "type", "rank"]
)

if __name__ == '__main__':
    model = ols("rate ~type + rank", data=df)
    data = model.fit()
    print(anova_lm(data))
    pass