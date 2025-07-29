
import shutil
import logging
import mimetypes #to see type of file
import validators #for checking is url
import os #to make dir
import re#to extract codes from instagram url
import instaloader #to download from instagram
import yt_dlp #to download videos from yt and other
import telegram
import traceback
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#section:logging
#############################################################################################################################################
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__) 

##############################################################################################################################################

#section:constants
###########################################################################################################################################################################

bot=telegram.Bot("<your token>")
# chat_id=''










extractor=''
website=''


#############################################################################################################################################################################



#section:to know which website it is and determine extractor has to be used
###########################################################################################################################################################################
def knowwebsiteandaddextractor(url):
  url=r"{}".format(url)
  print(1,url)
  print(2,'youtu.be' in url)
  if'youtube' in url or 'youtu.be' in url:
    return ["youtube","youtube"]
    

  elif 'instagram' in url:
    return ["instagram","instagram"]
    
   
  else:
    raise ValueError('Please check if this website is in  supported websites')
  









###########################################################################################################################################################################





#section:website-help 
###########################################################################################################################################################################
youtube_help="""

How To Download From Youtube
<link><flags>
link:Any youtube link
"""

instagram_help="""

 How To Download From Instagram
 <link><flags>
 <link>link to profile ,reel,post,story

 If the link is of a profile then flags-
 story-to download story 
 profilepic-to download profile picture

GETTING REELS POSTS STORY OF PRIVATE ACCOUNTS ARE NOT POSSIBLE





"""















###########################################################################################################################################################################







#section:list of commands .Used to check if it is one word or not
###########################################################################################################################################################################3
list_of_one_word_commands={"info"}


#############################################################################################################################################################################
#section:downloadfromlink
#############################################################################################################################################################################
def download_from_links(update,link,flags,chat_id):
   ##website will be second arg
  try:
         print("10",knowwebsiteandaddextractor(link))
         website,extractor=knowwebsiteandaddextractor(link)
         print(website)
         if website=="youtube":
            print(3,"came",website)
            downloadusingyt_dlp(update,link,flags,chat_id)
            print(90)
         elif website=="instagram":
            if r'/reel/' in link:

             downloadusingyt_dlp(update,link,flags,chat_id)

            else:
                downloadusinginstaloader(update,link,flags,chat_id)

         else:
          update.message.reply_text('This doesnt look like a website we support.If sending shortend link try sending full link.')
          return
  except Exception as e:
        update.message.reply_text("E6:Something unexpected happened.")
        print(traceback.format_exc())
            # to-edit=> add feeback mechanishm to see what site needs to be  included


  print(91)


###########################################################################################################################################################################

# section:showinfo
###########################################################################################################################################################################
def showinfo(update,website):
  website=website[0]
  if website not in supported_websites:
            update.message.reply_text("Sorry we dont support this site yet.")
            return

  update.message.reply_text(website_help[website])











#section:maindownloadfunctions
###########################################################################################################################################################################

#download using yt-dlp
def downloadusingyt_dlp(update,url,flags,chat_id):

 

  ydl_opts_if_audiovideoboth={
'format':'best [filesize<50M]',
'http_chunk_size':1000000,
'paths':{"home":"/{chatid}".format(chatid=chat_id)},
'ffmpeg_location':r'C:\Users\HP\Downloads\ffmpeg-master-latest-win64-gpl\bin'

        
        }

  ydl_opts_if_video_only={
  
'format':'bestvideo [filesize<50M]',
'http_chunk_size':1000000,
'paths':{"home":"/{chatid}".format(chatid=chat_id)},
'ffmpeg_location':r'C:\Users\HP\Downloads\ffmpeg-master-latest-win64-gpl\bin'

        
}
  ydl_opts_if_audio_only={
'format':'bestaudio [filesize<50M]',
'http_chunk_size':1000000,
'paths':{"home":"/{chatid}".format(chatid=chat_id)},
'ffmpeg_location':r'C:\Users\HP\Downloads\ffmpeg-master-latest-win64-gpl\bin',


        
        }












  url=r"{}".format(url)
 
  print(chat_id,"ppppp")
  try:
   print(os.path.join(os.getcwd(),str(chat_id)))
   print(os.getcwd()+str(chat_id))
   if os.path.exists(os.path.join(os.getcwd(),str(chat_id))):
    # Delete Folder 
    shutil.rmtree(os.path.join(os.getcwd(),str(chat_id)))
    print("!")
   os.mkdir('{path}'.format(path=chat_id))
