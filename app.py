########################################DATA PROCESSING ##########################################################

import streamlit as st
from process.process_data import *
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from dao.get_featured import *
from dao.get_dark import *
from dao.get_action import *
from dao.get_f2p import *
from dao.get_racing import *
from dao.contact_form import *

############################################UX/UI###################################################################################

# Streamlit UI

st.set_page_config(
    page_title="Game Recommender System",
    page_icon="🎮"
)

st.image("img/header.png",use_column_width=True)
######################SET BACKGROUND##########################
import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("img/background.jpg")

page_bg_img = f"""
<style>
    [data-testid="stAppViewContainer"]{{
        background-image: url("data:image/png;base64,{img}");
        background-position: center; 
    }}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


selected = option_menu(
    menu_title=None,
    options = ["Home Page","Recommend","Contact"],
    icons=["house","controller","envelope"],
    default_index=0,
    orientation="horizontal"
)
if selected == "Recommend":
#####################Xu ly game##########################
    game_list = games['name'].values
    selected_game = st.selectbox('Chọn game mà bạn muốn', game_list)

    if st.button("Show RECOMMENDATION"):
        games_goi_y = get_recommendations(selected_game)
        st.subheader("Bởi vì bạn đã chơi " + selected_game)

       
        # Danh sách URL hình ảnh
        for i in range(0,20):
          game = top_action.iloc[i]
          game_name = game['name']
          game_url = "https://store.steampowered.com/app/" + str(game['appid'])
          header_image = game['header_image']
          price = game['price']*25427.50
          formatted_price = '{:,.2f}'.format(price)
          f_price = str(formatted_price)
          short_description = game['short_description']
          release_date = game['release_date']
          developer = game['developer']
          publisher = game['publisher']
          tags = game['steamspy_tags']
          tags = eval(tags)
          thumbnail_urls = get_path_thumbnails(game['screenshots'])
          html_output = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{box-sizing: border-box}}
body {{font-family: Arial, Helvetica, sans-serif;; margin:0}}
.mySlides {{
  display: none;
  justify-content: center;
  align-items: center;
  display: flex;
}}

.main_container{{
  display: flex;
  padding:10px;
  position:relative;
  top:5px;
  background:#c7d5e0;
  flex-direction: column;
  border-radius: 25px;
  height:455px;
}}
/* Slideshow container */
.slideshow-container {{
  display: flex;
  position: relative;
  width: 100%;
  justify-content: center;
  align-items: center;
  border: 1px solid #c7d5e0;
  background: black;
  height: 240px;
  border-radius: 10px;
}}

.container{{
  display: flex;
  flex-direction: row;
}}

.slide_show{{
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 60%;
}}

.info{{
  width: 40%;
  margin-left: 10px;
}}
.short_description{{
  height: 6em; /* Khoảng chiều cao cho 3-4 dòng văn bản */
  overflow: hidden; /* Ẩn phần nội dung vượt quá */
  display: -webkit-box;
  -webkit-line-clamp: 4; /* Số dòng tối đa */
  -webkit-box-orient: vertical;
  line-height: 1.5em; 
  font-size: 12px;
  margin-bottom: 15px;
}}

.header{{
  background-color: black; 
  -webkit-background-clip: text; 
  -webkit-text-fill-color: transparent;
}}

.text{{
  display: flex;
  flex-direction: row;
  margin-bottom: 3px;
}}
#toggleButton{{
  font-size: 12px;
}}
#collapseButton{{
  font-size: 12px;
}}
.text-dev-publ{{
  font-size: 12px;
  display: block;
}}
.boild{{
  color:#1B2838;
  font-size: 12px;
  width: 95px;
}}
#content{{
  margin-left: 5px;
}}
.headerdiv{{
  margin-left: 10px;
}}
.hidden{{
  display: none;
}}
/* Next & previous buttons */
.prev, .next {{
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}}

/* Position the "next button" to the right */
.next {{
  right: 0;
  border-radius: 3px 0 0 3px;
}}
.prev {{
  left: 0;
  border-radius: 3px 0 0 3px;
}}
/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {{
  background-color: rgba(0,0,0,0.8);
}}


/* The dots/bullets/indicators */
.dot {{
  cursor: pointer;
  height: 10px;
  width: 10px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}}

.active, .dot:hover {{
  background-color: #717171;
}}

/* Fading animation */
.fade {{
  animation-name: fade;
  animation-duration: 1.5s;
}}

@keyframes fade {{
  from {{opacity: .4}} 
  to {{opacity: 1}}
}}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {{
  .prev, .next,.text {{font-size: 11px}}
}}
</style>
</head>
<body>
<div class="main_container">
  <div class="headerdiv">
    <h4 class="header">
      <a href="{game_url}" target="_blank">{game_name}</a>
    </h4>
  </div>
  <div class="container".
    <!-- Container for the image gallery -->
    <div class="slide_show">
      <div class="slideshow-container">
        {" ".join([f'<div class="mySlides fade"><img src="{thub}" style="width:100%; border-radius:10px; height: 223px;vertical-align: middle;"></div>' for thub in thumbnail_urls])}
        <a class="prev" onclick="plusSlides(-1)">❮</a>
        <a class="next" onclick="plusSlides(1)">❯</a>
      </div>
      <div style="margin-bottom: 20px">
        {" ".join([f'<span class="dot" onclick="currentSlide({i + 1})"></span>' for i in range(len(thumbnail_urls))])}
      </div>
      <div>{" ".join([f'<div style="color: #66c0f4;padding: 2px 4px; margin: 2px; display: inline-block; background:#2a475e; border-radius: 5px;font-size:14px">{tag}</div>' for tag in tags])}</div>
    </div>

    <div class="info">
      <img src="{header_image}" alt="Header Image" style="width: 100%; border-radius: 5px;">
      <div class="short_description">{short_description}</div>
      <div class="text">
        <b class="boild">Release Date:</b>
        <div style="color:#1B2838; font-size: 12px;margin-left: 5px">{release_date}</div>
      </div>
      <div class="text">
        <b class="boild">Developer:</b>
        <div id="content">
"""
          if(len(developer)>2):
            html_output += " ".join([f'<a class = "text-dev-publ">{developer[i]}</a>' for i in range(0,2)])
            html_output += " ".join([f'<a class = "text-dev-publ hidden">{developer[i]}</a>' for i in range(2,len(developer))])
            html_output += """<button id="toggleButton">Extend</button>
                        <button id="collapseButton" class="hidden">Collapse</button>
                    """
          else:
            html_output += " ".join([f'<a class = "text-dev-publ">{dev}</a>' for dev in developer])
      
          html_output += f"""
        </div>
      </div>
      <div class="text">
        <b class="boild">Publisher:</b>
        <div id="content">
          {" ".join([f'<a class = "text-dev-publ">{pub}</a>' for pub in publisher])}
        </div>
      </div>
      <h5 style ="color: #BEEE11;background: #4c6b22; text-align: center; margin-top: 10px; padding: 10px; margin-left:40%;">
        {f_price} ₫
      </h5>
    </div>
  </div>
</div>

<script>
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {{
  showSlides(slideIndex += n);
}}

function currentSlide(n) {{
  showSlides(slideIndex = n);
}}

function showSlides(n) {{
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {{slideIndex = 1}}    
  if (n < 1) {{slideIndex = slides.length}}
  for (i = 0; i < slides.length; i++) {{
    slides[i].style.display = "none";  
  }}
  for (i = 0; i < dots.length; i++) {{
    dots[i].className = dots[i].className.replace(" active", "");
  }}
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}}
</script>
<script>
 document.getElementById('toggleButton').addEventListener('click', function() {{
    var hiddenDevs = document.querySelectorAll('#content a.hidden');
    hiddenDevs.forEach(function(dev) {{
        dev.classList.remove('hidden');
    }});
    this.classList.add('hidden'); // Ẩn nút "Extend"
    document.getElementById('collapseButton').classList.remove('hidden'); // Hiển thị nút "Collapse"
}});

document.getElementById('collapseButton').addEventListener('click', function() {{
    var allDevs = document.querySelectorAll('#content a');
    allDevs.forEach(function(dev, index) {{
        if (index >= 2) {{
            dev.classList.add('hidden');
        }}
    }});
    document.getElementById('toggleButton').classList.remove('hidden'); // Hiển thị nút "Extend"
    this.classList.add('hidden'); // Ẩn nút "Collapse"
}});
</script>
</body>
</html> 
"""
          components.html(html_output, height=475)
