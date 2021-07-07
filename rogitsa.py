import nidcpower
import matplotlib.pyplot as plt


def some_func(dc_session):
    dc_session.measure_record_length = 10   # Число измерений (если больше, чем 1, то нужно выставлять measure_when)
    dc_session.measure_record_length_is_finite = True # Для проведения продолжительных измерений
    dc_session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE # Определяет, когда проводятся измерения
    dc_session.voltage_level = 27  # Выставлять флоут либо делать через рэндж/авторендж

    dc_session.commit() # Включает БП с прописанными свойствами

    summary_samples = 10 # Всего измерений
    samples = 0 # Текущее число измерений
# Заготовка для вахи
    plt.figure(dpi=120)
    plt.xlabel('Voltage', fontsize=10)
    plt.ylabel('Current', fontsize=10)
    plt.grid()

    V = [] # Списки для графиков
    C = [] #

    with dc_session.initiate(): # Пошли измерения
        while samples < summary_samples:
            measurements = dc_session.fetch_multiple(count=summary_samples, timeout=1.0) # Возврат измерений из буфера
            samples += len(measurements) # Счетчик измерений
            for i in range(len(measurements)):
                V.append(round(measurements[i].voltage, 3)) # Списки для графиков заполняются
                C.append(measurements[i].current)
                print(dc_session.get_channel_name(1), i+1,"Voltage = " + str(measurements[i].voltage)+ " V ","Current = " + str(measurements[i].current)+" A ")
    plt.plot(V, C, color='m', linewidth=2)
    plt.show()
    dc_session.reset()


with nidcpower.Session(resource_name='PXI1Slot3', channels=0, reset=True, options={'simulate': False}) as dc_session:
    subsession = nidcpower.Session(resource_name='PXI1Slot3', channels=1, reset=True, options={'simulate': False})
    some_func(subsession)
# Сначала подготавливается сессия для БП
    dc_session.measure_record_length = 10   # Число измерений (если больше, чем 1, то нужно выставлять measure_when)
    dc_session.measure_record_length_is_finite = True # Для проведения продолжительных измерений
    dc_session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE # Определяет, когда проводятся измерения
    dc_session.voltage_level = 27  # Выставлять флоут либо делать через рэндж/авторендж

    dc_session.commit() # Включает БП с прописанными свойствами

    summary_samples = 10 # Всего измерений
    samples = 0 # Текущее число измерений
# Заготовка для вахи
    plt.figure(dpi=120)
    plt.xlabel('Voltage', fontsize=10)
    plt.ylabel('Current', fontsize=10)
    plt.grid()

    V = [] # Списки для графиков
    C = [] #

    with dc_session.initiate(): # Пошли измерения
        while samples < summary_samples:
            measurements = dc_session.fetch_multiple(count=summary_samples, timeout=1.0) # Возврат измерений из буфера
            samples += len(measurements) # Счетчик измерений
            for i in range(len(measurements)):
                V.append(round(measurements[i].voltage, 3)) # Списки для графиков заполняются
                C.append(measurements[i].current)
                print(dc_session.get_channel_name(1), i+1,"Voltage = " + str(measurements[i].voltage)+ " V ","Current = " + str(measurements[i].current)+" A ")
    plt.plot(V, C, color='m', linewidth=2)
    plt.show()
    dc_session.reset()
