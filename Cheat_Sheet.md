# **Interest Rate Derivatives & Volatility Modeling Cheat Sheet**

---

## **Week 1: Black’s Model, Caps/Floors & Callable Bonds**

### **Black’s Model for Futures/Forwards Options**
- **Purpose:** Price options when the underlying is a forward/futures contract (uses forward prices & zero‑coupon bonds).
- **Key Distinction:**  
  - **Risk-neutral measure:** Discount factor \(e^{-r(T-t)}\)  
  - **Forward measure:** Use zero‑coupon bond \(Z(t,T)\)

- **Call Option Price:**  
  \[
  c_t = e^{-r(T-t)} [F_t N(d_1) - K N(d_2)]
  \]
- **Put Option Price:**  
  \[
  p_t = e^{-r(T-t)} [K N(-d_2) - F_t N(-d_1)]
  \]
- **Change of Measure:**  
  \[
  c_t = Z(t,T) [F_t N(d_1) - K N(d_2)]
  \]
- **Forward Price under Stochastic Rates:**  
  \[
  F_t = S_t e^{(r+u-y)(T-t)}
  \]
  - \(u\) = storage cost, \(y\) = convenience yield

---

### **Caps, Floors, & Forward Volatility**
- **Components:**
  - **Caplet:** Call option on an interest rate  
  - **Floorlet:** Put option on an interest rate  
  - **Cap/Floor:** Portfolios of caplets/floorlets

- **Caplet Pricing (Black’s Formula):**  
  \[
  B_{\text{caplet}} = Z(T) [F_T N(d_1) - K N(d_2)]
  \]
- **Cap Price:**  
  \[
  P_{\text{cap}} = \sum_{\tau} B_{\text{caplet}}(T_\tau, K, F_\tau, Z_\tau)
  \]
- **Volatility Notions:**
  - **Flat Volatility:** Single implied vol for the entire cap  
  - **Forward Volatility:** Bootstrapped for each caplet for accuracy

- **Forward Measure Approach:**  
  \[
  f(F, t) = Z(t,T) \mathbb{E}^{\tilde{Q}} [f(F,T)]
  \]

---

### **Callable Bonds & Embedded Options**
- **Concepts:**
  - **Callable Bond:** Issuer can redeem early (embedded call option)
  - **Negative Convexity:** Price declines faster when rates drop due to call risk
  - **OAS (Option-Adjusted Spread):** Adjusts yield to match market price

- **Formulas:**
  - **Forward Bond Price:**  
    \[
    P_{\text{forward}}(T_{\text{option}} \to T) = \frac{P(T) - \sum_{i=1}^{n} Z(T_i) C_i}{100 \, Z(T_{\text{option}})}
    \]
  - **Callable Bond Price:**  
    \[
    P_{\text{callable}} = P_{\text{vanilla}} - P_{\text{call option}}
    \]
  - **Call Option (Black’s):**  
    \[
    B_{\text{call}}(t) = Z(T) [F_T N(d_1) - K N(d_2)]
    \]
  - **Implied Bond Volatility:**  
    \[
    \sigma_{\text{bond}} \approx D \times \sigma_{\text{rate}} \times r
    \]

---

## **Week 2: Swaps, Swaptions & Timing**

### **Swaps & Swaptions**
- **Swap:** Exchange of fixed and floating cash flows  
  - **Replication:** Long fixed bond and short floating bond
- **Swaption:** Option on a swap
  - **Receiver Swaption:** Right to receive fixed (like a put)
  - **Payer Swaption:** Right to pay fixed (like a call)

### **Timing Considerations**
- **Key Dates:**  
  1. **Expiration** – when the option can be exercised  
  2. **Swap Start Date** – when cash flows begin  
  3. **Swap End Date** – maturity of the swap
- **Midcurve Swaption:** Expiration occurs before the swap start date

---

### **Pricing with Black’s Formula**
- **Swaptions:** Use Black’s formula (similar to caplets) but scale by the sum of discount factors:
  \[
  Z_{\text{swap}}(0, T_o, T) = \sum_{i=1}^{m} Z(0, T_i)
  \]
- **Forward Swap Rate:**  
  \[
  F(t, T_{\text{fwd}}, T) = \frac{Z(t, T_{\text{fwd}}) - Z(t, T)}{\sum_{i=1}^{m} Z(t, T_i)}
  \]
- **Put-Call Parity for Swaptions:**  
  \[
  p_{\text{payer}} - p_{\text{receiver}} = p_{\text{forward swap}}
  \]

---

### **Forward & Implied Volatility**
- **Differences:**  
  - Swaptions are a single option on a stream of payments  
  - Caps/Floors are a series of options on individual payments
