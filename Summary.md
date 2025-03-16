# Week 1
## **1. Black’s Model for Futures and Options on Forwards**
### **Main Topics**
- Black-Scholes vs. Black’s Model
- Pricing options on **forwards and futures**
- Risk-neutral measure vs. **forward measure**
- Contango and backwardation

### **Key Concepts**
- **Black’s model** is used when the underlying asset is a **forward contract** rather than a spot asset.
- In the risk-neutral world, the discount factor is \( e^{-r(T-t)} \), but in the **forward measure**, we use **zero-coupon bond prices** \( Z(t,T) \).

### **Important Formulas**
- **Call option price under Black’s model:**
  \[
  c_t = e^{-r(T-t)} [F_t N(d_1) - K N(d_2)]
  \]
- **Put option price under Black’s model:**
  \[
  p_t = e^{-r(T-t)} [K N(-d_2) - F_t N(-d_1)]
  \]
- **Change of measure (using zero-coupon bond as numeraire):**
  \[
  c_t = Z(t,T) [F_t N(d_1) - K N(d_2)]
  \]

- **Forward price under stochastic interest rates:**
  \[
  F_t = S_t e^{(r+u-y)(T-t)}
  \]
  where:
  - \( u \) = storage costs
  - \( y \) = convenience yield

---

## **2. Caps, Floors, and Forward Volatility**
### **Main Topics**
- Caps and floors as portfolios of caplets and floorlets
- Black’s formula for pricing interest rate options
- **Flat volatility vs. Forward volatility**
- Bootstrapping forward volatility

### **Key Concepts**
- **Caplet** = Call option on an interest rate  
- **Floorlet** = Put option on an interest rate  
- **Cap** = Portfolio of caplets  
- **Floor** = Portfolio of floorlets  
- The **swap rate** is used as the ATM strike for caps.
- **Flat volatility** is the implied volatility used for the entire cap (single value).
- **Forward volatility** is extracted to correctly price each caplet.

### **Important Formulas**
- **Caplet price using Black’s formula:**
  \[
  B_{\text{caplet}} = Z(T) [F_T N(d_1) - K N(d_2)]
  \]
- **Cap price as sum of caplet prices:**
  \[
  P_{\text{cap}} = \sum_{\tau} B_{\text{caplet}}(T_\tau, K, F_\tau, Z_\tau)
  \]
- **Bootstrapping forward volatilities from caps:**
  \[
  P_{\text{cap}}(T) = \sum_{i=1}^{n} P_{\text{caplet}}(T_i, \sigma_{\text{flat}})
  \]
  - Solve iteratively for **forward volatilities** from market cap prices.

- **Forward measure approach:**
  \[
  f(F, t) = Z(t,T) \mathbb{E}^{\tilde{Q}} [f(F,T)]
  \]
  - This ensures proper pricing under stochastic discount factors.

---

## **3. Callable Bonds and Embedded Options**
### **Main Topics**
- Callable bonds and their embedded call options
- Pricing callable bonds using Black’s model
- **Option-Adjusted Spread (OAS)**
- **Negative convexity** of callable bonds

### **Key Concepts**
- A **callable bond** can be called (redeemed early) by the issuer.
- The **issuer is short the call option**.
- Callable bonds **exhibit negative convexity**.
- The callable bond price is **lower than the vanilla bond** due to the embedded call.
- The **OAS** adjusts spot rates to match market prices.

### **Important Formulas**
- **Forward bond price:**
  \[
  P_{\text{forward}}(T_{\text{option}} \to T) = \frac{P(T) - \sum_{i=1}^{n} Z(T_i) C_i}{100 Z(T_{\text{option}})}
  \]
- **Callable bond price:**
  \[
  P_{\text{callable}} = P_{\text{vanilla}} - P_{\text{call option}}
  \]
- **Call option value using Black’s formula:**
  \[
  B_{\text{call}}(t) = Z(T) [F_T N(d_1) - K N(d_2)]
  \]
