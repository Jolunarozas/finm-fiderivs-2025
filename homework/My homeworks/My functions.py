import numpy as np
import pandas as pd


def price_bond(discounts: pd.DataFrame, cpnrate: float, ttm: float, cpnfreq: int = 2, face: float = 100) -> float:
    """
    Prices a typical coupon bond using discount factors.
    
    Parameters:
        discounts (pd.DataFrame): A dataframe with an index representing time-to-maturity (in years)
                                  at intervals (e.g., 0.5, 1.0, ..., 30), and with columns 'spot rate' and 'discount'.
        cpnrate (float): Annual coupon rate. If the value is greater than 1, it is assumed to be a percentage
                         and will be divided by 100.
        ttm (float): Time-to-maturity (in years) of the bond.
        cpnfreq (int, optional): Number of coupon payments per year (default=2 for semiannual coupons).
        face (float, optional): Face (par) value of the bond (default=100).
    
    Returns:
        float: The calculated bond price.
    """
    
    # Adjust coupon rate if provided as a percentage
    if cpnrate > 1:
        cpnrate = cpnrate / 100.0

    coupon_payment = face * cpnrate / cpnfreq

    # If time-to-maturity is less than one coupon period, set payment_dates to just [ttm]
    if ttm < 1/cpnfreq:
        payment_dates = np.array([ttm])
    else:
        # Generate regular coupon payment dates
        payment_dates = np.arange(1/cpnfreq, ttm + 1e-8, 1/cpnfreq)
        # If the last payment date is not exactly ttm, add the maturity as an irregular final period.
        if not np.isclose(payment_dates[-1], ttm):
            payment_dates = np.append(payment_dates, ttm)
    
    price = 0.0
    for t in payment_dates:
        # Determine cash flow:
        # For the final payment at maturity, add the face value.
        # Note: Depending on the bond's terms, you might want to prorate the coupon for an irregular period.
        if np.isclose(t, ttm):
            cash_flow = coupon_payment + face
        else:
            cash_flow = coupon_payment
        
        # Retrieve the discount factor: if an exact match is not found, interpolate.
        if t in discounts.index:
            discount_factor = discounts.loc[t, 'discount']
        else:
            discount_factor = np.interp(t, discounts.index.values, discounts['discount'].values)
        
        price += cash_flow * discount_factor
    
    return price

def get_approximate_discount(T,discs):
    diffs_array = np.abs(discs.index - T)
    imin = diffs_array.argmin()
    idx = discs.index[imin] 
    return idx

def calc_forward_bond_price(spot,Tfwd,discount_curve,cpnrate,face=100,cpnfreq=2):
    
    discount_grid_step = np.diff(discount_curve.index).mean()
    grid_step_cpn = round(1 / (cpnfreq * discount_grid_step))
    Tfwd_rounded = get_approximate_discount(Tfwd,discount_curve)

    Z = discount_curve.loc[Tfwd_rounded,'discount']
    cpn_discs = discount_curve.loc[:Tfwd_rounded:grid_step_cpn,'discount']

    coupon_payment = face * cpnrate / cpnfreq
    pv_coupons = sum(coupon_payment * df for df in cpn_discs)
    fwd_price = (spot - pv_coupons) / Z

    return fwd_price

def duration_closed_formula(tau, ytm, cpnrate=None, freq=2):

    if cpnrate is None:
        cpnrate = ytm
        
    y = ytm/freq
    c = cpnrate/freq
    T = tau * freq
        
    if cpnrate==ytm:
        duration = (1+y)/y  * (1 - 1/(1+y)**T)
        
    else:
        duration = (1+y)/y - (1+y+T*(c-y)) / (c*((1+y)**T-1)+y)

    duration /= freq
    
    return duration

def compound_rate(intrate,compound_input,compound_output):    
    if compound_input is None:
        outrate = compound_output * (np.exp(intrate/compound_output) - 1)
    elif compound_output is None:
        outrate = compound_input * np.log(1 + intrate/compound_input)
    else:
        outrate = ((1 + intrate/compound_input) ** (compound_input/compound_output) - 1) * compound_output

    return outrate

def calc_fwdswaprate(discounts, Tfwd, Tswap, freqswap):
    freqdisc = round(1/discounts.index.to_series().diff().mean())
    step = round(freqdisc / freqswap)
    
    periods_fwd = discounts.index.get_loc(Tfwd)
    periods_swap = discounts.index.get_loc(Tswap)
    periods_fwd += step
    periods_swap += 1
    
    fwdswaprate = freqswap * (discounts.loc[Tfwd] - discounts.loc[Tswap]) / discounts.iloc[periods_fwd:periods_swap:step].sum()
    return fwdswaprate


def blacks_formula(T,vol,strike,fwd,discount=1,isCall=True):
        
    sigT = vol * np.sqrt(T)
    d1 = (1/sigT) * np.log(fwd/strike) + .5*sigT
    d2 = d1-sigT
    
    if isCall:
        val = discount * (fwd * norm.cdf(d1) - strike * norm.cdf(d2))
    else:
        val = discount * (strike * norm.cdf(-d2) - fwd * norm.cdf(-d1))
    return val

def price_bond(ytm, T, cpn, cpnfreq=2, face=100, accr_frac=None):
    ytm_n = ytm/cpnfreq
    cpn_n = cpn/cpnfreq
    
    if accr_frac is None:
        #accr_frac = 1 - (T-round(T))*cpnfreq        
        accr_frac = 0

    if cpn==0:
        accr_frac = 0
        
    N = T * cpnfreq
    price = face * ((cpn_n / ytm_n) * (1-(1+ytm_n)**(-N)) + (1+ytm_n)**(-N)) * (1+ytm_n)**(accr_frac)
    return price
