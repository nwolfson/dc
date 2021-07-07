import nidcpower
with nidcpower.Session(resource_name='PXI1Slot3', channels=1, reset=False, options={'simulate': True}) as session:
    session.voltage_level = 5.0 # Выставлять флоут либо делать через рэндж/авторендж
    session.commit() # Включает БП с прописанными свойствами
    print(session.measure_multiple())