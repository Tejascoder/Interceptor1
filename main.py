from application import WeatherData
from framework import Framework

def main():
    framework_object= Framework()
    dispatcher = framework_object.create_dispatcher()
    #print(type(dispatcher))

    app= WeatherData()
    #create interceptors
    temp_interceptor= app.create_interceptor('temperature')
    pressure_interceptor = app.create_interceptor('pressure')
    convert_interceptor = app.create_interceptor('convert')

    #register interceptor
    app.register_interceptor(temp_interceptor,dispatcher)
    app.register_interceptor(pressure_interceptor,dispatcher)
    app.register_interceptor(convert_interceptor, dispatcher)

    #event 1 occurs
    framework_object.event(21.3, 4.44, 34.12)

    app.remove_interceptor(convert_interceptor, dispatcher)

    #event 2 occurs
    framework_object.event(80.3, 54.44, 64.12)

if __name__ == '__main__':
    main()
