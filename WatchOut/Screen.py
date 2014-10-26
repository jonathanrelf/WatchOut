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
        self.pfc.lcd.clear()