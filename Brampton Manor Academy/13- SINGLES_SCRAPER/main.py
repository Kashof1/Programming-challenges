import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def song_bracket_finder(html,i):
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)       
        newstring = html[open_tr:close_tr]
        return open_tr, close_tr, newstring
    
def itemfinder(html, lookingfor):
    i = 0
    itemlist = []
    count = 0
    while count<10:
        open_tr, close_tr, newstring = song_bracket_finder(html, i)
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find ('</', pos_start)
        largeitem = (newstring[pos_start + (len(lookingfor)):pos_end])
        small_item_start = largeitem.find('">')
        final_item = (largeitem[small_item_start+2:pos_end])
        i = close_tr
        count+=1
        itemlist.append(final_item)
    return itemlist


def name_finder(html):
    i = 0
    name_list = []
    count = 0
    while count < 10:
        open_tr, close_tr, newstring = song_bracket_finder(html, i)
        lookingfor = '<div class="title">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        item = (newstring[pos_start+(len(lookingfor)):pos_end])
        i = close_tr
        count+=1
        name_list.append(item)





if __name__ == "__main__":
    html = scrape(url)
    lookingfor_list = ['<div class="title">','<div class="artist">']
    song_list = itemfinder(html, lookingfor_list[0])
    artist_list = itemfinder(html,lookingfor_list[1])
    print ('------------------------------------------------------------------------------------------------------------------------')
    print (f"| {'POSITION':<10} | {'SONG NAME':50} | {'ARTIST':50} |")
    print ('------------------------------------------------------------------------------------------------------------------------')
    for x in range (10):
        print (f"| {x:<10} | {song_list[x]:50} | {artist_list[x]:50} |")
    print ('------------------------------------------------------------------------------------------------------------------------') 


#use a single abstracted function for all 3 functionalities
#pass in the lookingfor paramter into the function
#make a list with all the different variables that lookingfor can be, and iterate through the list and call the function as many times as needed