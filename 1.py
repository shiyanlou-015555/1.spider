from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.tripadvisor.cn/'
requests.get(url)
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.title > a')
imgs = soup.select('img[width="368"]')
hotals = soup.select('div.counts')
a=[]
for i in range(0,len(titles)-1,2):
    b=""
    b=titles[i].get_text()
    b+="/"+titles[i+1].get_text()
    a.append(b)
for j in range(len(imgs)):
    data = {
        'title': a[j],
        'img': imgs[j].get('src'),
        'hotal': list(hotals[j].stripped_strings),
    }
    print(data)


'''
headers ={
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
'Cookie':' ServerPool=B; VRMCID=%1%V1*id.12019*llp.%2F*e.1537963926074; TART=%1%enc%3A3I4HMFpeklvSsFwizGEZFOLtE0m0WAifOtsq2l9J1rD8AXy8Lb%2Fh44m0zhOZX19PxI40gBDO%2FFs%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUnique=%1%enc%3AwVOXq7XSmY1vL3PIkyRJo6tfEAa9ptIbPxLgkDasmdFwKEuBfUNryQ%3D%3D; TASSK=enc%3AAIsrUJgiMiozhtMRcTjwdZi0g%2FBK45Wr93F1h3PMnym5VlIvDpW9zXk2eXhAGfdQh9Le7PbI8dk%2BxRuqgOsxXw80WPObLVXzTsoIawQpawMv7%2BE%2BOdt1mlautKZ2JOfvPg%3D%3D; _ga=GA1.2.2019518865.1537359128; _gid=GA1.2.350982211.1537359128; _smt_uid=5ba23d1e.8efc3fb; __gads=ID=625d6597abc42635:T=1537359135:S=ALNI_MYldUl0t6eeIkVFVeShUReV6QWQTQ; CommercePopunder=SuppressAll*1537359158309; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FTourism-g293920-Phuket-Vacations.html; roybatty=TNI1625!AF1YPKczt6jp4AIfjw6O5TLhpaltMVgXBxMhUhE6Hl660KnJ0B4PhF1qS9bBZJTY%2BPvjXLQlsjhVo86Vj82e61PLo5syWT%2BCoVfhc2DSyGaZIoR7%2FA4NZCm4XbgbgSEG0e7FLX2ClMn6aS9SvE2QanorLMlVzJfz9aQE2vL0CHnE%2C1; ki_t=1537363005338%3B1537363005338%3B1537363005338%3B1%3B1; ki_r=; _gat_UA-79743238-4=1; SecureLogin2=3.4%3AADxhQiN7THcSl9kHXUfw6pfQ056nkVbXU1RGhmxdeldsbWP%2FLviDvQjF7yeXmaf5J%2BE815A%2BsEr5aV2lquySeWcL%2Fobo1nhJUr6LfOU6AEGuUMf88borU7JLK%2BiN25wiMhL95vO13mTx4yLJSn3RSeFAEeizFeLepAX7cx2L1oZ2NYxP8PZ9CPWx0Q97mNLXqDr4HmBWcwOJLklQdBqVvrQ%3D; TAAuth3=3%3A08c03e87fb383d2a714613271e7c1617%3AADPi%2FgT7yetzbiagJB39QgJM%2FJTXYbkcN0pV4kJ%2FTybL60N1PpmWP06AzCLU4WAvkaDibqujjCXpxwz6YqXqPoL7mbT9AKzso71ZkYV3ETUlD9QL4bZQY4KEDulatmpV646AYwmgrwoUiCEelhE9UIVRTqb%2FPLfro%2BM88s9JlPxYW4tu%2BvRwByf%2Bk%2BFc2v8rdQ%3D%3D; TASession=%1%V2ID.41F50A7494ACBF88B4335541C9DA00AF*SQ.44*MC.12019*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Flink%3Furl%3DJRi7_lCIKbFQr7IxJlNRKmmEZLC1MMjcX4-CqMtPdBlOoR3_hi4mrmhU2bqJnkAu%26wd%3D%26eqid%3Db18e1cbe0009895a000000035ba23d14*LP.%2F*PR.427%7C*LS.MetaPlacementAjax*GR.82*TCPAR.47*TBR.85*EXEX.48*ABTR.25*PHTB.40*FS.0*CPU.66*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.54095683591A994789548D050EA06F0F*FA.1*DF.0*MS.-1*RMS.-1*FLO.293920*TRA.true*LD.293920; TAUD=LA-1537359126128-1*RDD-1-2018_09_19*LG-3961902-2.1.F.*LD-3961903-.....'
}

url_saves = 'https://www.tripadvisor.cn/'
#url_saves='https://www.tripadvisor.cn/Hotels-g294212-Beijing-Hotels.html#apg=a251b6ef4d0a42d99e29b7d7df421538&ss=7A121B5D1B8348E36830DBD7762C32D3'
wb_data = requests.get(url_saves)
time.sleep(2)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.title > a')
print(titles)
imgs = soup.select('img[width="368"]')
hotals = soup.select('div.counts')
for title,img,hotal in zip(titles,imgs,hotals):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'hotal': list(hotal.stripped_strings),
    }
    print(data)

'''