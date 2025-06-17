import itertools
import threading
import sys
import time


def loading_animation():
    done = False

    # here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rLoading..' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\n')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(6)
    done = True