- **Implied bond price volatility:**
  \[
  \sigma_{\text{bond}} \approx D \times \sigma_{\text{rate}} \times r
  \]
- **Option-Adjusted Spread (OAS):**
  \[
  \text{OAS} = \text{Spread needed to match market price}
  \]

---

### **Final Takeaways**
1. **Black’s model extends Black-Scholes to interest rate derivatives**:
   - Uses **forwards instead of spot prices**.
   - Uses **zero-coupon bond discounting** in stochastic interest rate environments.

2. **Caps and Floors price volatility across different rate maturities**:
   - **Flat volatility** is a simplification for quoting.
   - **Forward volatility** provides accurate pricing via bootstrapping.

3. **Callable bonds involve embedded call options**:
   - They **exhibit negative convexity**.
   - Pricing requires separating the **vanilla bond and the embedded option**.
   - The **OAS measures mispricing or model adjustments**.

---

# Week 2

---

## **1. Swaps and Swaptions**
A **swap** is a simple derivative where fixed and floating cash flows are exchanged. A standard pricing approach is to replicate a swap as:
- **Receiving fixed**: Long a fixed-rate bond, short a floating-rate bond.

### **Swaptions (Swap Options)**
A **swaption** is an option on an interest rate swap:
- **Receiver Swaption**: Right (but not obligation) to enter a swap where the holder receives the fixed rate.
  - Analogous to a **put** on a swap.
- **Payer Swaption**: Right to enter a swap where the holder pays the fixed rate.
  - Analogous to a **call** on a swap.

Swaptions are **not the same** as being short the opposite swaption.

---

## **2. Timing Considerations**
Three key dates:
1. **Option Expiration** – when the swaption can be exercised.
2. **Swap Start Date** – when the underlying swap begins.
3. **Swap End Date** – when the underlying swap matures.

A **plain swaption** begins its swap immediately upon exercise.

Example:  
A **2% 1Y 10Y** swaption:
- Strike rate: **2%**
- Expires in **1 year**.
- Starts a **10-year** swap at that time.
- The total duration (from today) is **11 years**.

### **Midcurve Swaptions**
A midcurve swaption has an **underlying swap start date later than the swaption expiration**.  
Example: **6m 1Y 5Y Midcurve Swaption**
- Expires in **6 months**.
- Underlying swap starts **1 year after expiration** (1.5 years from today).
- Swap lasts **5 years**.

---

## **3. Pricing with Black’s Formula**
Swaptions are priced using **Black’s formula**, similar to **caps and caplets**, but with key differences:
- **Payer Swaption** (option to pay fixed) → **Call Option**  
- **Receiver Swaption** (option to receive fixed) → **Put Option**  

### **Timing**
- The swaption expiration date \( T_o \) is plugged into Black’s formula.
- Unlike caps, where each caplet is priced separately, a swaption is a **single option covering multiple payments**.

### **Discount Factor Adjustments**
- Unlike caps, where each caplet has a different forward vol, a swaption involves multiple payments from the same option.
- Instead of pricing each payment separately, use **one Black's formula evaluation** and scale by the sum of the discount factors.

#### **Discount Factor Formula**
\[
Z_{\text{swap}}(0, T_o, T) = \sum_{i=1}^{m} Z(0, T_i)
\]
where:
- \( Z(0, T_i) \) is the discount factor for payment time \( T_i \).
- \( m \) is the number of payments.

Example: **1Y 2Y Swaption on an annually paying swap**
\[
Z_{\text{swap}}(0, 1, 2) = Z(0,2) + Z(0,3)
\]

---

## **4. Forward Swap Rate**
Since swaptions depend on expected swap rates at expiration, we use the **forward swap rate**, not the spot swap rate.

\[
F(t, T_{\text{fwd}}, T) = \frac{Z(t, T_{\text{fwd}}) - Z(t, T)}{\sum_{i=1}^{m} Z(t, T_i)}
\]

