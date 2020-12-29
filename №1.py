from time import sleep

class TrafficLight:
    __color = ['RED LIGHT', 'YELLOW LIGHT', 'GREEN LIGHT']
    def running(self):
        for i in range(3):
            print("\033[31m {}".format(f'{TrafficLight.__color[0]}'))
            sleep(7)
            print("\033[33m {}".format(f'{TrafficLight.__color[1]}'))
            sleep(2)
            print("\033[32m {}".format(f'{TrafficLight.__color[2]}'))
            sleep(7)
            print("\033[37m {}".format('*' * 50))

start = TrafficLight()
start.running()
