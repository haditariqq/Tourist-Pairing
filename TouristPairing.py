def touris_pairing(T,S):
    swap=True
    n=len(S)
    while swap:
        swap=False
        for index in range(n-1):
            if S[index]<S[index + 1]:
                temp=S[index]
                S[index] = S[index +1]
                S[index+1] = temp
                swap=True

    j=len(T)
    total_passengers=0
    for count in range(j):
        total_passengers=total_passengers + T(count)
    
    car_counter=0

    for passenger_counter in range(j):
        total_passengers=total_passengers - S(passenger_counter)
        car_counter=car_counter+1
        if total_passengers<=0:
            break
    
    return car_counter
