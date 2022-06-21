from youtubesearchpython import Search #pip install youtube-search-python
from pytube import YouTube #pip install pytube
from moviepy.editor import VideoFileClip #pip install moviepy
import os,httpx

class Engine:
    def __init__(self):
        def clear():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        clear()
        text = """
        ###################################################
        - MiniYTUBE'A HOSGELDİN
            - Istediğin gibi arama yapıp,istediğin videoyu indirebilirsin
            - Mp3 ve Mp4 formatları
            - Yüksek kalite
        ###################################################
        
        """
        print(text)
    
    def searchMotor(self):
        try:
            try:
                print("*Not: Arama limitini 40 dan fazla girerseniz hata alabilirsiniz.")
                arama_limiti = int(input("Arama Limitini giriniz: "))
                self.search = input("Arama: ")
                self.allSearch = Search(self.search, limit = arama_limiti)
                results = self.allSearch.result()["result"]
                try:
                    for i in range(arama_limiti):
                        title = results[i]["title"]
                        channel = results[i]["channel"]["name"]
                        view = results[i]["viewCount"]["text"]
                        print(f"[{i}] {title}, Channel: {channel}, VIEW: {view}")
                except IndexError:
                    print("### DAHA FAZLA SECENEK BULUNMAMAKTADIR ###")
                print("-"*100)
                slt = int(input("Seçimin: "))
                if slt > arama_limiti:
                    print("### LİMİTİ AŞMA! ###")
                else:
                    text_two = f"""
                    *********************************************************
                    ---------------------------------------------------------
                    Video:
                        - Ismi : {results[slt]['title']}
                        - Kanal adı : {results[slt]['channel']['name']}
                        - Izlenme : {results[slt]['viewCount']['text']}
                        - URL : {results[slt]["link"]}
                    Indirme:
                        1 - Mp4 olarak indir
                        2 - Mp3 olarak indir
                        3 - Çıkış yap
                    ---------------------------------------------------------
                    *********************************************************
                    """
                    print(text_two)
                    information = f"Title: {results[slt]['title']}\nChannel: {results[slt]['channel']['name']}\nView: {results[slt]['viewCount']['text']}\nURL: {results[slt]['link']}"
                    dosya = open(f"{results[slt]['title']}.txt","w",encoding="utf-8").write(str(information))
                    while True:
                        download = int(input("Seçimin: "))
                        if download == 1:
                            self.motor(results[slt]["link"],"mp4")
                            print("INDIRME ISLEMI BASARILI!")
                            break
                        elif download == 2:
                            self.motor(results[slt]["link"],"mp3")
                            print("INDIRME ISLEMI BASARILI!")
                            break
                        elif download == 3:
                            print("Yine Bekleriz..")
                            break
                        else:
                            print("## YANLIS SECİM ##")
            except ValueError:
                print("INT ERROR")
        except httpx.ConnectError:
            os.system("cls")
            print("Internet Bağlantınızı Kontrol Ediniz!")

    def motor(self,url,format = "mp4"):
        if format == "mp4":
            mp4 = YouTube(url).streams.get_highest_resolution().download()
                                      
        elif format == "mp3":
            mp4 = YouTube(url).streams.get_highest_resolution().download()
            mp3 = mp4.split(".mp4",1)[0] + ".mp3"
                
            video_clip = VideoFileClip(mp4)
            audio = video_clip.audio
            audio.write_audiofile(mp3)
                
            audio.close()
            video_clip.close()
                
            os.remove(mp4)


e = Engine()
e.searchMotor()