### **Forward Factor Formula**
\[
f_n(t, T_{\text{fwd}}, T) = n \left( \frac{Z(t, T_{\text{fwd}})}{Z(t, T)} - 1 \right)
\]

where:
- \( Z(t, T) \) is the discount factor.
- \( n \) is the payment frequency (e.g., **2 for semiannual swaps**).
- \( T_{\text{fwd}} \) is the forward date.

---

## **5. Put-Call Parity Relationships**
Several arbitrage relationships exist among swaptions, caps, floors, and FRAs:

1. **Caplet-Floorlet-FRA Parity**
   \[
   p_{\text{caplet}} - p_{\text{floorlet}} = p_{\text{FRA}}
   \]

2. **Cap-Floor-Swap Parity**
   \[
   p_{\text{cap}} - p_{\text{floor}} = p_{\text{paying-fixed swap}}
   \]

3. **Swaption Put-Call Parity**
   \[
   p_{\text{payer}} - p_{\text{receiver}} = p_{\text{forward swap}}
   \]
   (Both swaptions must be European-style and struck at the forward swap rate.)

---

## **6. Forward Volatility and Implied Volatility**
- Swaptions differ from caps/floors in that they are **single options on a stream of payments**.
- Caps/floors are **streams of options on single payments**.
- **Forward Volatility Agreements (FVAs)** allow traders to speculate on forward volatility of interest rate products.

### **No-Arbitrage Links Between Forward Vols**
Since both swaptions and caps/floors depend on forward rates, their implied volatilities are related through no-arbitrage conditions.

---

## **Conclusion**
This lecture focused on **swaptions as options on swaps**, their pricing via **Black’s formula**, their relationships to **caps, floors, and FRAs**, and the **importance of forward swap rates**. The pricing adjustments for multiple payments and discounting were emphasized, as well as the put-call parity conditions among different interest rate derivatives.


----

### **Summary of "Volatility Modeling with SABR" Lecture**

#### **1. Motivation for Volatility Modeling**
- Implied volatility is not constant; it varies across:
  - **Moneyness** (strike price vs. underlying)
  - **Time-to-expiration**
  - **Time** itself
- This affects:
  - **Hedging**: How do we determine the right hedge ratio when volatility is inconsistent?
  - **Pricing**: Ensuring a consistent model for valuation.

#### **2. Volatility Surface & Skew**
- A key focus is on **volatility curves**, **smiles**, and **skews** (variation across strikes).
- Model inconsistency in implied volatility leads to inconsistency in:
  - **Delta**
  - **Gamma**
- Even if implied volatility were constant, its changes over time still matter due to **vega**.

#### **3. Types of Volatility Models**
- **Parametric Models**: Impose structure for statistical power and protection against overfitting (e.g., polynomials).
- **Non-Parametric / Semi-Parametric Models**: More flexible, allowing data-driven estimation (e.g., splines, machine learning).
- **Stochastic Volatility Models**: Define a stochastic process for volatility to ensure:
  - No-arbitrage conditions
  - Insights beyond observed data
  - Examples: **Local Volatility, SABR, ZABR**

---

### **4. SABR Model (Stochastic Alpha Beta Rho)**
- Used in conjunction with **Black’s Model**.
- SABR does not price directly but provides implied volatility input for pricing models.

#### **SABR Stochastic Differential Equations**
1. **Forward Price Process**:
   \[
   dF = \sigma F^\beta dW^{(1)}
   \]
   - \( \beta \) determines the nature of the forward price process:
     - **Lognormal (β = 1)**
     - **Normal (β = 0)**
     - **CEV (0 < β < 1)**
   - Typically set rather than estimated.

2. **Volatility Process**:
   \[
   d\sigma = \nu \sigma dW^{(2)}
   \]
   - \( \sigma \) follows a **geometric Brownian motion** (lognormal process).
   - **\( \nu \)**: Volatility of volatility parameter.

