**************
from lib2to3.fixes.fix_imports import alternates
import datetime
from lib2to3.pgen2.tokenize import generate_tokens
import random
from shlex import join
from sys import displayhook
from turtle import getcanvas
#تعریف ژن های بکار رفت در این برنامه 
genset ="abcdefghijklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890!@#$%&* "
hadaf=input("lotfan password ra vared conid")
def motor_valed(lenght):
    gen =[]
    while len(gen)<lenght:
        andazehpas= min(lenght-len(gen),len(genset))
        gen.extend(random.sample(genset,andazehpas))
    return ''.join(gen)
#بهینه سازی توسط فیت نس
def get_fitn(hadskalameh):
    return sum(1 for expected , actual in zip(hadaf,hadskalameh)if expected==actual)
#جهش روی حدس کنونی 
def jahesh(valed):
    index= random.randrange(0,len(valed))
    genvares= list(valed)
    genjadid, alternate = random.sample(genset,2)
    genvares[index]= alternate\
          if genjadid==genvares[index]\
          else genjadid
    return '' .join(genvares)
#مانیتور کردن روند کار
def monitoring(hads_ha):
    tafavout_zamani=datetime.datetime.now() - shorohe_zaman
    behineh=get_fitn(hads_ha)
    print("{0}\t{1}\t{2}".format(hads_ha,behineh,str(tafavout_zamani)))
#برنامه اصلی و متور ژنتیک
random.seed()
shorohe_zaman=datetime.datetime.now()
behtarin_valed=motor_valed(len(hadaf))
behtaran_behineh=get_fitn(behtarin_valed)
monitoring(behtarin_valed)
#موتور
while True:
    vares=jahesh(behtarin_valed)
    behineh_vares=get_fitn(vares)
    if behtaran_behineh >= behineh_vares:
        continue
    monitoring(vares)
    if behineh_vares>= len(behtarin_valed):
        break
    behtaran_behineh= behineh_vares
    behtarin_valed=vares


      
