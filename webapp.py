from flask import Flask, render_template, request, url_for
from urllib.request import urlopen 
from pymongo import MongoClient
import json
import os
import pandas as pd
#Client
client = MongoClient()
#Database
db = client.mydb
#Collections
links = db.linkds
movies = db.movieds
lnk = pd.DataFrame(list(links.find()))
mov = pd.DataFrame(list(movies.find()))
source = []
names = []
tmdbid = list(lnk[lnk.columns[3]])
movname = list(mov[mov.columns[3]])
movid = list(mov[mov.columns[2]])

#Global variables
for i in range(links.find().count()):
	response = urlopen("https://api.themoviedb.org/3/movie/"+str(tmdbid[i])+"?api_key=78077b8e590c738712916712631f58a3")
	data = json.load(response)
	try:
		imgPath = data['poster_path']
	except:
		imgPath = data['backdrop_path']
	source.append("https://image.tmdb.org/t/p/w185"+imgPath)
	names.append(movname[i])

userrate = []

def rate():
	if request.method() == 'POST':
		userrate = request.form['Submit']

app = Flask(__name__)
@app.route('/0')
def home():
    img1 = source[0]
    img2 = source[1]
    img3 = source[2]
    img4 = source[3]
    img5 = source[4]
    img6 = source[5]
    img7 = source[6]
    img8 = source[7]
    img9 = source[8]
    img10 = source[9]
    return render_template("index.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[0],m2=names[1],m3=names[2],m4=names[3],m5=names[4],m6=names[5],m7=names[6],m8=names[7],m9=names[8],m10=names[9])

@app.route('/1')
def home1():
    img1 = source[10]
    img2 = source[11]
    img3 = source[12]
    img4 = source[13]
    img5 = source[14]
    img6 = source[15]
    img7 = source[16]
    img8 = source[17]
    img9 = source[18]
    img10 = source[19]
    return render_template("index1.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[10],m2=names[11],m3=names[12],m4=names[13],m5=names[14],m6=names[15],m7=names[16],m8=names[17],m9=names[18],m10=names[19])

@app.route('/2')
def home2():
    img1 = source[20]
    img2 = source[21]
    img3 = source[22]
    img4 = source[23]
    img5 = source[24]
    img6 = source[25]
    img7 = source[26]
    img8 = source[27]
    img9 = source[28]
    img10 = source[29]
    return render_template("index2.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[20],m2=names[21],m3=names[22],m4=names[23],m5=names[24],m6=names[25],m7=names[26],m8=names[27],m9=names[28],m10=names[29])

@app.route('/3')
def home3():
    img1 = source[30]
    img2 = source[31]
    img3 = source[32]
    img4 = source[33]
    img5 = source[34]
    img6 = source[35]
    img7 = source[36]
    img8 = source[37]
    img9 = source[38]
    img10 = source[39]
    return render_template("index3.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[30],m2=names[31],m3=names[32],m4=names[33],m5=names[34],m6=names[35],m7=names[36],m8=names[37],m9=names[38],m10=names[39])

@app.route('/4')
def home4():
    img1 = source[40]
    img2 = source[41]
    img3 = source[42]
    img4 = source[43]
    img5 = source[44]
    img6 = source[45]
    img7 = source[46]
    img8 = source[47]
    img9 = source[48]
    img10 = source[49]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[40],m2=names[41],m3=names[42],m4=names[43],m5=names[44],m6=names[45],m7=names[46],m8=names[47],m9=names[48],m10=names[49])

@app.route('/5')
def home5():
    img1 = source[50]
    img2 = source[51]
    img3 = source[52]
    img4 = source[53]
    img5 = source[54]
    img6 = source[55]
    img7 = source[56]
    img8 = source[57]
    img9 = source[58]
    img10 = source[59]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[50],m2=names[51],m3=names[52],m4=names[53],m5=names[54],m6=names[55],m7=names[56],m8=names[57],m9=names[58],m10=names[59])

@app.route('/6')
def home6():
    img1 = source[60]
    img2 = source[61]
    img3 = source[62]
    img4 = source[63]
    img5 = source[64]
    img6 = source[65]
    img7 = source[66]
    img8 = source[67]
    img9 = source[68]
    img10 = source[69]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[60],m2=names[61],m3=names[62],m4=names[63],m5=names[64],m6=names[65],m7=names[66],m8=names[67],m9=names[68],m10=names[69])

@app.route('/7')
def home7():
    img1 = source[70]
    img2 = source[71]
    img3 = source[72]
    img4 = source[73]
    img5 = source[74]
    img6 = source[75]
    img7 = source[76]
    img8 = source[77]
    img9 = source[78]
    img10 = source[79]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[70],m2=names[71],m3=names[72],m4=names[73],m5=names[74],m6=names[75],m7=names[76],m8=names[77],m9=names[78],m10=names[79])

@app.route('/8')
def home8():
    img1 = source[80]
    img2 = source[81]
    img3 = source[82]
    img4 = source[83]
    img5 = source[84]
    img6 = source[85]
    img7 = source[86]
    img8 = source[87]
    img9 = source[88]
    img10 = source[89]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[80],m2=names[81],m3=names[82],m4=names[83],m5=names[84],m6=names[85],m7=names[86],m8=names[87],m9=names[88],m10=names[89])

@app.route('/9')
def home9():
    img1 = source[90]
    img2 = source[91]
    img3 = source[92]
    img4 = source[93]
    img5 = source[94]
    img6 = source[95]
    img7 = source[96]
    img8 = source[97]
    img9 = source[98]
    img10 = source[99]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[90],m2=names[91],m3=names[92],m4=names[93],m5=names[94],m6=names[95],m7=names[96],m8=names[97],m9=names[98],m10=names[99])

@app.route('/10')
def home10():
    img1 = source[100]
    img2 = source[101]
    img3 = source[102]
    img4 = source[103]
    img5 = source[104]
    img6 = source[105]
    img7 = source[106]
    img8 = source[107]
    img9 = source[108]
    img10 = source[109]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[100],m2=names[101],m3=names[102],m4=names[103],m5=names[104],m6=names[105],m7=names[106],m8=names[107],m9=names[108],m10=names[109])

@app.route('/11')
def home11():
    img1 = source[110]
    img2 = source[111]
    img3 = source[112]
    img4 = source[113]
    img5 = source[114]
    img6 = source[115]
    img7 = source[116]
    img8 = source[117]
    img9 = source[118]
    img10 = source[119]
    return render_template("index4.html", user_image1 = img1 ,user_image2 = img2 ,user_image3 = img3 ,user_image4 = img4 ,user_image5 = img5 ,user_image6 = img6,user_image7 = img7,user_image8 = img8,user_image9 = img9,user_image10 = img10,m1=names[110],m2=names[111],m3=names[112],m4=names[113],m5=names[114],m6=names[115],m7=names[116],m8=names[117],m9=names[118],m10=names[119])

@app.route('/RateYourMovie')
def rate():
    return "NOT FOUND"

if __name__ == "__main__":
    app.run()