#    to edit
   if len (flags)>1:
    update.message.reply_text("Invalid use of flags")
   update.message.reply_text("Downloading")  
   if len(flags)==0:
   #download just video
   
    with yt_dlp.YoutubeDL(ydl_opts_if_audiovideoboth) as ydl:
     ydl.download(url)
         
   elif 'audio' in flags:
    #download just audio
    with yt_dlp.YoutubeDL(ydl_opts_if_audio_only) as ydl:
     ydl.download(url)

   elif  'video' in flags:
    with yt_dlp.YoutubeDL(ydl_opts_if_video_only) as ydl:
     ydl.download(url)

  except Exception as e:
    print(e.with_traceback)
    update.message.reply_text("E1:Something unexpected happened.")
    print(traceback.format_exc())








def downloadusinginstaloader(update,url,flags,chat_id):
 url=r"{}".format(url)
 try:
  if os.path.exists(os.path.join(os.getcwd(),str(chat_id))):
      
    # Delete Folder code
    shutil.rmtree(os.path.join(os.getcwd(),str(chat_id)))
    #here we have to check what the link is of posts or profile
  if flags not in {'story','profilcpic'}:
    update.message.reply_text('Wrong flags given.See /help')
    return
  L = instaloader.Instaloader(download_video_thumbnails=False,max_connection_attempts=3,save_metadata=False,dirname_pattern="{chat_id}".format(chat_id=chat_id))
  
    #for post 
  try:
    if r'/p/' in url:
        #it is a post
        # now we have to extract the post code
        # now extracting post code
        #if flags are given return
        if len(flags)>0:
          
          update.message.reply_text('Flags should not be given ')
             
        pattern="(?:https?:\/\/www\.)?instagram\.com\/p\/(\w+)\/?"
        match=re.findall(pattern,url)
        if len(match)==0:
          raise ValueError
        post_shortcode=match[0]  
        
        #now code to download post
        posts=instaloader.Post.from_shortcode(L.context,post_shortcode)
        update.message.reply_text("Downloading Post")
        L.download_post(posts,posts.owner_username)  
               
        
          



    #for profile

    else:
      pattern="(?:https?:\/\/www\.)?instagram\.com\/([\w._]*)\/?"
      match=re.findall(pattern,url)
      if len(match)==0:
          raise ValueError
      profile_username=match[0] 
      
     #now here we have to check flags if flag is story then dwonalod story elese
      if len(flags)==0:
        update.message.reply_text("Flag was not specified about story or profile pic")
        return
     
      if "story" in flags:
        try:

         L.load_session_from_file("telegrambot162")
          
        except Exception as e:
          print(traceback.format_exc())
          pass
        try:
         L.login("telegrambot162", "password13!") 
        except Exception as e:
          print("Sorry couldn't process your request")
          print(traceback.format_exc())
        update.message.reply_text("Downloading stories ")
        L.download_profile(profile_username,download_stories_only=True,profile_pic=False)

      if "profilepic" in flags:
        update.message.reply_text("Downloading profile pic")
        L.download_profile(profile_username,profile_pic_only=True)









  except Exception as E:
          update.message.reply_text('E2:Something went wrong while checking url.')
          print(traceback.format_exc())


 except Exception as e:
    update.message.reply_text("E3:Something unexpected happened.")
    print(traceback.format_exc())
  
            
###########################################################################################################################################################################

#section:downloaderfunctionscalled
###########################################################################################################################################################################







###########################################################################################################################################################################
supported_websites=['youtube','instagram'] 

website_help={"youtube":youtube_help,"instagram":instagram_help}


