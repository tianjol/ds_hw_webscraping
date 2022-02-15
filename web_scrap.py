import urllib.request, json, timeit, pandas as pd

shopee_url = "https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=minyak%20goreng&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
print(shopee_url)
with urllib.request.urlopen(shopee_url) as url:
    data_shopee = json.loads(url.read().decode())
    
type(data_shopee)
df_shopee=pd.DataFrame.from_dict(data_shopee,orient='index')
df_shopee=pd.DataFrame(df_shopee.transpose())

type(df_shopee['items'][0][0])
#df_shopee['items'][0][0]

daftar=pd.DataFrame(df_shopee['items'][0])
aaa=daftar['item_basic']
len(aaa)
data_barang={}
df_data_barangs=pd.DataFrame(data_barang)
for x in range(0,len(aaa)):
    data_barang["nama_barang"] = aaa[x]['name']
    data_barang["harga_barang"] = int(aaa[x]['price'])/100000
    df_data_barang=pd.DataFrame(data_barang, index=[x])
    #df_data_barangs.append(df_data_barang)
    df_data_barangs = df_data_barangs.append(df_data_barang)
#data_barang

type(df_data_barang)    
df_data_barangs['harga_barang']
df_data_barangs.to_csv('D:\\tutor\\digital skola\\hw\\latian 13\\ds_hw_webscraping\\hasil_scrap_barang.csv', index = False)
      
  


