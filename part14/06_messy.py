def shipping_fee( weight,region ):
    fees={'서울':3000,"부산":3500 }
    fee=fees.get(region,5000)
    if weight>10 : fee=fee+2000
    return fee
