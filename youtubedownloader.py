from pytube import YouTube

status = 0

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    global status

    total = stream.filesize
    bytes_downloaded = total - bytes_remaining
    char_amount = int((bytes_downloaded*10)/total)

    if(char_amount > status):
        status = char_amount
        string = "[----------]"
        string = string.replace("-","+",status)
        print(string)

    return


def show_dl_completed_message(stream,file_handle):
    print("File downloaded")
    return


url = input("Type video's link ")
path = input("Type download's directory ")
download = YouTube(url)
download.register_on_progress_callback(show_progress_bar)
download.register_on_complete_callback(show_dl_completed_message)
print("Starting the download...")
download.streams.filter(progressive=True).first().download(path)