3. **Correlation Between Processes**:
   \[
   dW^{(1)} dW^{(2)} = \rho dt
   \]
   - \( \rho \) represents the correlation between price and volatility processes.
   - Question: Is \( \rho \) typically **positive or negative**? -> Typically is a negative relation, decreasing rate generate a higher implied vol 

---

### **5. Key Parameters in SABR**
- **\( \alpha \) (Initial Volatility Level):** 
  - Sometimes written as \( \sigma_0 \), controlling the base volatility level.
- **\( \nu \) (Volatility of Volatility):**
  - Governs how much volatility itself fluctuates.
- **\( \rho \) (Correlation between price and volatility shocks):**
  - Typically **negative** in equity markets.
  - Can vary across different asset classes.

---

### **6. Implied Volatility Formula in SABR**
The SABR model leads to the implied volatility approximation:

\[
\sigma_{\text{imp}}(F_0, K) = AB \cdot \frac{\phi}{\chi} \ln(F_0/K)
\]

For **At-The-Money (ATM)** options (\( K = F_0 \)), the formula simplifies:

\[
\sigma_{\text{imp}}^* = \frac{\sigma_0 B}{F_0^{1-\beta}}
\]

This allows traders to express **\( \alpha \) (or \( \sigma_0 \)) as a function of market-implied volatility**, reducing the number of estimated parameters.

---

### **7. Fitting the SABR Model**
1. Use **market-observed implied volatilities**.
2. Numerically optimize parameters (\( \alpha, \nu, \rho \)) by minimizing:
   \[
   \sum_i (\sigma_{\text{imp}}^{\text{SABR}}(i) - \sigma_{\text{imp}}^{\text{market}}(i))^2
   \]
3. Use fitted parameters to generate a **volatility curve** for:
   - Pricing other options
   - More accurate **Greek calculations**

---

### **8. Delta Hedging with SABR**
- **Delta changes when implied volatility changes** (known as **vanna**).
- A more accurate delta includes **volatility sensitivity**:

  \[
  \Delta = \frac{\partial C}{\partial F} + \frac{\partial C}{\partial \sigma_{\text{imp}}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial F}
  \]

---

### **9. Comparison with Other Models**
- **Black-Scholes Model**: Assumes constant volatility → Does **not** account for skew.
- **Local Volatility Model**:
  - Fits market-implied volatilities **exactly**.
  - However, **fails in time dynamics**, leading to worse hedging performance.
- **SABR Model**: Balances flexibility and tractability, making it more useful for practical trading.

---

### **Conclusion**
- The **SABR model** is a widely used **stochastic volatility model** for derivatives pricing.
- It extends Black’s model by introducing **stochastic volatility and skew**.
- By calibrating to market-implied volatilities, it provides a **realistic volatility surface**.
- **Delta hedging and risk management** are improved by incorporating volatility dynamics.


-----

# Week 3


### **Summary of "STIR Futures" Lecture (Short-Term Interest Rate Futures)**

#### **1. Introduction to STIR Futures**
- **STIR Futures** are contracts written directly on an **interest rate**, not a bond.
- They share key similarities with bond futures:
  - **Trade on an exchange**
  - **Daily settlement**
- Key differences:
  - **Cash-settled**, meaning there is no physical delivery—only a cash payment.
  - **No embedded options** (unlike bond futures).
- **Payoff Structure**:
  - Futures price moves **inversely** to the reference interest rate:
    \[
    P_t = 100 (1 - r^{\text{ref}}_t)
    \]
  - When rates **increase**, the futures price **decreases**.

---

### **2. Fed Funds Futures**
- Reference rate: **Simple average** of the **Fed Funds Effective Rate** over the month.
  - **Non-trading days** use the most recent traded day’s rate.
- **Contract Specifications**:
  - Notional: \( N = 5,000,000 \)
  - Settlement: 1-month horizon (30/360 convention)
