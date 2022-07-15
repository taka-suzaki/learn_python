import speech_recognition as sr

class Speech_to_Text:
    def __init__(self):
        self.r = sr.Recognizer()
        # 閾値の自動調整. する場合はTrue
        # self.r.dynamic_energy_threshold = False
        # 閾値
        # self.r.energy_threshold = 300
        self.mic = sr.Microphone()
        self.text = ""

    def __call__(self, json_data):
        self.json_data = json_data
        self.catch_error()
        self.intent = json_data.get("intent", "")
        self.request = json_data.get("request", {})
        self.timeout = self.request.get("timeout", 15)
        self.json_data["timeout"] = False

        while True:
            self.recognize()
            self.audio_to_text()
            if self.intent != "":
                if self.text == "":
                    self.json_data["timeout"] = True
                break
            elif self.text != "":
                break
        self.json_data["contents"] = self.text
        
    def catch_error(self):
        if self.json_data is not None:
            if not isinstance(self.json_data, dict):
                raise TypeError("{} is not supported".format(type(self.json_data)))
        
    def recognize(self):
        print("Say something ...")
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source) #雑音対策
            self.audio = self.r.listen(source, timeout=self.timeout, phrase_time_limit=self.timeout)
            # self.audio = self.r.listen(source, timeout=self.timeout)
        print ("Now to recognize it...")
        
    def audio_to_text(self):
        try:
            self.text = self.r.recognize_google(self.audio, language='ja-JP')
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def func():
    StoT = Speech_to_Text()
    StoT(dict())
    print(StoT.text)
        
if __name__ == "__main__":
    from multiprocessing import Process
    p = Process(target=func,)
    p.start()