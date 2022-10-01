# define foot to meter
def footToMeter(foot1):
    meter1 = 0.305 * foot1
    return meter1

# define meter to foot
def meterToFoot(meter2):
    foot2 = meter2 / 0.305
    return foot2

# define main function
def main():
    print("==============================================================")
    print("||", format("Feet", "7s"), "|", format("Meter","7s"), "||", format("Meter", "7s"), "|", format("Foot", "7s"), "||")
    print("--------------------------------------------------------------")
    foot = 1
    meter = 20
    while foot < 11.0 and meter < 70:
        print("||", format(foot, "7.3f"), "|", format(footToMeter(foot),"7.3f"), "||", format(meter, "7.3f"), "|", format(meterToFoot(meter), "7.3f"), "||")
        foot += 1
        meter += 6

main()