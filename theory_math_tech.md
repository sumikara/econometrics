## PYTHON
# statistics/analysis/visualizations libraries and packages
- numpy:Numerical Python. for numerical computing.array objects as one of the standard interface for data exchange. arithmetic operations. subsidiary of for loop. faster and easier (range function). it is transferable to pandas.
for EDA: sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod functions
for DQ: sort, unique, in1d, intersect1d, union1d, setdiff1d, setxor1d
for array saving: save, load
important: random walks (random module with plotting generally),  
- pandas: numpy's brother(complementary). data structures, data manipulation tools included. work for data cleaning and analysis fast and convenient. pandas is designed for working with tabular or heterogeneous data. NA, nulls, Nan
some complementaries: SciPy, statsmodels, scikit-learn, matplotlib
for EDA: Data cleanıng purpose
stars in Pandas: Series, Data Frame(A DataFrame represents a rectangular table of data and contains an ordered, named collection of columns, each of which can be a different value type (numeric, string, Boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dictionary of Series all sharing the same index).
With DataFrame(data), .head(), .tail(), index, columns, sum(), skip na, level, idxmin, idxmax, 
important functions/methods: to_dict, keys, sdata, isna, notna, append(), difference, intersection, union, isin, delete, drop, insert, is_monotonic, is unique, unique, reindex, loc, iloc, sort_values, rank, dense(tie breaking)), std, mean, median, mad, prod, var, skew, diff, pct_change, value_counts, 
- reading the data from local (read_csv/*)--> message, header:None, index_col, sep/delimiter, skiprows, na_values, sentinels keep_default_na, nrows, chunksize, TextFileReader,  
- to_csv, sys.stdout, reader(), csv.Dialect, escapechar, 
JSON: read_json/ to_json/ from out into Python: json.load / from Python to out as JSON: json.dumps
XML&HTML:Web Scraping --> read_html, pip install lxml
Parquet(binary data format): pyarrow, conda install pyarrow, .read_parquet   
Web API: requests, get(), raise_for_status 
databases: sqlite3, connect(), .execute(query), .commit, fetchall, .description, sqlalchemy  SQLAlchemyProject for Python-SQL toolkit.
Data Cleaning and Preparation
Handling Missing Data: descriptive statistics on pandas objects exclude missing data by default.
(NAN, None)isna, fillna (or dropna),
Data Transformation: 1-removing duplicates: duplicated(), drop_duplicates(), 
map yeni bir kolon dict oluşturursan append edersin. 
replace, reshape, upper, lower
get_dummies & cut together (star is the dummy variable in pandas)
string manipulation: .split, .strip, .r/lstrip, .join, endswith, startswith, index, find, rfind, casefold, regex  
Merging Data se**t: pandas.merge, .concat, combine_first, concatenate, 
**Visualization:** matplotlib, seaborn, figure(), add_subplot, plot(), density, bins, 
Data Aggregation (sum, count, mean,min) and Grouping Ops: groupby pands.
Time Series As Structured Data: timeststamp, datetime, timedelta, %Y,%...
Categorical Data: 
## Patsy Lib:  for describing statistical models (especially linear models) with a string-based "formula syntax," which is inspired by (but not exactly the same as) the formula syntax used by the R and S statistical programming languages. It is installed automatically when you install statsmodels:
conda install statsmodels, DesignMatrix , 
Data Transformations in Patsy Formulas
You can mix Python code into your Patsy formulas; when evaluating the
## statsmodels Lib:for fitting many kinds of statistical models, performing statistical tests, and data exploration and visualization.
Linear models, generalized linear models, and robust linear models (OLS) Linear mixed effects models, Analysis of variance (ANOVA) methods, Time series processes and state space models, Generalized method of moments
scikit-learn (dependent, independet variable OLS modeling in Python wiht scikit-lear)
scikit-learn is one of the most widely used and trusted general-purpose Python machine learning toolkits.


## R
# statistics/analysis libraries and packages
-  
