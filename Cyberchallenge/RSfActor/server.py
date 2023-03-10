import os
import signal

TIMEOUT = 100
FLAG = os.environ["FLAG"]
q = int(os.environ["q"])
p = int(os.environ["p"])


def handle():
    n = p*q
    e = 65537
    m=[]
    for ch in FLAG:
        m.append(ord(ch))
    
    C = []
    for ch in m:
        c = pow(ch, e, n)
        C.append(c)

    print("n = " + str(n))
    print("e = " + str(e))
    print("c = [", end="")
    for c in C:
        print(c,end = ", ")
    print("]")
    

    print("FF was added to database during this request. Thanks!")
    print("Gimme the flag!")
    
    guess = input()
    print(guess)
    if guess == FLAG:
        print("That's right!")
        print(FLAG)

        print("the meme:")
        f = open('ascii-art.txt', 'r')
        
        for line in f.readlines():
            print(line)

        f.close()
    else:
        print("Guess harder")


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()