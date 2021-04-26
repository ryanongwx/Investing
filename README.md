# Investing

This repository is for the programs that I have written which are related to investing and stocks. As investing is one field that I am interested
in, I will attempt to write programs from time to time that may help me in the process of investing. The possible areas that these programs can
enable to be more efficient are areas such as calculation and information retrieving from the web. Through the application of the investing
principles that I have picked up when reading books, I will apply them and make us of code to make calculations easier. This will definitely aid
me in finding the 'right' stocks to invest in.


Pricetarget.py makes use of the Wall Street P/E Model (P/E Relative Valuation Model) to calculate a price target at which to buy the stocks.
The price target is obtained via the multiplication of a company's one-year-ahead earnings estimate and the long-run P/E ratio estimate. In
this case the one-year-ahead earnings estimate is obtained from Yahoo Finance and the long-run P/E ratio (5 year P/E ratio average) is obtained
from Ycharts. Finally, the pricce target and the current price of the stock is compared and the potential gain from inveesting in the stock
is calculated as a perccentage gain.  Output of the pricetarget.py file is pricetarget.csv. This may further be developed into an output to google
sheets and prompt and email to be sent when the potential gain hits a certain percentage. This can act as a live stock tracker and can acccurately
inform us when a certain potential projected gain is reached and perhaps may be the 'right' time to invest in the stock. I am currently further 
exploring this.
