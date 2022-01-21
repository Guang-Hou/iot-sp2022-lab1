from time import sleep
import picar_4wd as fc

speed = 40


def main():
    while True:
        scan_list = fc.scan_step(37)
        if not scan_list:
            continue
        
        left_signal = scan_list[:3]
        forward_signal = scan_list[3:7]
        right_signal = scan_list[7:]

        if forward_signal != [2, 2, 2, 2]:   # there is obstacle ahead
            fc.backward(speed)
            sleep(0.3)
            if left_signal == [2, 2, 2]:     # left direction clear
                fc.turn_left(speed)
                sleep(0.2)
            elif right_signal == [2, 2, 2]:  # right direction clear
                fc.turn_right(speed)
                sleep(0.2)
            else:                            # obstacles in all three directions
                break
        else:                                # no obstacle ahead
            fc.forward(speed)
            sleep(0.3)

    fc.stop()


if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()