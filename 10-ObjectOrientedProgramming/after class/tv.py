class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False


    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


    def set_channels(self, channels_list):
        self.channels.extend(channels_list)


    def show_channels(self):
        count = 1
        print("Channel list: \n", end = "")
        for element in self.channels:
            print(f"{count}. {element}")
            count += 1


    def show_status(self):
        try:
            if self.is_on:
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}")
            else:
                print("TV is off")

        except IndexError:
            print(f"TV is on, channel {self.channel_no}, volume {self.volume}")


    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume is max (10)")


    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is min (0)")
