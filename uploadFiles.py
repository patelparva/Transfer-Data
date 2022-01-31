import os
from posixpath import relpath
import dropbox

class TransferData():
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for file in files:
                local_path=os.path.join(root,file)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=dropbox.files.WriteMode.overwrite)
        
        print('Files uploaded Successfully.')

def main():
    access_token='sl.BBLAwSEp9JHjh-lesuvFBqOALPHsSJ7GEn2hU78AAAseBjucu6JsKTjKeTJJQ3WDg9UyXdiHzoOYD7ff8gPP-vd1BXjFAzGB8_cjvgzipP4V6U9huBTyfhF1bVn2OdJPUmXUoofxpqYJ'
    transferData=TransferData(access_token)

    file_from=input('Enter the folder\'s path from which you want to upload the file ')
    file_to=input('In Dropbox, Which Folder you want to upload this files ')

    transferData.upload_file(file_from,file_to)

if __name__ == '__main__':
    main()