#start 
def start(update, context):
    update.message.reply_text("""Hi There!
This is a bot to download  stuff from social media sites.
Note: Due to increasing strict policy of instagram about accessing it from bot there might be some problems in downloading from instagram.Working on improving
Please use '/help' for guide on how to use the bot.""")



def help(update, context):
    update.message.reply_text("""
    
The format of commands-
<link> <flags>
General Flags-
audio: To download audio only of a video
video: To download video only
(Specifying nothing will download both audio video)

Enter info <website name> for info about how to download from that website and corresponding flags
What can be downloaded
Youtube:   
Yotutube video
Youtube shorts
Youtube playlist

Instagram:

Instargram profile(all posts ,profile picture,everything)
Instagram profile picture
Instagram Stories
Instagram highlights
Instagram tagged
Instagram igtv
    
Facebook:
Reels

    
Currently suported sites:
    
Youtube
Instagram
Facebook
    """)




def info(update,context):
  try:
     message=update.message.text
     print(message)
     chat_id=update.message.chat_id
     # to remove ' ' we are converting to set then from set we are removing '' so that the '' are completetly removed
     message_splitted_list=message.split()
     print(message_splitted_list)
    #  message_splitted_set=set(message_splitted)
    #  print(message_splitted_set)
    #  if ' ' in message_splitted_set:
      # message_splitted_set.remove('')
    #  message_splitted_list=list(message_splitted_set)
     print(message_splitted_list)
     
  



     #keyword contain commanand check if second command is provided and tell what went wrong
     keyword=message_splitted_list[0]
     if keyword.lower() in list_of_one_word_commands and len(message_splitted_list)==1:
      
      if keyword.lower()=="info":
           update.message.reply_text("Please provide website name for info")
           return

     #flags is list of all flags seperately 
      # here this will not cause errors as flags will be there else they would have been denied in above if
     flags=message_splitted_list[1:]
     if validators.url(keyword)==True:
        download_from_links(update,keyword,flags,chat_id)
        print(93)
      
     #if keyword is info
      #----------INFO FUNCTION STARTS-------------
     elif(keyword.lower()=="info"):
        #website contains which website info is needed
          print("came here ")          
          showinfo(update,flags)
     
     else:
      print(keyword)
      update.message.reply_text("E0:Unrecognized input")
      return 
        
  except Exception as e:
        update.message.reply_text("E5:Something unexpected happened")
        print(traceback.format_exc())
        return
    
    
      #--------INFO FUNCTION ENDS----------


     
   

  
  
  #now we have to send files   
  try:
     loc=r"{loc}".format(loc=os.path.join(os.getcwd(),str(chat_id)))
     print(loc)
     if os.path.exists(loc):
      print(95)
      if len(os.listdir(loc))==0:
        raise ValueError("Empty directory")
      update.message.reply_text("Sending files.Please wait upto 3 minutes")
      for file in os.scandir(loc):
         type=mimetypes.guess_type(file.path)
         type_temp=type
         if(isinstance(type,tuple)):
          type_temp=type[0]
          print(type_temp)

          

             
          if 'audio' in type or 'audio' in type_temp: #if audio
            print("Sending audio")
            bot.send_audio(chat_id,audio=open(r"{filepath}".format(filepath=file.path),"rb"),timeout=5000)

          elif 'video' in type or 'video' in type_temp: #if video
            bot.send_video(chat_id,video=open(r"{filepath}".format(filepath=file.path),"rb"),timeout=9000)
            print("Sending video")
          
          elif 'image' in type or 'image' in type_temp: #if image 
            bot.send_photo(chat_id,image=open(r"{filepath}".format(filepath=file.path),"rb"))
          else: #if anything else -tobe send as document
            bot.send_document(chat_id,image=open(r"{filepath}".format(filepath=file.path),"rb"))
      else:
          pass

  except Exception as e:
        update.message.reply_text('Error occured In sending files')
        print(traceback.format_exc())








def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5648145804:AAFGzLMQN0pRE8cmIOKILzIie900mSfwAr0", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(MessageHandler(Filters.text, info))
    updater.start_polling() 
    updater.idle()

if __name__ == '__main__':
    main()
    


    

