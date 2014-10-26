import pifacecad


class Screen:
    pfc_base = pifacecad
    pfc = pifacecad.PiFaceCAD()

    def update_display(self, text=""):
        self.pfc.lcd.set_cursor(0,0)
        self.pfc.lcd.write(text)

    def update_display(self, text="", text2=""):
        self.pfc.lcd.set_cursor(0,0)
        self.pfc.lcd.write(text+"\n"+text2)

    def clear_display(self):
        print("Clear Display")
        self.pfc.lcd.clear()

    def hide_cursors(self):
        self.pfc.lcd.cursor_off()
        self.pfc.lcd.blink_off()