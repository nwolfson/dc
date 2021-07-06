import nidcpower
with nidcpower.Session(resource_name='PXI1Slot3', channels=0, reset=False, options={'simulate': True}) as session:
# Сначала подготавливается сессия для БП
    session.measure_record_length = 10   # Число измерений (если больше, чем 1, то нужно выставлять measure_when)
    session.measure_record_length_is_finite = True
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE # Определяет, когда проводятся измерения
    session.voltage_level_autorange = True # Выставлять флоут либо делать через рэндж/авторендж

    session.commit() # Включает БП с прописанными свойствами

    samples = 0
    with session.initiate():
        while samples < 10:
            measurements = session.fetch_multiple(count=10, timeout=1.0)
            samples += len(measurements)
            for i in range(len(measurements)):
                print(i+1,"Voltage = " + str(measurements[i].voltage)+ " V ","Current = " + str(measurements[i].current)+" A " )

    session.abort()