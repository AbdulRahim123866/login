# class LegacySystem:
#     def specific_requist(self):
#         return "Legacy system behavior"
# class Target:
#     def request(self):
#         pass
#
# #Multiple inheritance approach (Python-specific)
# #هاض الاسلوب هو الاسلوب الاصح لانه انا ما بدي السيستيم القدديم بدي التعديل الجديد بس
# # class ClassAdapter(Target,):
# #     def __init__(self,adaptee):
# #         self.adaptee=adaptee
# #
# #     def request(self):
# #         return f"Adapter: {self.adaptee.specific_requist()}"
# # #______________
# class ClassAdapter(Target,LegacySystem):
#     def __init__(self,):
#         # self.adaptee=adaptee
#         pass
#
#
#     def request(self):
#         return f"Adapter: {self.specific_requist()}"
#
#
# # ls=LegacySystem()
# # adapter=ClassAdapter(ls)
# # print(adapter.request())
# # print(adapter.specific_requist())
# # # print(ClassAdapter.mro())
#
# #_________________
#
# # ls=LegacySystem()
# adapter=ClassAdapter()
# print(adapter.request())
# print(adapter.specific_requist())
# # print(ClassAdapter.mro())
#

#important Example
class MediaPlayer:
    def play(self, filename: str) -> None:
        raise NotImplementedError


class VLCPlayer:
    def play_vlc(self, filename: str) -> None:
        print(f"Playing VLC file: {filename}")


class MP4Player:
    def play_mp4(self, filename: str) -> None:
        print(f"Playing MP4 file: {filename}")


# Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, media_type: str):
        if media_type == "vlc":
            self.player = VLCPlayer()
            self.method = self.player.play_vlc
        elif media_type == "mp4":
            self.player = MP4Player()
            self.method = self.player.play_mp4
        else:
            raise ValueError("Unsupported media type")

    def play(self, filename: str) -> None:
        self.method(filename)


# Client
class AudioPlayer(MediaPlayer):
    def play(self, filename: str) -> None:
        if filename.endswith(".mp3"):
            print(f"Playing mp3 file: {filename}")
        elif filename.endswith(".vlc"):
            adapter = MediaAdapter("vlc")
            adapter.play(filename)
        elif filename.endswith(".mp4"):
            adapter = MediaAdapter("mp4")
            adapter.play(filename)
        else:
            print(f"Unsupported file format: {filename}")


if __name__ == "__main__":
    player = AudioPlayer()
    player.play("song.mp3")
    player.play("video.vlc")
    player.play("movie.mp4")
    player.play("podcast.wav")

#
# class MediaPlayer:
#     def play(self,filename:str)->None:
#         raise NotImplementedError
# class VLCPlayer:
#     def play_vlc(self,filename:str)->None:
#         print(f"Playing VLC file: {filename}")
# class MP4Player:
#     def play_mp4(self,filename:str)->None:
#         print(f"Playing MP4 file:{filename}")
# #Adapter
# class MediaAdapter(MediaPlayer):
#     def __init__(self,media_type:str):
#         if media_type=="vlc":
#             self.player=VLCPlayer()
#         elif media_type=="mp4":
#             self.player=MP4Player()
#         else:
#             raise ValueError("Unsupported media type")
# #Client
# class AudioPlayer(MediaPlayer):
#     def play(self,filename:str) ->None:
#         if filename.endswith(".mp3"):
#             print(f"Playing mp3 file: {filename}")
#         elif filename.endswith(".vlc"):
#             adapter=MediaAdapter("vlc")
#             adapter.play(filename)
#         elif filename.endswith(".mp4"):
#             adapter=MediaAdapter("mp4")
#             adapter.play(filename)
#         else:
#             print(f"Unsipported file format: {filename}")
#         # adapter=MediaAdapter(filename.rsplit('.')[-1])
#         # adapter.play(filename)
# if __name__=="__main__":
#     player=AudioPlayer()
#     player.play("song.mp3")
#     player.play("video.vlc")
#     player.play("movie.mp4")
#     player.play("podcast.wav")