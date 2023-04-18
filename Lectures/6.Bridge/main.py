from bridge import RemoteControl, AdvancedRemoteControl, SonyTv, SamsungTv


def main():
    remote_control = AdvancedRemoteControl(SamsungTv())
    remote_control.turn_on()


if __name__ == '__main__':
    main()