if selected == "Contact":
    contact()
    
if selected == "Home Page":
    st.header("TOP GAMES")
    select01 = option_menu(
    menu_title=None,
    options = ["FEATURED","Souls-like","Action","F2P","Racing"],
    icons=[" "," "," "," "," "," "],
    default_index=0,
    orientation="horizontal"
    )
    ########################################## FEATURED ##########################################################################
    if select01 == "FEATURED": 
        get_featured()
    ########################################## DARK FANTASY #######################################################
    if select01 == 'Souls-like':
        get_dark()
    ########################################################################TOP ACTION##########################################
    if select01 == 'Action':
        get_action()
    ######################################################## TOP F2P ##################################################################
    if select01 == 'F2P':
        get_f2p()
    #################################################### TOP RACING #######################################################################
    if select01 == 'Racing':
        get_racing()
        
footer_container = st.container()

with footer_container:
  mission, about_us = st.columns((1,1))
  
  with mission:
    st.image("img/header.png",use_column_width=True)
    st.markdown("""<div style="text-align: justify;font-size: 14px;">Trong thế game, việc tìm kiếm và trải nghiệm các game phù hợp sở thích cá nhân trở nên dễ dàng hơn nhờ hệ thống đề xuất game. Hệ thống này cung cấp các tính năng như xem game thịnh hành, khám phá game hot theo thể loại và gợi ý game dựa trên game đã chơi, giúp bạn thoả mãn đam mê và giải trí sau những giờ học, làm căng thẳng. Chúc các bạn có trải nghiệm vui vẻ ❤🎮</div>""",unsafe_allow_html=True)
    
  with about_us:
    st.markdown("""<div style="font-size:20px; margin-bottom:8px;">About us</div>""",unsafe_allow_html=True)
    st.markdown("""<div style="text-align: justify;font-size: 14px;">Nhóm 1 của chúng tôi gồm 5 con người cùng có đam mê lập trình và game. Cùng chung tay, chúng tôi xây dựng hệ thống đề xuất này để thỏa mãn niềm đam mê của mỗi thành viên.</div>""",unsafe_allow_html=True)
    st.markdown("""<div style="font-size:20px; margin-bottom:8px; margin-top:10px">Social Media</div>""",unsafe_allow_html=True)
    image = "data:image/jpeg;base64,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"
    link = "https://www.facebook.com/groups/1178041743343458"
    st.markdown(f'<a href="{link}" target="_blank"><img src="{image}" style="width:42px; height:42px; display: inline-block; margin-right: 15px;"></a><a href="https://store.steampowered.com/app/1245620/ELDEN_RING/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/512px-Steam_icon_logo.svg.png" style="width:42px;height:42px;"></a>', unsafe_allow_html=True)
    