- **Forward Volatility Agreements (FVAs):** Allow speculation on forward vol levels
- **No-Arbitrage:** Links forward vols between swaptions and caps/floors

---

## **Volatility Modeling with SABR**

### **Motivation & Volatility Surface**
- **Implied Volatility:** Varies with strike (skew/smile) and time
- **Hedging Impact:** Affects delta, gamma, and vega sensitivities

### **SABR Model Essentials**
- **Stochastic Processes:**
  - **Forward Price:**  
    \[
    dF = \sigma F^\beta dW^{(1)}
    \]
    - \( \beta \): Determines process type (Lognormal for \(\beta=1\), Normal for \(\beta=0\), etc.)
  - **Volatility Process:**  
    \[
    d\sigma = \nu \sigma dW^{(2)}
    \]
    - \( \nu \): Volatility of volatility
  - **Correlation:**  
    \[
    dW^{(1)} dW^{(2)} = \rho dt
    \]
    - Typically \(\rho\) is negative (especially in equities)

- **Implied Volatility Approximation:**  
  \[
  \sigma_{\text{imp}}(F_0, K) \approx \text{(complex function involving } \alpha,\beta,\nu,\rho \text{)}
  \]
  - For ATM:  
    \[
    \sigma_{\text{imp}}^* = \frac{\sigma_0 B}{F_0^{1-\beta}}
    \]

- **Calibration:** Fit parameters \((\alpha,\nu,\rho)\) by minimizing squared errors between model and market implied vols.

- **Delta Hedging:**  
  \[
  \Delta = \frac{\partial C}{\partial F} + \frac{\partial C}{\partial \sigma_{\text{imp}}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial F}
  \]

---

## **Week 3: STIR Futures & Treasury Futures**

### **STIR Futures (Short-Term Interest Rate Futures)**
- **Overview:**  
  - **Contracts:** Written on an interest rate (e.g., Fed Funds, SOFR)  
  - **Features:** Cash-settled, daily settlement, no embedded options  
- **Price Relation:**  
  \[
  P_t = 100 (1 - r^{\text{ref}}_t)
  \]
- **Fed Funds Futures:**
  - **Notional:** \(5,000,000\)
  - **Settlement:** 1-month (30/360 convention)
  - **1bp Change Impact:** PnL \(\approx -41.67\)
- **SOFR Futures:**
  - **1-Month:** Similar to Fed Funds  
  - **3-Month:** Based on compounded SOFR; 1bp Impact \(\approx -25.00\)

- **Convexity Adjustment:**  
  \[
  r_{\text{fut}} = r_{\text{fwd}} + \frac{\tau^2 \sigma^2}{2}
  \]
  - Adjusts for daily settlement effects

- **Basis Risk:**  
  - Differences in underlying rate or timing between futures and corresponding forwards

---

### **Treasury Futures**
- **Basics:**  
  - **Forward Agreement:** Buy/sell a bond at future date at price set today  
  - **Futures:** Standardized, exchange-traded with daily margining
- **Forward Price Equation:**  
  \[
  F_{t \to T} = P_t(1 + r_{\text{repo}} \cdot \tau_{\text{act/360}})
  \]
- **Carry/Forward Drop:**  
  \[
  \tilde{c}_i = c_i - r_{\text{repo}}
  \]
- **CTD (Cheapest to Deliver):**
  - **Conversion Factor:**  
    \[
    \psi_i = \sum_{j=1}^{2T_i} \frac{c_i/2}{(1+0.06/2)^j} + \frac{1}{(1+0.06/2)^{2T_i}}
    \]
  - **CTD Price at Delivery:**  
    \[
    P_{\text{ctd},T} = \psi_{\text{ctd}} F_{T \to T}
    \]
- **Embedded Options:**  
  - **Quality, Timing, End-of-Month, Wildcard** options benefit the short position
- **Implied Repo Rate:**  
  \[
  r_{\text{IR}} = \frac{F_i \psi_i + \xi_T - P_i - \xi_i}{(P_i + \xi_i) \cdot \tau_{\text{act/360}}}
  \]

---

## **Final Takeaways**
- **Black’s & SABR Models:** Extend option pricing into forward and stochastic volatility realms.
- **Interest Rate Derivatives:** Include a range of instruments (caps/floors, swaptions, futures) each with unique pricing adjustments.
- **Risk & Hedging:** Understanding timing, discounting, and volatility dynamics is key to accurate pricing and risk management.
- **Practical Adjustments:** Convexity adjustments, CTD selection, and OAS are vital in managing real-world trading strategies.