- **Contract Pricing & Settlement**:
  - Settlement price:
    \[
    P_T = 100 (1 - r^{\text{ref}}_T)
    \]
  - **Daily Settlement**:
    \[
    PnL = 5,000,000 \times \frac{(P_{t+1} - P_t)}{100} \times \frac{30}{360}
    \]
  - **Impact of 1 basis point (bp) change**:
    \[
    PnL = -41.67
    \]
- **Market Expectations**:
  - Fed Funds futures prices are used to infer market expectations of **Federal Reserve rate hikes or cuts**.

---

### **3. SOFR Futures**
- **Transition from LIBOR** to **SOFR (Secured Overnight Financing Rate)** as a benchmark.
- Two major types:
  - **1-month SOFR Futures**: Similar to Fed Funds Futures.
  - **3-month SOFR Futures**: Has key differences.

#### **1-Month SOFR Futures**
- Nearly identical to **Fed Funds Futures**.

#### **3-Month SOFR Futures**
- **Reference rate**: Compounded SOFR over the 3-month period (not a simple average).
- **Contract Specs**:
  - Notional: \( N = 1,000,000 \)
  - **Quarterly expirations** (March, June, September, December).
  - Settlement price:
    \[
    P_T = 100 (1 - r^{\text{ref}}_T)
    \]
- **Daily Settlement**:
  \[
  PnL = 1,000,000 \times \frac{(P_{t+1} - P_t)}{100} \times \frac{90}{360}
  \]
  - **Impact of 1bp change**:
    \[
    PnL = -25.00
    \]

---

### **4. STIR Futures in Discount Curve Estimation**
- **STIR Futures are used to estimate short-term interest rates.**
- They provide **spot (discount) rates** or **forward rates** for short maturities.
- More liquid than swaps for maturities **up to 3 years**.

---

### **5. Convexity Adjustment in STIR Futures**
- Futures rates tend to be **higher than forward rates** due to daily settlement.
- **Convexity Adjustment Formula**:
  \[
  r_{\text{fut}} = r_{\text{fwd}} + \frac{\tau^2 \sigma^2}{2}
  \]
  - \( \tau = T - t \) (time horizon)
  - \( r_{\text{fwd}}(t, T) \) is the continuously compounded forward rate.
  - \( r_{\text{fut}}(t, T) \) is the continuously compounded futures rate.

**Why does this adjustment exist?**
- Daily settlement creates a disadvantage for long positions.
- The adjustment **corrects** this difference based on an interest rate model.

---

### **6. Basis Risk in Futures Hedging**
- **Forward contracts (OTC) vs. Futures (exchange-traded)**:
  - **Forwards** are customizable and match the exact interest rate risk.
  - **Futures** require using the closest available contract.
- **Sources of Basis Risk**:
  - **Mismatch in underlying rate** (e.g., different benchmark rate).
  - **Mismatch in timing** (e.g., futures contract expiration differs from risk horizon).

---

### **Conclusion**
- **STIR Futures** (Fed Funds, SOFR) are key instruments in interest rate markets.
- Used for **hedging, speculation, and estimating discount curves**.
- The **convexity adjustment** accounts for the difference between futures and forward rates.
- **Basis risk** is a challenge in futures hedging, requiring careful contract selection.

----

### **Summary of "W.3. Treasury Futures" Lecture (FINM 37500: Fixed Income Derivatives)**  


## **1. Introduction to Treasury Futures**  
- **Forward agreements** commit to purchasing an asset at a future date \( T \) for a price \( F_t \).  
- The forward price is set such that the value of the contract is **zero** at initiation.  
- Unlike options, net value at expiration can be **positive or negative** for either party.  
- **Futures contracts** function similarly but differ in trading structure and settlement processes.

## **2. Forward Pricing & Synthetic Forwards**
- Forward price equation:

  \[
  F_{t \to T} = P_t(1 + r_{\text{repo}} \cdot \tau_{\text{act/360}})
  \]

  where:  
  - \( P_t \) is the spot price.  
  - \( r_{\text{repo}} \) is the simply compounded repo rate.  
  - \( \tau_{\text{act/360}} \) is the time fraction measured in **ACT/360** convention.  

