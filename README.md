### Financial_Backtrader
# Backtesting is the hallmark of quantitative trading.
# Backtesting takes historical or synthetic market data and tests the profitability of algorithmic trading strategies.


### Source
# Expanded upon the Medium Article "Medium Backtest-stock-trading-strategies" by Roman Paulucci series
(Medium Article)[https://romanmichaelpaolucci.medium.com]

### Backtrader Process
# I. The Backtesting Engine
# II. Historical and Synthetic Data Management
# III. Backtesting Metrics
# IV. Live Implementation
# V. Pitfalls in Strategy Development


### Scientific Method
# Ask a questions of one or more variables
# For hypothetical questions in the standard form of such a proposition, it is the part that follows "then". In an implication, if P implies Q, then P is called the antecedent and Q is called the consequent
# In prepositional logic we form questions that must be cogent
# "My antecedent is that y happens because of m, x or b..."
# If you think your grass gets wet when it rains then
    # P = It rained last night
    # Q = My grass is wet
    # we can calculate Probability of P given Q
    
# If you think you're home value goes up when you have more square feet of living space
    # P = Appreciated home value
    # Q = Additional square feet of living space
    # we can localize or increase the accuracy of the calculation given geography
    # Y = Mx+b
    # Y = Home value
    # M = Localized coefficent value for each square foot
    $ x = Number of square feet

### Technical Trading Strategy
1. Clean Data
2. Calculate z score or distribution test
3. Calculate Quoted Spread
4. Calculate Order Size
5. Calculate Transactional Cost
6. Calculate Profit Potential
   1. is Z <= Lth-value
      1. if no trade = no
         1. add trade interval[ML]
            1. back to position 1
      2. if yes trade = yes
         1. is profit delta > zero
            1. if yes go to step seven
         2. add trade interval[ML]
   2. is Z > Uth
      1. if no trade = no
         1. add trade interval[ML]
            1. back to position 1
      2. if yes trade = yes
         1. is profit delta > zero
            1. if yes go to step seven
         2. add trade interval[ML]
7. Place Buy-Sell Order
8. Check MRS, MRE, 30MRE
   1. if no back to position 1
9. Check stop loss 
   1. if no back to position 1
10. Check Max Duration
11. Check Strategy Complete
    1. if no back to step 8

### Chart Reading
# Bull vs Bear
# Buy the "blah"
# Sell the "zorg"

### Installation
# Python3.7


### Uses
# algorithmic finance
# crypto trading


### TODO list
- [] add 'pip install backtrader[plotting]'
- [] added add 'pip install backtrader
- [] ERROR = box/PycharmProjects/Financial_Backtrader/backtesting_b.py", line 3, in <module>
    from models.isolation_model import IsolationModel
ModuleNotFoundError: No module named 'models'
- [] most likely an ommited custom function = msg OP and wait for response
- [] git PR to author for next steps.