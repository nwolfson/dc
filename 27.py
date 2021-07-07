import nidcpower
import matplotlib.pyplot as plt
import nidmm
with nidcpower.Session(resource_name='PXI1Slot3', channels=0, reset=False, options={'simulate': False}) as dc_session:
# Сначала подготавливается сессия для БП
    dc_session.measure_record_length = 10   # Число измерений (если больше, чем 1, то нужно выставлять measure_when)
    dc_session.measure_record_length_is_finite = True # Для проведения продолжительных измерений
    dc_session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE # Определяет, когда проводятся измерения
    dc_session.voltage_level_autorange = True # Выставлять флоут либо делать через рэндж/авторендж

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
                V.append(str(measurements[i].voltage)) # Списки для графиков заполняются
                C.append(str(measurements[i].current)) #
                print(dc_session.get_channel_name(1), i+1,"Voltage = " + str(measurements[i].voltage)+ " V ","Current = " + str(measurements[i].current)+" A ")
    plt.plot(V, C, color='m', linewidth=2)
    plt.show()
with nidmm.Session("Dev1") as dmm_session:
    dmm_session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
    print("Measurement: " + str(dmm_session.read()))