- **Forward price behavior**:  
  - If **coupon rate > repo rate**, spot price is **more attractive**, leading to **lower forward price**.  
  - If **coupon rate < repo rate**, forward price is **higher than spot price**.

- **Carry and Forward Drop:**  
  - Carry is defined as:

    \[
    \tilde{c}_i = c_i - r_{\text{repo}}
    \]

  - Forward drop (or rise) is analogous to **Covered Interest Parity** in FX markets.

## **3. Futures vs. Forwards**
- **Similarities:**
  - Both involve forward pricing, hedging, and risk management.  

- **Differences:**
  - **Futures trade on exchanges** (not OTC).  
  - **Standardized contracts** vs. customizable forwards.  
  - **Daily settlement** of P&L in futures.  
  - **Margin requirements** for futures.

- **Effect of Daily Settlement:**  
  - Futures prices tend to be **lower** than forward prices due to unfavorable cashflow timing.  
  - **Mathematically:**  
    \[
    N_{\text{fut}} = Z(t,T) N_{\text{fwd}}
    \]
    where \( Z(t,T) \) is the present value discount factor.

## **4. Treasury Bond Futures (TY)**
- **10-Year U.S. Treasury Note Futures** (CME & CBOT).  
- **Delivery Optionality:**  
  - Any Treasury note with maturity **between 6.5 to 10 years** is eligible for delivery.  
  - Prevents market manipulation ("squeezes").  

- **Conversion Factor Calculation:**  
  \[
  \psi_i = \sum_{j=1}^{2T_i} \frac{c_i/2}{(1+0.06/2)^j} + \frac{1}{(1+0.06/2)^{2T_i}}
  \]
  where:  
  - \( c_i \) is the bond's coupon rate.  
  - \( T_i \) is time to maturity.  
  - Uses a **6% flat yield curve** assumption.

## **5. Cheapest to Deliver (CTD) Bond**
- At expiration:

  \[
  P_{\text{ctd},T} = \psi_{\text{ctd}} F_{T \to T}
  \]

  where \( P_{\text{ctd},T} \) is the price of the CTD bond.  
- **Delivery cost for bond \( i \):**  

  \[
  \text{Delivery Cost}_T = P_i + \xi_i - (\psi_i F_{T \to T} + \xi_i) = P_i - \psi_i F_{T \to T}
  \]

- The **bond with the lowest delivery cost** is the **CTD bond**.

## **6. Embedded Optionality in Treasury Futures**
- **Quality Option:** Seller selects the CTD bond.  
- **Timing Option:** Seller can deliver any day in the delivery month.  
- **End-of-Month Option:** Seller has additional days to choose a delivery bond.  
- **Wildcard Option:** Shorts can decide **post-settlement** whether to deliver.

## **7. Basis Trade and Net Basis**
- **Gross Basis:**  
  \[
  \Gamma_i = P_i - \psi_i F_{T \to T}
  \]
- **Net Basis:**  
  \[
  \tilde{\Gamma}_i = \Gamma_i - (c_N - r_{\text{repo}} P_i) \frac{\tau_{\text{act/360}}}{360}
  \]

- **At expiration:**  
  \[
  \Gamma_{\text{ctd},T} = \tilde{\Gamma}_{\text{ctd},T} = 0
  \]

- **Net basis is a key measure of CTD likelihood**.

## **8. Implied Repo Rate**
- The **repo rate that equates spot and futures price**:

  \[
  r_{\text{IR}} = \frac{F_i \psi_i + \xi_T - P_i - \xi_i}{(P_i + \xi_i) \cdot \tau_{\text{act/360}}}
  \]

- If **implied repo > actual repo**, futures may be **overpriced**.

---

### **Conclusion**
- **Treasury futures play a vital role** in managing interest rate risk and market liquidity.  
- **CTD selection, carry, and embedded options** influence futures pricing and strategy.  
- **Understanding basis trades and implied repo** is critical for arbitrage strategies.  






